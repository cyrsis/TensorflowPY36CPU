# ========================================================================= #
#                              Variable 变量                                      #
# :                                                     #
# ========================================================================= #

import os

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

import tensorflow as tf

state = tf.Variable(0, name='counter')

# 定义常量 one
one = tf.constant(1)

# 定义加法步骤 (注: 此步并没有直接计算)
stateAddOne = tf.add(state, one)

# 将 State 更新成 new_value
update = tf.assign(state,one)


init = tf.global_variables_initializer()  # 替换成这样就好

with tf.Session() as sess:
    sess.run(init)
    for _ in range(3):

        sess.run(update)
        print(sess.run(state))
