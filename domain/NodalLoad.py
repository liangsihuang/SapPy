from domain.Load import Load

class NodalLoad(Load):
    LOAD_TAG_NodalLoad = 1
    def __init__(self, tag, node, theLoad, isLoadConstant=False):
        Load.__init__(self, tag, self.LOAD_TAG_NodalLoad)
        self._myNode = node # Node object tag
        self._konstant = isLoadConstant # true if load is load factor independent
        self._load = theLoad
    
    def getNodeTag(self):
        return self._myNode