from SRC.analysis.integrator.IncrementalIntegrator import IncrementalIntegrator

class StaticIntegrator(IncrementalIntegrator):
    def __init__(self, clasTag):
        super().__init__(clasTag)
        
    # methods which define what the FE_Element and DOF_Groups add to the system of equation object
    def formEleTangent(self, theEle):
        # theEle is FE_Element
        if self.statusFlag == IncrementalIntegrator.CURRENT_TANGENT:
            theEle.zeroTangent()
            theEle.addKtToTang()
        elif self.statusFlag == IncrementalIntegrator.INITIAL_TANGENT:
            theEle.zeroTangent()
            theEle.addKiToTang()
        return 0

    def formEleResidual(self, theEle):
        # theEle is FE_Element
        # only elements residual needed
        theEle.zeroResidual()
        theEle.addRtoResidual()
        return 0

    def formNodTangent(self, theDof):
        # should never be called
        print('StaticIntegrator::formNodTangent() - this method should never have been called!\n')
        return -1

    def formNodUnbalance(self, theDof):
        # theDof is DOF_Group
        # only nodes unbalance need be added
        theDof.zeroUnbalance()
        theDof.addPtoUnbalance()
        return 0
        