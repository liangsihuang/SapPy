from SRC.domain.component.DomainComponent import DomainComponent

class Node(DomainComponent):
    NOD_TAG_Node = 1
    def __init__(self, tag, ndof, Crd1, Crd2):
        DomainComponent.__init__(self, tag, Node.NOD_TAG_Node)
        self.numberDOF = ndof          # number of dof at Node
        self.theDOF_Group = None    # pointer to associated DOF_Group
        self.Crd = [Crd1, Crd2]        # original nodal coords, vector

        self.commitDisp = []
        self.commitVel = []
        self.commitAccel = []

        self.trialDisp = []
        self.trialVel = []  
        self.trialAccel = []    

        self.unbalLoad = []        # unbalanced load
        self.incrDisp = []
        self.incrDeltaDisp = []

        self.disp = [] # double arrays holding the disp, vel and accel value
        self.vel = []
        self.accel = []

        # self.dbTag1 = 0 # needed for database
        # self.dbTag2 = 0
        # self.dbTag3 = 0
        # self.dbTag4 = 0

        self.R = None        # nodal participation matrix
        self.mass = None     # mass matrix
        self.unbalLoadWithInertia = []
        self.alphaM = 0        # rayleigh damping factor
        self.theEigenvectors = None 

        self.reaction = []
        self.displayLocation = []

    # public methods dealing with the DOF at the node
    def getNumberDOF(self):
        return self.numberDOF
    def setDOF_Group(self, theDOF_Grp):
        self.theDOF_Group = theDOF_Grp
    def getDOF_Group(self):
        return self.theDOF_Group

    # public methods for obtaining the nodal coordinates
    def getCrds(self):
        return self.Crd
    def getDisplayCrds(self, results, fact):
        pass
    def setDisplayCrds(self, theCrds):
        pass
    # public methods for obtaining committed and trial response quantities of the node
    def getDisp(self):
        pass
    # public methods for updating the trial response quantities
    # public methods for adding and obtaining load information
    def zeroUnbalancedLoad(self):
        if(self.unbalLoad!=[]):
            for i in range(0,len(self.unbalLoad)):
                self.unbalLoad[i] = 0.0

    # public methods dealing with the commited state of the node
    def commitState(self):
        pass

    def revertToLastCommit(self):
        # check disp exists, if does set trial = last commit, incr = 0
        if(self.disp!=[]):
            for i in range(0,self.numberDOF):
                self.disp[i] = self.disp[i+self.numberDOF]
                self.disp[i+2*self.numberDOF] = 0.0
                self.disp[i+3*self.numberDOF] = 0.0
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



    
        