import gym


if __name__ == "__main__":
    env = gym.make("Breakout-v0")
    env.reset()

    print("Observeration Space : {} ".format(env.observation_space)) #Observeration Space : Box(210, 160, 3)
    print("Action Space        : {} ".format(env.action_space))  #Action Space        : Discrete(4)


    pendulumEnv = gym.make("Pendulum-v0")
    pendulumEnv.reset()

    print("ObServeration Space : {} ".format(pendulumEnv.observation_space))
    print("Action Space        : {} ".format(pendulumEnv.action_space))

    # for _ in range(1000):
    #     env.render()
    #     env.step(env.action_space.sample())