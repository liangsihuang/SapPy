from SRC.domain.component.DomainComponent import DomainComponent

class Load(DomainComponent):

    def __init__(self, tag, clasTag):
        DomainComponent.__init__(self, tag, clasTag)
        self.loadPatternTag = -1
    
    def applyLoad(self, loadfactor):
        pass # 纯虚函数

    def setLoadPatternTag(self, tag):
        self.loadPatternTag = tag
    
    def getLoadPatternTag(self):
        return self.loadPatternTag
    

    