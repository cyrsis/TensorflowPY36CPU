import gym


if __name__ == "__main__":
    env = gym.make("Breakout-v0")
    env.reset()

    print("Observeration Space : {} ".format(env.observation_space)) #Observeration Space : Box(210, 160, 3)
    print("Action Space        : {} ".format(env.action_space))  #Action Space        : Discrete(4)

for _ in range(1000):
    env.render()
    env.step(env.action_space.sample())
