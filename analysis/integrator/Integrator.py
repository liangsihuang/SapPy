from actor.MovableObject import MovableObject

class Integrator(MovableObject):
    def __init__(self, clasTag):
        super().__init__(self, clasTag)
        

    def domainChanged(self):
        return 0
    
    def formEleTangent(self, theEle):
        pass # 纯虚
    def formNodTangent(self, theDof):
        pass # 纯虚
    def formEleResidual(self, theEle):
        pass # 纯虚
    def formNodUnbalance(self, theDof):
        pass # 纯虚

    