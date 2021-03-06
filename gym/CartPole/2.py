import gym
env = gym.make('CartPole-v0')
for i_episode in range(20):
    observation = env.reset() # reset for each new trial
    for t in range(100): # run for 100 timesteps or until done, whichever is first
        env.render()
        #print(observation)
        action = env.action_space.sample() # select a random action (see https://github.com/openai/gym/wiki/CartPole-v0)
        observation, reward, done, info = env.step(action)
        if done:
            print("Episode finished after {} timesteps".format(t+1))
            break
