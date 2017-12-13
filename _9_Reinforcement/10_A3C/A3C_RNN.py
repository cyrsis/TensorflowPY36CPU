"""
Asynchronous Advantage Actor Critic (A3C) with continuous action space, Reinforcement Learning.

The Pendulum example.

View more on my tutorial page: https://morvanzhou.github.io/tutorials/

Using:
tensorflow r1.3
gym 0.8.0
"""
# =============================================================================================== #
#                                                                                                 #
# A3C 的算法实际上就是将 Actor-Critic 放在了多个线程中进行同步训练.                                  #
# 可以想象成几个人同时在玩一样的游戏, 而他们玩游戏的经验都会同步上传到一个中央大脑.                    #
# 然后他们又从中央大脑中获取最新的玩游戏方法.                                                        #
# 这样, 对于这几个人, 他们的好处是: 中央大脑汇集了所有人的经验,                                       #
# 是最会玩游戏的一个, 他们能时不时获取到中央大脑的必杀招, 用在自己的场景中.                           #
# 对于中央大脑的好处是: 中央大脑最怕一个人的连续性更新, 不只基于一个人推送更新这种方式能打消这种连续性. #
#  使中央大脑不必有用像 DQN, DDPG 那样的记忆库  也能很好的更新.                                      #
#                                                                                                 #
# =============================================================================================== #

import multiprocessing
import threading
import tensorflow as tf
import numpy as np
import gym
import os
import shutil
import matplotlib.pyplot as plt
import datetime

GAME = 'Breakout-v0'
OUTPUT_GRAPH = True
LOG_DIR = './log'
N_WORKERS = multiprocessing.cpu_count()
MAX_EP_STEP = 200
MAX_GLOBAL_EP = 5000
GLOBAL_NET_SCOPE = 'Global_Net'
UPDATE_GLOBAL_ITER = 10
GAMMA = 0.9
ENTROPY_BETA = 0.01
LR_A = 0.0001  # learning rate for actor
LR_C = 0.001  # learning rate for critic
GLOBAL_RUNNING_R = []
GLOBAL_EP = 0

env = gym.make(GAME)

N_S = env.observation_space.shape[0]
N_A = env.action_space.shape[0]
A_BOUND = [env.action_space.low, env.action_space.high]


# 这个 class 可以被调用生成一个 global net.
# 也能被调用生成一个 worker 的 net, 因为他们的结构是一样的,
# 所以这个 class 可以被重复利用.

