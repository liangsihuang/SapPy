from analysis.algorithm.SolutionAlgorithm import SolutionAlgorithm

class EquiSolnAlgo(SolutionAlgorithm):

    def __init__(self, clasTag):
        super().__init__(self, clasTag)

        self._theModel = None
        self._theIntegrator = None
        self._theSysOfEqn = None
        self._theTest = None
    
    def setLinks(self, theNewModel, theNewIntegrator, theSOE, theConvergenceTest):
        self._theModel = theNewModel
        self._theIntegrator = theNewIntegrator
        self._theSysOfEqn = theSOE
        self._theTest = theConvergenceTest

    def solveCurrentStep(self):
        pass # 纯虚函数

    def setConvergenceTest(self, theConvergenceTest):
        self._theTest = theConvergenceTest
    
    def getConvergenceTest(self):
        return self._theTest
    
    def Print(self):
        pass # 纯虚函数

    def getAnalysisModel(self):
        return self._theModel

    def getIncrementalIntegrator(self):
        return self._theIntegrator

    def getLinearSOE(self):
        return self._theSysOfEqn
    


