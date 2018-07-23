from domain.component.DomainComponent import DomainComponent

class SP_Constraint(DomainComponent):
    numSPs = 0
    nextTag = 0
    CNSTRNT_TAG_SP_Constraint = 1

    def __init__(self, node, ndof, value, ISconstant):
        SP_Constraint.nextTag = SP_Constraint.nextTag + 1
        SP_Constraint.numSPs = SP_Constraint.numSPs + 1
        # super().__init__(SP_Constraint.nextTag, SP_Constraint.CNSTRNT_TAG_SP_Constraint)
        DomainComponent.__init__(self, SP_Constraint.nextTag, SP_Constraint.CNSTRNT_TAG_SP_Constraint)
        self._nodeTag = node
        self._dofNumber = ndof
        self._valueR = value
        self._isConstant = ISconstant
    
    def __del__(self):
        SP_Constraint.numSPs = SP_Constraint.numSPs - 1
        if(SP_Constraint.numSPs == 0):
            SP_Constraint.nextTag = 0

    def getNodeTag(self):
        return self._nodeTag
    
    def getDOF_Number(self):
        return self._dofNumber
    
    


    # 还有：
    # The constraint may be time-varying .. time varying constarints however 
    # must be implemented using subclasses.