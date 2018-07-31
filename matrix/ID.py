import numpy as np

class ID(object):
    
    def __init__(self, size=0):
        self._sz = size
        self._data = None
        self._arraySize = size
        self._fromFree = 0

        if(size>0):
            self._data = np.zeros((size,), dtype = int)
    
    def setData(self, newData):
        self._data = newData
    
    def Size(self):
        return self._sz
    
    def __getitem__(self, x):
        return self._data[x]
    
    def __setitem__(self, x):
        
    
    


