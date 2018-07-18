# 继承自： DomainComponent
from domain.component.DomainComponent import DomainComponent

class Node(DomainComponent):

    def __init__(self, tag, ndof, Crd1, Crd2):
        # 父类
        self._theTag = tag
        self._classTag = 1
        # 自己
        self._numberDOF = ndof
        self._Crd = [Crd1, Crd2]
    
    # def getTag() 间接继承自 TaggedObject
    
        