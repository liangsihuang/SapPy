import numpy as np

class Vector(object):
    def __init__(self, size = 0, data = None):
        self.sz = size   # int
        self.data = data # np.narray
        self.fromFree = 0
        if (size > 0) and (data == None).all():
            self.data = np.zeros(size)
        if (size != 0) and (data != None).all():
            self.fromFree = 1

    # utility methods
    def setData(self, newData, size):
        self.sz = size
        self.newData = newData
        self.fromFree = 1
    
    def Assemble(self, V, l, fact = 1.0):
        pass
    
    def Norm(self):
        pass
    def pNorm(self):
        pass
    def Size(self):
        return self.sz
    
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
    def __setitem__(self, key, value):
        self.data[key] = value
        
    def __getitem__(self, x):
        return self.data[x]       