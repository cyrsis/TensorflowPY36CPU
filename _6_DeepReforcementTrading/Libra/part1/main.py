# main.py
# ========================================================================= #
#        Focus on building blocks of the Machine learning                   #
#        Everything should be start from
#
#        env should have
#        env.reset()
#        env.render()
#        env.step()
#
#                                                           #
# ========================================================================= #


from env import ArmEnv
from rl import DDPG

# Gloabel Variable
MAX_EPISOSES = 500
MAX_EP_STEPS = 500

# Set the environement
env = ArmEnv()
s_dim = env.state_dim
a_dim = env.action_dim
a_bound = env.action_bound

# set the RL method
rl = DDPG(a_dim, s_dim, a_bound)

# start Training

for i in range(MAX_EPISOSES):
    s = env.reset()
    for j in range(MAX_EP_STEPS):
        env.render()

        a = rl.choose_action(s)

        s_, r, done = env.step(a)

        rl.store_transitions(s, a, r, s_)

        if rl.memory_full:
            # start to learn once has fulfulled the memory
            rl.learn()
        s = s_
