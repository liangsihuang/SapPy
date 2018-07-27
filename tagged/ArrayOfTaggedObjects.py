# 继承自：TaggedObjectStorage，但这个类所有函数都是纯虚函数，没有实现

class ArrayOfTaggedObjects(object):

    def __init__(self, size):
        self._theComponents = []        # the array

        self._numComponents = 0         # num of components added
        self._sizeComponentArray = size    # size of the array

        self._positionLastEntry = 0         # marker of last position used in the array
        self._positionLastNoFitEntry = 0    # marker of place array filled up to

        self._fitFlag = True            # flag indicating if all components in nicely

        # zero the array
        for i in range(0,size):
            self._theComponents[i] = None
    
    def clearAll(self, invokeDestrutors):
        if(invokeDestrutors==True):
            # go through and invoke the components object destructors and set the array pointer to 0
            for i in range(0,self._positionLastEntry+1):
                if(self._theComponents[i]!=None):
                    del self._theComponents[i]
                    self._theComponents[i] = None
        else:
            # just set the array pointers to 0
            for i in range(0,self._positionLastEntry+1):
                if(self._theComponents[i]!=None):
                    self._theComponents[i] = None

        self._positionLastEntry = 0
        self._positionLastNoFitEntry = 0
        self._fitFlag = True
        self._numComponents = 0
    




    


    
