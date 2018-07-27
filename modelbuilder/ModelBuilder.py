
class ModelBuilder(object):

    def __init__(self, theDomain):
        self._myDomain = theDomain
    
    def getDomain(self):
        return self._myDomain
    
    def buildFE_Model(self):
        pass # 纯虚函数
    