class ACNet(object):
    def __init__(self, scope, globalAC=None):

        # 当创建 worker 网络的时候, 我们传入之前创建的 globalAC 给这个 worker
        if scope == GLOBAL_NET_SCOPE:  ## 判断当下建立的网络是 local 还是 global
            with tf.variable_scope(scope):
                self.s = tf.placeholder(tf.float32, [None, N_S], 'S')
                self.a_params, self.c_params = self._build_net(scope)[-2:]

        else:  # local net, calculate losses
            with tf.variable_scope(scope):
                # 接着计算 critic loss 和 actor loss
                # 用这两个 loss 计算要推送的 gradients
                self.s = tf.placeholder(tf.float32, [None, N_S], 'S')
                self.a_his = tf.placeholder(tf.float32, [None, N_A], 'A')
                self.v_target = tf.placeholder(tf.float32, [None, 1], 'Vtarget')

                mu, sigma, self.v, self.a_params, self.c_params = self._build_net(scope)

                td = tf.subtract(self.v_target, self.v, name='TD_error')
                with tf.name_scope('c_loss'):
                    self.c_loss = tf.reduce_mean(tf.square(td))

                with tf.name_scope('wrap_a_out'):
                    mu, sigma = mu * A_BOUND[1], sigma + 1e-4

                normal_dist = tf.contrib.distributions.Normal(mu, sigma)

                with tf.name_scope('a_loss'):
                    log_prob = normal_dist.log_prob(self.a_his)
                    exp_v = log_prob * td
                    entropy = normal_dist.entropy()  # encourage exploration
                    self.exp_v = ENTROPY_BETA * entropy + exp_v
                    self.a_loss = tf.reduce_mean(-self.exp_v)

                with tf.name_scope('choose_a'):  # use local params to choose action
                    self.A = tf.clip_by_value(tf.squeeze(normal_dist.sample(1), axis=0), A_BOUND[0], A_BOUND[1])
                with tf.name_scope('local_grad'):
                    self.a_grads = tf.gradients(self.a_loss, self.a_params)
                    self.c_grads = tf.gradients(self.c_loss, self.c_params)

            with tf.name_scope('sync'):
                with tf.name_scope('pull'):  # 同步
                    # 更新去 global
                    self.pull_a_params_op = [l_p.assign(g_p) for l_p, g_p in zip(self.a_params, globalAC.a_params)]
                    self.pull_c_params_op = [l_p.assign(g_p) for l_p, g_p in zip(self.c_params, globalAC.c_params)]

                    # 获取 global 参数
                with tf.name_scope('push'):
                    self.update_a_op = OPT_A.apply_gradients(zip(self.a_grads, globalAC.a_params))
                    self.update_c_op = OPT_C.apply_gradients(zip(self.c_grads, globalAC.c_params))

    def _build_net(self, scope):

        # 在这里搭建 Actor 和 Critic 的网络
        # return 均值, 方差, state_value
        w_init = tf.random_normal_initializer(0., .1)

        with tf.variable_scope('actor'):
            l_a = tf.layers.dense(self.s, 200, tf.nn.relu6, kernel_initializer=w_init, name='la')
            mu = tf.layers.dense(l_a, N_A, tf.nn.tanh, kernel_initializer=w_init, name='mu')
            sigma = tf.layers.dense(l_a, N_A, tf.nn.softplus, kernel_initializer=w_init, name='sigma')
        with tf.variable_scope('critic'):
            l_c = tf.layers.dense(self.s, 100, tf.nn.relu6, kernel_initializer=w_init, name='lc')
            v = tf.layers.dense(l_c, 1, kernel_initializer=w_init, name='v')  # state value
        a_params = tf.get_collection(tf.GraphKeys.TRAINABLE_VARIABLES, scope=scope + '/actor')
        c_params = tf.get_collection(tf.GraphKeys.TRAINABLE_VARIABLES, scope=scope + '/critic')
        return mu, sigma, v, a_params, c_params

    def update_global(self, feed_dict):  # run by a local
        # 进行 push 操作
        SESS.run([self.update_a_op, self.update_c_op], feed_dict)  # local grads applies to global net

    def pull_global(self):  # run by a local
        # 进行 pull 操作
        SESS.run([self.pull_a_params_op, self.pull_c_params_op])

    def choose_action(self, s):  # run by a local
        # 根据 s 选动作
        s = s[np.newaxis, :]
        return SESS.run(self.A, {self.s: s})[0]


