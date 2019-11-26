import gym
from nn import Neural_Network, np


class openAI(object):

    def __init__(self, eval):
        self.EVALUATIONS = eval
        self.env = gym.make('CartPole-v1')
        self.env._max_episode_steps = eval
        self.NN = Neural_Network()
        self.init_state = np.array([-0.01799011, -0.03709275, -0.04547845, 0.04748696])

    def run_simulation(self, weights):
        self.env.reset()
        observation = self.init_state
        self.env.env.state = self.init_state
        award = 0
        self.NN.set_weights(weights)
        for t in range(self.EVALUATIONS):
            action = self.NN.forward(observation)
            if action >= 0.5:
                action = 1
            else:
                action = 0
            observation, reward, done, info = self.env.step(action)
            award += reward
            if done:
                break
        return award

    def run_result(self, weights):
        obsservation = self.env.reset()
        self.NN.set_weights(weights)
        for t in range(self.EVALUATIONS):
            self.env.render()
            action = self.NN.forward(obsservation)
            if action >= 0.5:
                action = 1
            else:
                action = 0
            obsservation, reward, done, info = self.env.step(action)
            if done:
                self.env.close()
                break
