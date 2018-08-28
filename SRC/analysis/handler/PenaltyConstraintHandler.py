from analysis.handler.ConstraintHandler import ConstraintHandler

class PenaltyConstraintHandler(ConstraintHandler):
    HANDLER_TAG_PenaltyConstraintHandler = 3
    def __init__(self, sp, mp):
        ConstraintHandler.__init__(self, self.HANDLER_TAG_PenaltyConstraintHandler)
        self.alphaSP = sp
        self.alphaMP = mp

    def handle(self, nodesNumberedLast=None):
        theDomain = self.getDomain()
        theModel = self.getAnalysisModel()
        theIntegrator = self.getIntegrator()
        
        # first check links exist to a Domain and an AnalysisModel object
        if theDomain==None or theModel==None or theIntegrator==None:
            print('WARNING PenaltyConstraintHandler::handle() - setLinks() has not been called.\n')
            return -1
        
        # get number of elements and nodes in the domain and init the theFEs and theDOFs arrays
        numSPs = 0
