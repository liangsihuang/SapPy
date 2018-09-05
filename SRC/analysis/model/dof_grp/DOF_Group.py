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

        DOF_Group.numDOFs += 1
        
        
    def setID(self, index, value): # 有重载，复制函数
        if index >= 0 and index <= self.numDOF:
            self.myID[index] = value
        else:
            print('WARNING DOF_Group::setID - invalid location '+str(index)+' in ID of size '+str(self.numDOF)+'.\n')

    def getID(self):
        return self.myID

    def doneID(self):
        return 0 # 有鬼用
    
    def getNodeTag(self):
        if self.myNode != None:
            return self.myNode.getTag()
        else:
            return -1

    def getNumDOF(self):
        return self.numDOF

    def getNumFreeDOF(self):
        numFreeDOF = self.numDOF
        for i in range(0, self.numDOF):
            if self.myID[i] == -1 or self.myID[i] == -4:
                numFreeDOF -= 1
        return numFreeDOF

    def getNumConstrainedDOF(self):
        numConstr = 0
        for i in range(0, self.numDOF):
            if self.myID[i] < 0:
                numConstr += 1
        return numConstr
    
    # methods to form the tangent
    def getTangent(self, theIntegrator): # 不call还写出来干嘛？
        if theIntegrator != None:
            theIntegrator.formNodTangent(self) # StaticIntegrator::formNodTangent() - this method should never have been called!
        return self.tangent # is Matrix

    def zeroTangent(self):
        self.tangent.Zero()

    def addMtoTang(self, fact = 1.0):
        pass
    def addCtoTang(self, fact = 1.0):
        pass
    
    # methods to form the unbalance
    def getUnbalance(self, theIntegrator):
        if theIntegrator != None:
            theIntegrator.formNodUnbalance(self)
        return self.unbalance # is Vector

    def zeroUnbalance(self):
        self.unbalance.Zero()

    def addPtoUnbalance(self, fact = 1.0):
        if self.myNode != None:
            if self.unbalance.addVector(1.0, self.myNode.getUnbalancedLoad(), fact) < 0 :
                print('DOF_Group::addPIncInertiaToUnbalance() - invoking addVector() on the unbalance failed.\n')
        else:
            print('DOF_Group::addPtoUnbalance() - no Node associated. Subclass should provide the method.\n')

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
        # u 是 Vector
        if self.myNode == None:
            print('DOF_Group::setNodeDisp: 0 Node Pointer.\n')
        
        disp = self.unbalance
        # disp 是 Vector
        if disp.Size() == 0:
            print('DOF_Group::setNodeIncrDisp - out of space.\n')
            return
        
        # get disp for my dof out of vector u
        for i in range(0, self.numDOF):
            loc = self.myID(i)
            if loc >= 0:
                disp[i] = u[loc]
            else:
                disp[i] = 0.0
        
        self.myNode.incrTrialDisp(disp)
    


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
    
        
        
        
        


        
    