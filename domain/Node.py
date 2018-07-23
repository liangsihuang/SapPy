from domain.component.DomainComponent import DomainComponent

class Node(DomainComponent):
    NOD_TAG_Node = 1

    def __init__(self, tag, ndof, Crd1, Crd2):
        DomainComponent.__init__(self, tag, self.NOD_TAG_Node)
        self._numberDOF = ndof
        self._Crd = [Crd1, Crd2]
    
    
        