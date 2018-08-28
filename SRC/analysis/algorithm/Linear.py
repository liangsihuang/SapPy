from analysis.algorithm.EquiSolnAlgo import EquiSolnAlgo

class Linear(EquiSolnAlgo):
    EquiALGORITHM_TAGS_Linear = 1
    CURRENT_TANGENT = 0

    def __init__(self, theTangent = CURRENT_TANGENT, Fact = 0):
        EquiSolnAlgo.__init__(self.EquiALGORITHM_TAGS_Linear)
        self._incrTangent = theTangent
        self._factorOnce = Fact

    def solveCurrentStep(self):
        theAnalysisModel = self.getAnalysisModel()
        theSOE = self.getLinearSOE()
        theIntegrator = self.getIncrementalIntegrator()
        if ((theAnalysisModel==None) or (theIntegrator==None) or (theSOE==None)):
            print('WARNING Linear::solveCurrentStep() - setLinks() has not been called. \n')
            return -5
        
        # form the system of equations
        # theIntegrator.formUnbalance()
        # theIntegrator.formTangent()

        # solve the system of equations
        # theLinearSOE.solveX()
        # U = getLinearSOE.getX()

        # update
        # theIntegrator.updateIncr(U)
        
        
    def setConvergenceTest(self, theNewTest):
        pass


