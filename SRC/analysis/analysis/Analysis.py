
class Analysis(object):
    def __init__(self, theDom):
        self._theDomain = theDom

    def getDomain(self):
        return self._theDomain

    def DomainChanged(self):
        pass # 纯虚函数
    

