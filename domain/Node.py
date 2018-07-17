# 继承自： DomainComponent
class Node(object):

    def __init__(self, tag, ndof, Crd1, Crd2):
        self.Crd = [Crd1, Crd2]
        