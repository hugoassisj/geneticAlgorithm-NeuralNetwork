import numpy as np

inputLayerSize = 4
hiddenLayer_1_Size = 4
hiddenLayer_2_Size = 2
outputLayerSize = 1


class Individue:
    def __init__(self):
        self.fitness = 0

        W1 = np.random.randn(inputLayerSize, hiddenLayer_1_Size)  # np.random.uniform(1.1, 3.1) *
        W2 = np.random.randn(hiddenLayer_1_Size, hiddenLayer_2_Size)
        W3 = np.random.randn(hiddenLayer_2_Size, outputLayerSize)

        self.weights = [W1, W2, W3]


class Population:

    def __init__(self, size):
        self.population = []
        for i in range(size):
            self.population.append(Individue())

    def get(self):
        return self.population

    def set(self, population):
        self.population = population

    def add(self, individue):
        self.population.append(individue)
