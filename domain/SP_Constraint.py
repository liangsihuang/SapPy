from domain.component.DomainComponent import DomainComponent

class SP_Constraint(DomainComponent):
    numSPs = 0
    nextTag = 0
    CNSTRNT_TAG_SP_Constraint = 1

    def __init__(self, node, ndof, value, ISconstant):
        SP_Constraint.nextTag = SP_Constraint.nextTag + 1
        super().__init__(SP_Constraint.nextTag, SP_Constraint.CNSTRNT_TAG_SP_Constraint)
        self._nodeTag = node
        self._dofNumber = ndof
        self._valueR = value
        self._valueC = value
        self._isConstant = ISconstant
        self._loadPatternTag = -1
        
        SP_Constraint.numSPs = SP_Constraint.numSPs + 1

    
    def __del__(self):
        SP_Constraint.numSPs = SP_Constraint.numSPs - 1
        if(SP_Constraint.numSPs == 0):
            SP_Constraint.nextTag = 0

    def getNodeTag(self):
        return self._nodeTag
    
    def getDOF_Number(self):
        return self._dofNumber
    
    def applyConstraint(self, loadFactor):
        # as SP_Constraint objects are time invariant nothing is done
        if (self._isConstant == False):
            self._valueC = loadFactor*self._valueR
        return 0
    # 还有：
    # The constraint may be time-varying .. time varying constarints however 
    # must be implemented using subclasses.
    
    def getValue(self):
        pass
    
    def isHomogeneous(self):
        pass
    
    def setLoadPatternTag(self, loadPatternTag):
        pass

    def getLoadPatternTag(self):
        pass
    
    def sendSelf(self):
        pass
    def recvSelf(self):
        pass
    def Print(self):
        pass
