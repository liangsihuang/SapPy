import numpy as np

class ID(object):
    
    def __init__(self, size=0):
        self.sz = size # sz是实际数据的数量， arraySize 是数组容量的大小
        self.data = None
        self.fromFree = 0 # 什么用？
        if(arraySize>0):
            self.data = np.zeros(arraySize, dtype = int)

    # utility methods
    def setData(self, newData, cleanIt=False):
        # newData is np.array, 一维，数据类型为int
        self.data = newData
        self.sz = len(self.data)
        if cleanIt == False:
            self.fromFree = 1
        else:
            self.fromFree = 0

    def Size(self):
        return self.sz

    def Zero(self):
        for i in self.data:
            i = 0
    
    def insert(self, x):
        # 二分法查找
        middle = 0
        left = 0
        right = self.sz - 1
        if(self.sz!=0):
            while(left<=right):
                middle = (left+right)/2
                dataMiddle = self.data[middle]
                if(x == dataMiddle):
                    return 1 # already there
                elif(x > dataMiddle):
                    left = middle + 1
                else:
                    right = middle - 1
        # 插入
        middle = left
        if(self.sz < self.arraySize):
            i = self.sz
            while(i>middle):
                self.data[i] = self.data[i-1]
                i = i - 1
            self.sz = self.sz + 1
            self.data[i] = x
            return 0
        else:
            newArraySize = (self.sz+1)*2
            newData = np.zeros((newArraySize,1), dtype=int)
            for i in range(0, middle):
                newData[i] = self.data[i]
                newData[middle] = x
            for j in range(middle, self.sz):
                newData[j+1] = self.data[j]
            self.sz = self.sz + 1
            self.data = newData
            self.arraySize = newArraySize
            return 0
        return -1
            
    # overloaded operators
    def __getitem__(self, x):
        return self.data[x]
    
    def __setitem__(self, key, value):
        self.data[key] = value



        
    
    