class Worker(object):
    def __init__(self, name, globalAC):
        self.env = gym.make(GAME).unwrapped  # 创建自己的环境
        self.name = name  # 自己的名字
        self.AC = ACNet(name, globalAC)  # 自己的 local net, 并绑定上 globalAC

    def work(self):
        global GLOBAL_RUNNING_R, GLOBAL_EP
        total_step = 1

        # s, a, r 的缓存, 用于 n_steps 更新
        buffer_s, buffer_a, buffer_r = [], [], []

        while not COORD.should_stop() and GLOBAL_EP < MAX_GLOBAL_EP:
            s = self.env.reset()
            ep_r = 0
            for ep_t in range(MAX_EP_STEP):
                if self.name == 'W_0':
                    self.env.render()
                a = self.AC.choose_action(s)
                s_, r, done, info = self.env.step(a)
                done = True if ep_t == MAX_EP_STEP - 1 else False

                ep_r += r
                buffer_s.append(s)  # 添加各种缓存
                buffer_a.append(a)
                buffer_r.append((r + 8) / 8)  # normalize

                # 每 UPDATE_GLOBAL_ITER 步 或者回合完了, 进行 sync 操作
                if total_step % UPDATE_GLOBAL_ITER == 0 or done:  # update global and assign to local net

                    # 获得用于计算 TD error 的 下一 state 的 value
                    if done:
                        v_s_ = 0  # terminal
                    else:
                        v_s_ = SESS.run(self.AC.v, {self.AC.s: s_[np.newaxis, :]})[0, 0]

                    buffer_v_target = []  # 下 state value 的缓存, 用于算 TD

                    for r in buffer_r[::-1]:  # reverse buffer r # 进行 n_steps forward view
                        v_s_ = r + GAMMA * v_s_
                        buffer_v_target.append(v_s_)
                    buffer_v_target.reverse()

                    buffer_s, buffer_a, buffer_v_target = np.vstack(buffer_s), np.vstack(buffer_a), np.vstack(
                        buffer_v_target)
                    feed_dict = {
                        self.AC.s: buffer_s,
                        self.AC.a_his: buffer_a,
                        self.AC.v_target: buffer_v_target,
                    }

                    self.AC.update_global(feed_dict)  # 推送更新去 globalAC
                    buffer_s, buffer_a, buffer_r = [], [], []  # 清空缓存
                    self.AC.pull_global()  # 获取 globalAC 的最新参数

                s = s_
                total_step += 1
                if done:
                    if len(GLOBAL_RUNNING_R) == 0:  # record running episode reward
                        GLOBAL_RUNNING_R.append(ep_r)
                    else:
                        GLOBAL_RUNNING_R.append(0.9 * GLOBAL_RUNNING_R[-1] + 0.1 * ep_r)
                    print(
                        self.name,
                        "Ep:", GLOBAL_EP,
                        "| Ep_r: %i" % GLOBAL_RUNNING_R[-1],
                    )
                    GLOBAL_EP += 1  # 加一回合
                    break  # 结束这回合


if __name__ == "__main__":
    SESS = tf.Session()
    # 这里才是真正的重点! Worker 的并行计算.

    starttime = datetime.datetime.now()
    print('Start:\t\t' + starttime.strftime("%Y-%m-%d %X"))
    with tf.device("/cpu:0"):
        OPT_A = tf.train.RMSPropOptimizer(LR_A, name='RMSPropA')
        OPT_C = tf.train.RMSPropOptimizer(LR_C, name='RMSPropC')
        GLOBAL_AC = ACNet(GLOBAL_NET_SCOPE)  # 建立 Global AC
        workers = []
        # Create worker
        for i in range(N_WORKERS):  # 创建 worker, 之后在并行
            i_name = 'W_%i' % i  # worker name
            workers.append(Worker(i_name, GLOBAL_AC))  # 每个 worker 都有共享这个 global AC

    COORD = tf.train.Coordinator()  # Tensorflow 用于并行的工具
    SESS.run(tf.global_variables_initializer())

    if OUTPUT_GRAPH:
        if os.path.exists(LOG_DIR):
            shutil.rmtree(LOG_DIR)
        tf.summary.FileWriter(LOG_DIR, SESS.graph)

    worker_threads = []
    for worker in workers:
        job = lambda: worker.work()
        t = threading.Thread(target=job)  # 添加一个工作线程
        t.start()
        worker_threads.append(t)
    COORD.join(worker_threads)  # tf 的线程调度

    endtime = datetime.datetime.now()
    duringtime = endtime - starttime
    print('Spend Time:\t' + str(duringtime))

    plt.plot(np.arange(len(GLOBAL_RUNNING_R)), GLOBAL_RUNNING_R)
    plt.xlabel('step')
    plt.ylabel('Total moving reward')
    plt.show()
