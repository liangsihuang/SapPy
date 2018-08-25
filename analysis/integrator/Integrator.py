from actor.MovableObject import MovableObject

# 1. form the SOE
# 2. define the contributions of the FE_Element and DOF_Group objects to the SOE
# 3. update the response at the DOF_Group
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

    