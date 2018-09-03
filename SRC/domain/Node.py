from SRC.domain.component.DomainComponent import DomainComponent

class Node(DomainComponent):
    NOD_TAG_Node = 1
    def __init__(self, tag, ndof, *Crd):
        DomainComponent.__init__(self, tag, Node.NOD_TAG_Node)
        self.numberDOF = ndof          # number of dof at Node
        self.theDOF_Group = None    # pointer to associated DOF_Group
        self.Crd = Crd        # Crd是可变参数，接收到的是一个 tuple

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
    def incrTrialDisp(self, incrDispl):
        # incrDispl 是 Vector
        # check vector arg is of correct size
        if incrDispl.Size() != self.numberDOF:
            print('WARNING Node::incrTrialDisp() - incompatable sizes.\n')
            return -2
        # create a copy if no trial exists andd add committed
        if self.trialDisp == None:
            if self.createDisp() < 0:
                print('FATAL Node::incrTrialDisp() - ran out of memory.\n')
                exit(self, -1) #???
            for i in range(0, self.numberDOF):
                incrDispI = incrDispl(i)
                self.disp[i] = incrDispI
                self.disp[i+2*self.numberDOF] = incrDispI
                self.disp[i+3*self.numberDOF] = incrDispI
            return 0
        # otherwise set trial = incr + trial
        for i in range(0, self.numberDOF):
            incrDispI = incrDispl(i)
            self.disp[i] += incrDispI
            self.disp[i+2*self.numberDOF] += incrDispI
            self.disp[i+3*self.numberDOF] = incrDispI
        return 0

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
    def createDisp(self):
        pass
    def createVel(self):
        pass
    def createAccel(self):
        pass



    
        