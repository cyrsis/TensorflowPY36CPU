import gym


env = gym.make("Taxi-v2")

state = env.reset()
counter = 0
reward = None
while reward != 20:
    env.render()
    state, reward, done, info = env.step(env.action_space.sample())
    counter += 1

print(counter)