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

        self._domainStamp = 0
    
    def clearAll(self):
        pass

    def analyze(self, numSteps):
        result = 0
        the_Domain = self.getDomain()
        for i in range(0,numSteps):
            result = self._theAnalysisModel.analysisStep()
            if(result<0):
                print('StaticAnalysis::analyze() - the AnalysisModel failed ')
                print('at iteration: '+str(i)+' with domain at load factor ')
                print(str(the_Domain.getCurrentTime())+'.\n')
                the_Domain.revertToLastCommit()
                return -2
        # check for change in Domain since last step. 
        # As a change can occur in a commit() in a domaindecomp with load balancing
        # this must now be inside the loop.

        stamp = the_Domain.hasDomainChanged()
        if(stamp!=self._domainStamp): 
            self._domainStamp = stamp

    def eigen(self):
        pass
    def initialize(self):
        pass

    def domainChanged(self):
        result = 0
        the_Domain = self.getDomain()
        stamp = the_Domain.hasDomainChanged()
        self._domainStamp = stamp

        self._theAnalysisModel.clearAll()
        self._theConstraintHandler.clearAll()

        # now we invoke handle() on the constraint handler which causes the creation of FE_Element
        # and DOF_Group objects and their addition to the AnalysisModel
        result = self._theConstraintHandler.handle()
        if(result<0):
            print('StaticAnalysis::domainChanged() - ConstraintHandler::handle() failed')
            return -1
        
        # now we invoke number() on the numberer which causes equation numbers to be assigned to all the
        # DOFs in the AnalysisModel.
    
    def setNumberer(self, theNumberer):
        pass
    def setAlgorithm(self, theAlgorithm):
        pass
    def setIntegrator(self, theIntegrator):
        pass
    def setLinearSOE(self, theSOE):
        pass
    def setConvergenceTest(self, theTest):
        pass
    def setEigenSOE(self, theSOE):
        pass
    
    def getAlgorithm(self):
        pass
    def getIntegrator(self):
        pass
    def getConvergenceTest(self):
        pass
    
    


                
        
