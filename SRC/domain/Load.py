from domain.component.DomainComponent import DomainComponent

class Load(DomainComponent):

    def __init__(self, tag, clasTag):
        DomainComponent.__init__(self, tag, clasTag)
        self._loadPatternTag = -1
    
    def applyLoad(self, loadfactor):
        pass # 纯虚函数

    def setLoadPatternTag(self, tag):
        self._loadPatternTag = tag
    
    def getLoadPatternTag(self):
        return self._loadPatternTag
    

    