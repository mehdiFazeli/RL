import numpy as np


class Environment:
    def __init__(self, windowSize = 50, ratio = 3, maxCandleCheck = 20) -> None:
        self.data = np.empty([1, 4])
        self.colonmNames = []
        self.actions = [-1, 0, 1]

    def readData(self, fileName):
        self.data = np.loadtxt(fileName, delimiter="\t", dtype=str)
        self.colonmNames = self.data[0, 2: 6]
        self.data = self.data[1:, 2:6]

        self.data = [float(i) for i in self.data.flatten()]
        self.data = np.reshape(self.data, (-1, 4))

    def dataPreprocessing(self):
        pass

    def reset(self):
        pass

    def step(action):
        pass

env = Environment() 
env.readData('./data/1000_rows.csv')
print (env.colonmNames)
print (env.data)