from SRC.analysis.integrator.StaticIntegrator import StaticIntegrator

class LoadControl(StaticIntegrator):
    INTEGRATOR_TAGS_LoadControl = 6
    def __init__(self, dLambda, numIncr, minLambda, maxLambda):
        StaticIntegrator.__init__(self, self.INTEGRATOR_TAGS_LoadControl)
        self.deltaLambda = dLambda
        self.specNumIncrStep = numIncr # Jd
        self.numIncrLastStep = numIncr # J(i-1)
        self.dLambdaMin = minLambda # min values for dlambda at step(i)
        self.dLambdaMax = maxLambda # max ...

        # to avoid divide-by-zero error on first update() ensure numIncr != 0
        if numIncr == 0 :
            print('WARNING LoadControl::LoadControl() - numIncr set to 0, 1 assumed.\n')
            self.specNumIncrStep = 1.0
            self.numIncrLastStep = 1.0


    def newStep(self):
        theModel = self.theAnalysisModel
        if theModel == None:
            print('LoadControl::newStep() - no associated AnalysisModel.\n')
            return -1
        # determine delta lambda for this step based on dLambda and #iter of last step
        factor = self.specNumIncrStep / self.numIncrLastStep
        self.deltaLambda *= factor

        if self.deltaLambda < self.dLambdaMin:
            self.deltaLambda = self.dLambdaMin
        elif self.deltaLambda > self.dLambdaMax:
            self.deltaLambda = self.dLambdaMax

        currentLambda = theModel.getCurrentDomainTime()
        currentLambda += self.deltaLambda
        theModel.applyLoadDomain(currentLambda)

        self.numIncrLastStep = 0
        return 0
    
    def update(self, deltaU):
        # deltaU 是 Vector
        myModel = self.getAnalysisModel()
        theSOE = self.getLinearSOE()
        if myModel==None or theSOE==None:
            print('WARNING LoadControl::update() - No AnalysisModel or LinearSOE has been set.\n')
            return -1
        
        myModel.incrDisp(deltaU)
        if myModel.updateDomain() < 0:
            print('LoadControl::update - model failed to update for new dU.\n')
            return -1
        
        # set deltaU for the convergence test
        theSOE.setX(deltaU)
        self.numIncrLastStep += 1
        return 0
    
    def setDeltaLambda(self, newDeltaLambda):
        pass
    
    
    
    

