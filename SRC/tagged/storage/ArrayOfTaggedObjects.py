# 继承自：TaggedObjectStorage，但这个类所有函数都是纯虚函数，没有实现

class ArrayOfTaggedObjects(object):

    def __init__(self):
        self.theComponents = []        # 用自带的 list 实现

        self.numComponents = 0         # num of components added
        self.sizeComponentArray = 0    # size of the array

        self.positionLastEntry = 0         # marker of last position used in the array
        self.positionLastNoFitEntry = 0    # marker of place array filled up to

        self.fitFlag = True            # flag indicating if all components in nicely

        # # zero the array
        # for i in range(0,self.sizeComponentArray):
        #     self.theComponents[i] = None
    
    def clearAll(self, invokeDestrutors):
        if(invokeDestrutors==True):
            # go through and invoke the components object destructors and set the array pointer to 0
            for i in range(0,self.positionLastEntry+1):
                if(self.theComponents[i]!=None):
                    del self.theComponents[i]
                    self.theComponents[i] = None
        else:
            # just set the array pointers to 0
            for i in range(0,self.positionLastEntry+1):
                if(self.theComponents[i]!=None):
                    self.theComponents[i] = None

        self.positionLastEntry = 0
        self.positionLastNoFitEntry = 0
        self.fitFlag = True
        self.numComponents = 0

    def getComponent(self, tag):
        for tag_object in self.theComponents:
            if tag_object.getTag() == tag:
                return tag_object
        return None # it's not in the list    
    
    def addComponent(self, newComponent):
        # check no other component already exists
        other = self.getComponent(newComponent.getTag())
        if other!=None:
            print('WARNING ArrayOfTaggedObjects::addComponent() - component already exists, not adding component with tag: '
            +str(newComponent.getTag())+'.\n')
            return False
        # check if size of current array is big enough. if not resize.
        self.theComponents.append(newComponent)
        return True
    
    def getComponents(self):
        return self.theComponents




    


    
