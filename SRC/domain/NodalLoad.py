from domain.Load import Load

class NodalLoad(Load):
    LOAD_TAG_NodalLoad = 1
    def __init__(self, tag, node, theLoad, isLoadConstant=False):
        Load.__init__(self, tag, self.LOAD_TAG_NodalLoad)
        self._myNodeTag = node                 # tag indicating associated Node objects tag
        self._myNode = None              # pointer to Node object on which load acts
        self._load = theLoad                # a vector
        self._konstant = isLoadConstant     # true if load is load factor independent
    
    def setDomain(self, newDomain):
        super().setDomain(newDomain)
    
    def getNodeTag(self):
        return self._myNodeTag

    def applyLoad(self):
        pass
    
     
    
