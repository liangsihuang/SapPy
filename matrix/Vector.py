import numpy as np
class Vector(object):
    def __init__(self, size = 0, data = None):
        self._sz = size
        self._data = data
        self._fromFree = 0
        if (size > 0) and (data == None):
            self._data = np.zeros((size,1))
        if (size != 0) and (data != None):
            self._fromFree = 1

    # utility methods
    def setData(self, newData, size):
        self._sz = size
        self._newData = newData
        self._fromFree = 1
    
    def Assemble(self, V, l, fact = 1.0):
        pass
    
    def Norm(self):
        pass
    def pNorm(self):
        pass
    def Size(self):
        return self._sz
    
    def resize(self, newSize):
        pass
    def Zero(self):
        pass
    def Normalize(self):
        pass
    
    def addVector(self, factThis, other, factOther):
        pass
    def addMatrixVector(self, factThis, m, v, factOther):
        pass
    def addMatrixTransposeVector(self, factThis, m, v, factOther):
        pass
    
    # overloaded operators