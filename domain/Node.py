from domain.component.DomainComponent import DomainComponent

class Node(DomainComponent):
    NOD_TAG_Node = 1
# constructors
    def __init__(self, tag, ndof, Crd1, Crd2):
        DomainComponent.__init__(self, tag, self.NOD_TAG_Node)
        self._numberDOF = ndof
        self._Crd = [Crd1, Crd2]

        self._disp = [] # double arrays holding the disp, vel and accel value
        self._vel = []
        self._accel = []

        self._unbalLoad = [] # unbalanced load

    # destructor
    # public methods dealing with the DOF at the node
    # public methods for obtaining the nodal coordinates
    # public methods for obtaining committed and trial response quantities of the node
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



    
        