from analysis.analysis.Analysis import Analysis

class AnalysisModel(Analysis):
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


