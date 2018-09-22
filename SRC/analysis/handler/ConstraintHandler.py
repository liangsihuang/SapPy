from SRC.actor.MovableObject import MovableObject

# Responsible for creating the DOF_Group and FE_Element objects, and adding them to the AnalysisModel.
# Also responsible for assigning an initial mapping of dof to equation numbers.

class ConstraintHandler(MovableObject):

    def __init__(self, clasTag):
        super().__init__(clasTag)
        self.theDomain = None
        self.theAnalysisModel = None
        self.theIntegrator = None

    def setLinks(self, theDomain, theModel, theIntegrator):
        self.theDomain = theDomain
        self.theAnalysisModel = theModel
        self.theIntegrator = theIntegrator
    
    def doneNumberingDOF(self):
        # iterate through the FE_Element getting them to set their IDs
        for theEle in self.theAnalysisModel.getFEs():
            theEle.setID()
        return 0
    
    def getDomain(self):
        return self.theDomain
    def getAnalysisModel(self):
        return self.theAnalysisModel
    def getIntegrator(self):
        return self.theIntegrator
    
    def clearAll(self):
        # for the nodes reset the DOF_Group pointers to 0
        theDomain = self.getDomain()
        if theDomain is None:
            return
        theNodes = theDomain.getNodes()
        for tag in theNodes:
            theNod = theNodes.getComponent(tag)
            theNod.setDOF_Group(None)
    
    def applyLoad(self):
        return 0 # 有什么作用？可能有些子类不需要，有些子类要重写这个方法。保证代码通用？
