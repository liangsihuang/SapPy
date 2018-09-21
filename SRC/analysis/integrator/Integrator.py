from SRC.actor.MovableObject import MovableObject

# 1. form the SOE
# 2. define the contributions of the FE_Element and DOF_Group objects to the SOE
# 3. update the response at the DOF_Group
class Integrator(MovableObject):
    def __init__(self, clasTag):
        super().__init__(clasTag)
        

    def domainChanged(self):
        return 0

    