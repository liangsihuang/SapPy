from SRC.analysis.algorithm.SolutionAlgorithm import SolutionAlgorithm

class EquiSolnAlgo(SolutionAlgorithm):

    def __init__(self, clasTag):
        super().__init__(clasTag)

        self.theModel = None
        self.theIntegrator = None
        self.theSysOfEqn = None
        self.theTest = None
    
    def setLinks(self, theNewModel, theNewIntegrator, theSOE, theConvergenceTest):
        self.theModel = theNewModel
        self.theIntegrator = theNewIntegrator
        self.theSysOfEqn = theSOE
        self.theTest = theConvergenceTest

    def solveCurrentStep(self):
        pass # 纯虚函数

    def setConvergenceTest(self, theConvergenceTest):
        self.theTest = theConvergenceTest
    
    def getConvergenceTest(self):
        return self.theTest
    
    def Print(self):
        pass # 纯虚函数

    def getAnalysisModel(self):
        return self.theModel

    def getIncrementalIntegrator(self):
        return self.theIntegrator

    def getLinearSOE(self):
        return self.theSysOfEqn
    


