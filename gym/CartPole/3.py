import gym
env = gym.make('CartPole-v0')
highscore = 0
for i_episode in range(20): # run 20 episodes
    observation = env.reset()
    step = 0
    points = 0 # keep track of the reward each episode
    while True: # run until episode is done
    #for t in range(100):
        step +=1
        env.render()
        action = 1 if observation[2] > 0 else 0 # if angle if positive, move right. if angle is negative, move left
        observation, reward, done, info = env.step(action)
        points += reward
        if done:
            if points > highscore: # record high score
                highscore = points
            print("Episode finished after {} timesteps".format(step+1))
            break
