from SRC.analysis.algorithm.EquiSolnAlgo import EquiSolnAlgo

class Linear(EquiSolnAlgo):
    EquiALGORITHM_TAGS_Linear = 1
    CURRENT_TANGENT = 0

    def __init__(self, theTangent = CURRENT_TANGENT, Fact = 0):
        EquiSolnAlgo.__init__(Linear.EquiALGORITHM_TAGS_Linear)
        self.incrTangent = theTangent
        self.factorOnce = Fact

    def solveCurrentStep(self):
        theAnalysisModel = self.getAnalysisModel()
        theSOE = self.getLinearSOE()
        theIncIntegrator = self.getIncrementalIntegrator()
        if ((theAnalysisModel==None) or (theIncIntegrator==None) or (theSOE==None)):
            print('WARNING Linear::solveCurrentStep() - setLinks() has not been called. \n')
            return -5
        
        if self.factorOnce != 2:
            if theIncIntegrator.formTangent(self.incrTangent) < 0 :
                print('WARNING Linear::solveCurrentStep() - the Integrator failed in formTangent().\n')
                return -1
            if self.factorOnce == 1:
                self.factorOnce = 2
        
        if theIncIntegrator.formUnbalance() < 0:
            print('WARNING Linear::solveCurrentStep() - the Integrator failed in formUnbalance().\n')
            return -2
        
        if theSOE.solve() < 0:
            print('WARNING Linear::solveCurrentStep() - theLinearSOE failed in solve().\n')
            return -3
        
        deltaU = theSOE.getX()

        if theIncIntegrator.update(deltaU) < 0:
            print('WARNING Linear::solveCurrentStep() - the Integrator failed in update().\n')
            return -4
        
        return 0
        
    def setConvergenceTest(self, theNewTest):
        pass


