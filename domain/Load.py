from domain.component.DomainComponent import DomainComponent

class Load(DomainComponent):

    def __init__(self, tag, clasTag):
        DomainComponent.__init__(self, tag, clasTag)
        self._loadPatternTag = -1

    def setLoadPatternTag(self, tag):
        self._loadPatternTag = tag
    
    def getLoadPatternTag():
        return self._loadPatternTag