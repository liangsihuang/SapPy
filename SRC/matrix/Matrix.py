import numpy as np 

class Matrix(object):
    def __init__(self, nRows, nCols):
        self.numRows = nRows
        self.numCols = nCols
        self.dataSize = nRows * nCols
        self.data = None
        self.fromFree = 0
        if self.dataSize > 0:
            self.data = np.zeros((nRows, nCols), float)

    def setData(self, theData):
        self.data = theData
        self.dataSize = np.size(theData)
        self.numCols = np.size(theData, 0)
        self.numRows = np.size(theData, 1)
        self.fromFree = 1

    def Zero(self):
        for i in range(0, self.numRows):
            for j in range(0, self.numCols):
                self.data[i, j] = 0

    