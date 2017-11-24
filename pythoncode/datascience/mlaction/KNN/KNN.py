__author__ = 'vkthakur'

from numpy import zeros
from numpy import array

class KNN:

    def __init__(self):
        self.dataset = None
        self.labels = None

    def createDataSet(self):
        self.dataset =array([[1,1],[2,2],[6,6],[8,8]])
        self.labels  = ['A', 'A', 'B', 'B']





if __name__ == '__main__':
    knn = KNN()
    knn.createDataSet()
