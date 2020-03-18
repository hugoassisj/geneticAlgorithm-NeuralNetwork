import gym
from nn import Neural_Network, np
import os


class openAI(object):

    def __init__(self, eval):
        self.EVALUATIONS = eval
        self.env = gym.make('CartPole-v1')
        self.env._max_episode_steps = eval
        self.NN = Neural_Network()
        self.init_state = np.array([-0.01, -0.02, -0.03, 0.04])

    def run_simulation(self, weights):
        self.env.reset()
        observation = self.init_state
        self.env.env.state = self.init_state
        award = 0
        self.NN.set_weights(weights)
        for t in range(self.EVALUATIONS):
            action = self.NN.forward(observation)
            # print(action)
            if action >= 0.5:
                action = 1
            else:
                action = 0
            observation, reward, done, info = self.env.step(action)
            award += reward
            if observation[0] > 4.2 or observation[0] < -4.2:
                award -= 15
            # if observation[2] > 0.10472 or observation[2] < -0.10472:
            #     award -= 6

            if done:
                break
        # print(observation[0])
        return award

    def run_result(self, weights):
        env = gym.make('CartPole-v1')
        obsservation = env.reset()
        env.env.state = np.array([-0.01, -0.02, -0.03, 0.04])
        self.NN.set_weights(weights)
        env.render()
        for t in range(self.EVALUATIONS):
            env.render()
            action = self.NN.forward(obsservation)
            if action >= 0.5:
                action = 1
            else:
                action = 0
            obsservation, reward, done, info = env.step(action)
            if done:
                env.close()
                break
