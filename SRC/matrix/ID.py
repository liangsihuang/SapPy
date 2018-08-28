import numpy as np

class ID(object):
    
    def __init__(self, size=0, arraySize=0):
        self._sz = size # sz是实际数据的数量， arraySize 是数组容量的大小
        self._data = None
        self._arraySize = arraySize
        self._fromFree = 0 # 什么用？
        
        if(arraySize>0):
            self._data = np.zeros((arraySize,1), dtype = int)
    
    # utility methods
    def setData(self, newData, size, cleanIt):
        self._data = newData
        self._sz = size
        if(cleanIt==False):
            self._fromFree = 1
        else:
            self._fromFree = 0

    def Size(self):
        return self._sz

    def Zero(self):
        for i in self._data:
            i = 0
    
    def insert(self, x):
        # 二分法查找
        middle = 0
        left = 0
        right = self._sz - 1
        if(self._sz!=0):
            while(left<=right):
                middle = (left+right)/2
                dataMiddle = self._data[middle]
                if(x == dataMiddle):
                    return 1 # already there
                elif(x > dataMiddle):
                    left = middle + 1
                else:
                    right = middle - 1
        # 插入
        middle = left
        if(self._sz < self._arraySize):
            i = self._sz
            while(i>middle):
                self._data[i] = self._data[i-1]
                i = i - 1
            self._sz = self._sz + 1
            self._data[i] = x
            return 0
        else:
            newArraySize = (self._sz+1)*2
            newData = np.zeros((newArraySize,1), dtype=int)
            for i in range(0, middle):
                newData[i] = self._data[i]
                newData[middle] = x
            for j in range(middle, self._sz):
                newData[j+1] = self._data[j]
            self._sz = self._sz + 1
            self._data = newData
            self._arraySize = newArraySize
            return 0
        return -1
            
    # overloaded operators
    def __getitem__(self, x):
        return self._data[x]



        
    
    


