from actor.MovableObject import MovableObject

# Responsible for creating the DOF_Group and FE_Element objects, and adding them to the AnalysisModel.
# Also responsible for assigning an initial mapping of dof to equation numbers.

class ConstraintHandler(MovableObject):

    def __init__(self, clasTag):
        super().__init__(clasTag)
        self._theDomain = None
        self._theAnalysisModel = None
        self._theIntegrator = None

    def setLinks(self, theDomain, theModel, theIntegrator):
        self._theDomain = theDomain
        self._theAnalysisModel = theModel
        self._theIntegrator = theIntegrator
    
    def handle(self, nodesNumberedLast=None):
        pass # 纯虚
    def update(self):
        return # 纯虚
    def applyLoad(self):
        pass # 纯虚
    def doneNumberingDOF(self):
        # iterate through the FE_Element getting them to set their IDs
        for theEle in self._theAnalysisModel.getFEs():
            theEle.setID()

    def clearAll(self):
        pass # 纯虚
    
    def getDomain(self):
        return self._theDomain
    def getAnalysisModel(self):
        return self._theAnalysisModel
    def getIntegrator(self):
        return self._theIntegrator
    
