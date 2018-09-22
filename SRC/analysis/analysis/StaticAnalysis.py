from SRC.analysis.analysis.Analysis import Analysis

class StaticAnalysis(Analysis):
    def __init__(self, theDomain, theHandler, theNumberer, theModel, theSolnAlgo, theLinSOE, theStaticIntegrator, theConvergenceTest=0):
        super().__init__(theDomain)
        self.theConstraintHandler = theHandler
        self.theDOF_Numberer = theNumberer
        self.theAnalysisModel = theModel
        self.theAlgorithm = theSolnAlgo
        self.theSOE = theLinSOE
        self.theEigenSOE = None
        self.theIntegrator = theStaticIntegrator
        self.theTest = theConvergenceTest

        self.domainStamp = 0

        # first we set up the links needed by the elements in the aggregation
        self.theAnalysisModel.setLinks(theDomain, theHandler)
        self.theConstraintHandler.setLinks(theDomain, theModel, theStaticIntegrator)
        self.theDOF_Numberer.setLinks(theModel)
        self.theIntegrator.setLinks(theModel, theLinSOE, theConvergenceTest)
    
    def clearAll(self):
        pass

    def analyze(self, numSteps):
        result = 0
        theDomain = self.getDomain()
        for i in range(0,numSteps):
            result = self.theAnalysisModel.analysisStep()
            if(result<0):
                print('StaticAnalysis::analyze() - the AnalysisModel failed at iteration: '+str(i))
                print(' with domain at load factor '+str(theDomain.getCurrentTime())+'.\n')
                theDomain.revertToLastCommit()
                return -2
            
            stamp = theDomain.hasDomainChanged()
            if(self.domainStamp!=stamp): 
                self.domainStamp = stamp
                result = self.domainChanged()
                if result < 0:
                    print('StaticAnalysis::analyze() - domainChanged failed at step '+str(i)+' of '+str(numSteps)+'.\n')
                    return -1

            result = self.theIntegrator.newStep()
            if result < 0:
                print('StaticAnalysis::analyze() - the Integrator failed at iteration: '+str(i))
                print(' with domain at load factor '+str(theDomain.getCurrentTime())+'.\n')
                theDomain.revertToLastCommit()
                self.theIntegrator.revertToLastStep()
                return -2

            result = self.theAlgorithm.solveCurrentStep()
            if result < 0:
                print('StaticAnalysis::analyze() - the Algorithm failed at iteration: '+str(i))
                print(' with domain at load factor '+str(theDomain.getCurrentTime())+'.\n')
                theDomain.revertToLastCommit()
                self.theIntegrator.revertToLastStep() # 不是theAlgorithm
                return -3
            
            result = self.theIntegrator.commit()
            if result < 0:
                print('StaticAnalysis::analyze() - the Integrator failed at iteration: '+str(i))
                print(' with domain at load factor '+str(theDomain.getCurrentTime())+'.\n')
                theDomain.revertToLastCommit()
                self.theIntegrator.revertToLastStep()
                return -4
            
            return 0






    def eigen(self):
        pass
    def initialize(self):
        pass

    def domainChanged(self):
        result = 0
        theDomain = self.getDomain()
        stamp = theDomain.hasDomainChanged()
        self.domainStamp = stamp

        self.theAnalysisModel.clearAll()
        self.theConstraintHandler.clearAll()

        # now we invoke handle() on the constraint handler which causes the creation of FE_Element
        # and DOF_Group objects and their addition to the AnalysisModel
        result = self.theConstraintHandler.handle()
        if result < 0:
            print('StaticAnalysis::domainChanged() - ConstraintHandler::handle() failed')
            return -1
        
        # now we invoke number() on the numberer which causes equation numbers to be assigned to all the
        # DOFs in the AnalysisModel.
        result = self.theDOF_Numberer.numberDOF()
        if result < 0:
            print('StaticAnalysis::handle() - DOF_Numberer::numberDOF() failed.')
            return -2
        
        result = self.theConstraintHandler.doneNumberingDOF()
        if result < 0:
            print('StaticAnalysis::handle() - ConstraintHandler::doneNumberingDOF() failed.')
            return -2
        # we invoke setSize() on the LinearSOE which causes that object to determine its size
        theGraph = self.theAnalysisModel.getDOFGraph()
        result = self.theSOE.setSize(theGraph)
        

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
    
    


                
        
