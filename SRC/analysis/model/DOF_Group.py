from tagged.TaggedObject import TaggedObject
import numpy as np


class DOF_Group(TaggedObject):
    # static variables - single copy for all objects of the class
    numDOFs = 0

    def __init__(self, tag, node):
        super().__init__(tag) # tag 从0开始
        
        # protected variables - a copy for each object of the class  
        self.unbalance = None
        self.tangent = None
        self.myNode = node

        # private variables - a copy for each object of the class  
        self.myID = np.zeros((node.getNumberDOF(),),dtype=int)
        self.numDOF = node.getNumberDOF()

        # get number of DOF & verify valid
        numDOF = node.getNumberDOF()
        if(numDOF <= 0):
            print('DOF_Group::DOF_Group() - node must have at least 1 dof. \n')
        
        
        # initially set all the IDs to be -2
        for i in range(0, numDOF):
            self.myID[i] = -2
        
        # if this is the first DOF_Group, we now create the arrays used to store pointers to 
        # class wide matrix and vector objects used to return tangent and residual

        DOF_Group.numDOFs = DOF_Group.numDOFs + 1
        
        
    def setID(self, dof, value):
        pass
    def getID(self):
        return self.myID
    def doneID(self):
        pass
    
    def getNodeTag(self):
        pass  
    def getNumDOF(self):
        pass
    def getNumFreeDOF(self):
        pass
    def getNumConstrainedDOF(self):
        pass
    
    # methods to form the tangent
    def getTangent(self, theIntegrator):
        pass
    def zeroTangent(self):
        pass
    def addMtoTang(self, fact = 1.0):
        pass
    def addCtoTang(self, fact = 1.0):
        pass
    
    # methods to form the unbalance
    def getUnbalance(self, theIntegrator):
        pass
    def zeroUnbalance(self):
        pass
    def addPtoUnbalance(self, fact = 1.0):
        pass
    def addPIncInertiaToUnbalance(self, fact = 1.0):
        pass
    def addM_Force(self, Udotdot, fact = 1.0):
        pass
    
    def getTangForce(self, x, fact=1.0):
        pass
    def getC_Force(self, x, fact=1.0):
        pass
    def getM_Force(self, x, fact=1.0):
        pass

    # methods to obtain committed responses from the nodes
    def getCommittedDisp(self):
        pass
    def getCommittedVel(self):
        pass
    def getCommittedAccel(self):
        pass
    
    # methods to update the trial response at the nodes
    def setNodeDisp(self, u):
        pass
    def setNodeVel(self, udot):
        pass
    def setNodeAccel(self, Udotdot):
        pass
    
    def incrNodeDisp(self, u):
        pass
    def incrNodeVel(self, udot):
        pass
    def incrNodeAccel(self, Udotdot):
        pass

    # methods to set the eigen vectors
    # methods added for TransformationDOF_Groups
    def getT(self):
        pass

    # protected:
    def addLocalM_Force(self, Udotdot, fact=1.0):
        pass
    
        
        
        
        


        
    