import numpy as np


class Neural_Network(object):
    def __init__(self):
        # Define Hyperparameters
        self.inputLayerSize = 4
        self.hiddenLayer_1_Size = 4
        self.hiddenLayer_2_Size = 2
        self.outputLayerSize = 1

    def forward(self, X):
        # Propagate inputs though network
        self.z2 = np.dot(X, self.W1)
        self.a2 = self.relu(self.z2)
        self.z3 = np.dot(self.a2, self.W2)
        self.a3 = self.relu(self.z3)
        self.z4 = np.dot(self.a3, self.W3)
        yHat = self.relu(self.z4)
        return yHat

    def set_weights(self, weights):
        self.W1 = weights[0]
        self.W2 = weights[1]
        self.W3 = weights[2]

    def relu(self, data):
        # Apply sigmoid activation function to scalar, vector, or matrix
        return np.maximum(data, 0)
