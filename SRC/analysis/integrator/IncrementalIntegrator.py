from SRC.analysis.integrator.Integrator import Integrator

class IncrementalIntegrator(Integrator):
    CURRENT_TANGENT = 0
    INITIAL_TANGENT = 1
    CURRENT_SECANT = 2
    INITIAL_THEN_CURRENT_TANGENT = 3
    NO_TANGENT = 4
    SECOND_TANGENT = 5

    def __init__(self, clasTag):
        super().__init__(self, clasTag)
        self.statusFlag = self.CURRENT_TANGENT

        self.theSOE = None
        self.theAnalysisModel = None
        self.theTest = None

    def setLinks(self, theModel, theLinSOE, theConvergenceTest):
        self.theAnalysisModel = theModel
        self.theSOE = theLinSOE
        self.theTest = theConvergenceTest
    
    def setEigenSOE(self):
        pass
    
    # methods to set up the system of equations
    def formTangent(self, statFlag = CURRENT_TANGENT):
        self.statusFlag = statFlag

        if ((self.theAnalysisModel==None) or (self.theSOE==None)):
            print('WARNING IncrementalIntegrator::formTangent() - no AnalysisModel or LinearSOE have been set. \n')
            return -1
        
        # zero the A matrix of the linearSOE
        self.theSOE.zeroA()
        
        # the loops to form and add the tangents are broken into two for efficiency when performing parallel computations - CHANGE
        # loop through the FE_Elements adding their contributions to the tangent
        theEles2 = self.theAnalysisModel.getFEs()
        for ele in theEles2:
            result = self.theSOE.addA(ele.getTangent(self), ele.getID())
            if result < 0:
                print('WARNING IncrementalIntegrator::formTangent - failed in addA for ID '+str(ele.getID())+' .\n')
                return -3

        return 0
    
    def formUnbalance(self):
        if self.theAnalysisModel == None or self.theSOE == None:
            print('WARNING IncrementalIntegrator::formUnbalance - no AnalysisModel or LinearSOE has been set.\n')
            return -1
        self.theSOE.zeroB()

        if self.formElementResidual() < 0:
            print('WARNING IncrementalIntegrator::formUnbalance - this->formElementResidual failed.\n')
            return -1
        
        if self.formNodalUnbalance() < 0:
            print('WARNING IncrementalIntegrator::formUnbalance - this->formNodalUnbalance failed.\n')
            return -2
        
        return 0

    # methods to update the domain
    def commit(self):
        if self.theAnalysisModel == None:
            print('WARNING IncrementalIntegrator::commit() - no AnalysisModel object associated with this object.\n')
            return -1
        return self.theAnalysisModel.commitDomain()

    # protected:
    def getLinearSOE(self):
        return self.theSOE

    def getAnalysisModel(self):
        return self.theAnalysisModel

    def getConvergenceTest(self):
        return self.theTest

    def formElementResidual(self):
        # loop through the FE_Elements and add the residual
        theEles2 = self.theAnalysisModel.getFEs()
        for ele in theEles2:
            result = self.theSOE.addB(ele.getResidual(self), ele.getID())
            if result < 0:
                print('WARNING IncrementalIntegrator::formElementResidual - failed in addB for ID '+str(ele.getID())+'.\n')
                return -2
        return 0
    

    def formNodalUnbalance(self):
        # loop through the DOF_Groups and add the unbalance
        theDOFs = self.theAnalysisModel.getDOFs()
        for dof in theDOFs:
            result = self.theSOE.addB(dof.getUnbalance(self), dof.getID())
            if result < 0:
                print('WARNING IncrementalIntegrator::formNodalUnbalance - failed in addB for ID '+str(dof.getID())+'.\n')
                return -2    
        return 0
    
        

    