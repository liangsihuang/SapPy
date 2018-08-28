from domain.component.DomainComponent import DomainComponent

class Node(DomainComponent):
    NOD_TAG_Node = 1
    def __init__(self, tag, ndof, Crd1, Crd2):
        DomainComponent.__init__(self, tag, self.NOD_TAG_Node)
        self._numberDOF = ndof          # number of dof at Node
        self._theDOF_Group = None    # pointer to associated DOF_Group
        self._Crd = [Crd1, Crd2]        # original nodal coords, vector

        self._commitDisp = []
        self._commitVel = []
        self._commitAccel = []

        self._trialDisp = []
        self._trialVel = []
        self._trialAccel = []    

        self._unbalLoad = []        # unbalanced load
        self._incrDisp = []
        self._incrDeltaDisp = []

        self._disp = [] # double arrays holding the disp, vel and accel value
        self._vel = []
        self._accel = []

        self._dbTag1 = 0 # needed for database
        self._dbTag2 = 0
        self._dbTag3 = 0
        self._dbTag4 = 0

        self._R = None        # nodal participation matrix
        self._mass = None     # mass matrix
        self._unbalLoadWithInertia = []
        self._alphaM = 0        # rayleigh damping factor
        self._theEigenvectors = None 

        self._reaction = []
        self._displayLocation = []

    # public methods dealing with the DOF at the node
    def getNumberDOF(self):
        return self._numberDOF
    def setDOF_Group(self, theDOF_Grp):
        self._theDOF_Group = theDOF_Grp
    def getDOF_Group(self):
        return self._theDOF_Group

    # public methods for obtaining the nodal coordinates
    def getCrds(self):
        return self._Crd
    def getDisplayCrds(self, results, fact):
        pass
    def setDisplayCrds(self, theCrds):
        pass
    # public methods for obtaining committed and trial response quantities of the node
    def getDisp(self):
        
    # public methods for updating the trial response quantities
    # public methods for adding and obtaining load information
    def zeroUnbalancedLoad(self):
        if(self._unbalLoad!=[]):
            for i in range(0,len(self._unbalLoad)):
                self._unbalLoad[i] = 0.0

    # public methods dealing with the commited state of the node
    def commitState(self):
        pass

    def revertToLastCommit(self):
        # check disp exists, if does set trial = last commit, incr = 0
        if(self._disp!=[]):
            for i in range(0,self._numberDOF):
                self._disp[i] = self._disp[i+self._numberDOF]
                self._disp[i+2*self._numberDOF] = 0.0
                self._disp[i+3*self._numberDOF] = 0.0
        # check vel exists, if does set trial = last commit
        # check accel exists, if does set trial = last commit

    def revertToStart(self):
        pass
    
    # public methods for dynamic analysis
    # public methods for eigen vector
    # public methods for output

# AddingSensitivity: BEGIN
# AddingSensitivity: END

    # private methods used to create the Vector objects 
    # for the committed and trial response quantities.
    def _createDisp(self):
        pass
    def _createVel(self):
        pass
    def _createAccel(self):
        pass



    
        