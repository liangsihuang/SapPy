from analysis.integrator.Integrator import Integrator

class IncrementalIntegrator(Integrator):
    CURRENT_TANGENT = 0
    INITIAL_TANGENT = 1
    CURRENT_SECANT = 2
    INITIAL_THEN_CURRENT_TANGENT = 3
    NO_TANGENT = 4
    SECOND_TANGENT = 5

    def __init__(self, clasTag):
        super().__init__(self, clasTag)
        self._statusFlag = self.CURRENT_TANGENT

        self._theSOE = None
        self._theAnalysisModel = None
        self._theTest = None

    def setLinks(self, theModel, theLinSOE, theConvergenceTest):
        self._theAnalysisModel = theModel
        self._theSOE = theLinSOE
        self._theTest = theConvergenceTest
    
    def setEigenSOE(self):
        pass
    
    # methods to set up the system of equations
    def formTangent(self, statFlag = CURRENT_TANGENT):
        result = 0
        self._statusFlag = statFlag
        if ((self._theAnalysisModel==None) or (self._theSOE==None)):
            print('WARNING IncrementalIntegrator::formTangent() - no AnalysisModel or LinearSOE have been set. \n')
        
        # zero the A matrix of the linearSOE

    
    def formUnbalance(self):
        pass
    
    # pure virtual methods to define the FE_Ele and DOF_Group contributions
    # 在父类中定义了

    # methods to update the domain
    def newStep(self, deltaT):
        pass
    def update(self, deltaU):
        pass # 纯虚
    def commit(self):
        pass
    def revertToLastStep(self):
        pass
    def initialize(self):
        pass
    

    