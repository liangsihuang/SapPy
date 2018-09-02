from SRC.analysis.integrator.IncrementalIntegrator import IncrementalIntegrator

class StaticIntegrator(IncrementalIntegrator):
    def __init__(self, clasTag):
        super().__init__(self, clasTag)
        
    # methods which define what the FE_Element and DOF_Groups add to the system of equation object
    def formEleTangent(self, theEle):
        pass
    def formEleResidual(self, theEle):
        pass
    def formNodTangent(self, theDof):
        pass
    def formNodUnbalance(self, theDof):
        pass