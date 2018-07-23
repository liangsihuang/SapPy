from analysis.analysis.Analysis import Analysis

class StaticAnalysis(Analysis):
    def __init__(self, theDomain, theHandler, theNumberer, theModel, theSolnAlgo, theLinSOE, theStaticIntegrator, theConvergenceTest=0):
        super().__init__(theDomain)
        self._theConstraintHandler = theHandler
        self._theDOF_Numberer = theNumberer
        self._theAnalysisModel = theModel
        self._theAlgorithm = theSolnAlgo
        self._theSOE = theLinSOE
        self._theEigenSOE = None
        self._theIntegrator = theStaticIntegrator
        self._theTest = theConvergenceTest

    def analyze(self, numSteps):
        the_Domain = self.getDomain()
        result = 0

        for i in range(0,numSteps,1):
            result = self._theAnalysisModel.analysisStep()
            if(result<0):
                print('StaticAnalysis::analyze() - the AnalysisModel failed ')
                print('at iteration: '+str(i)+' with domain at load factor ')
                print(str(the_Domain.getCurrentTime())+'.\n')
                
        
