from element.Element import Element

class Truss(Element):

    def __init__(self, tag, dim, Nd1, Nd2, theMaterial, A, rho=0.0, doRayleighDamping=0):
        ELE_TAG_Truss = 12 # 常量应全部定义在一个外部文件
        super().__init__(tag, ELE_TAG_Truss)
        self._dimension = dim
        self._connectedExternalNodes = [Nd1, Nd2]
        self._theMaterial = theMaterial
        self._A = A
    
    def getExternalNodes(self):
        return self._connectedExternalNodes
