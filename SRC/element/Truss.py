from SRC.element.Element import Element
import numpy as np

class Truss(Element):
    ELE_TAG_Truss = 12

    def __init__(self, tag, dim, Nd1, Nd2, theMaterial, A, r=0.0, damp=0, cm=0):
        super().__init__(tag, Truss.ELE_TAG_Truss)
        self.theMaterial = theMaterial
        self.connectedExternalNodes = np.array([Nd1, Nd2])
        self.dimension = dim   # truss in 2 or 3d domain
        self.numDOF = 0        # number of dof for truss ??

        self.theLoad = None    # pointer to the load vector P
        self.theMatrix = None  # pointer to objects matrix (a class wide Matrix) ??
        self.theVector = None  # pointer to objects vector (a class wide Vector) ??

        self.L = 0.0       # length of truss based on undeformed configuration
        self.A = A         # area of truss
        self.rho = r       # rho: mass density per unit length

        self.doRayleighDamping = damp  # flag to include Rayleigh damping
        self.cMass = cm                # consistent mass flag

        self.cosX = [0, 0, 0]      # direction cosines
        self.theNodes = [None, None] # int指针数组 对应 list , 和 connectedExternalNodes 有什么区别？一个存储节点号，一个存储节点本身
        self.initialDisp = None     # list
    
    # public methods to obtain information about dof and connectivity
    def getNumExternalNodes(self):
        return 2
    def getExternalNodes(self):
        return self.connectedExternalNodes
    def getNode(self):
        return self.theNodes
    def getNumDOF(self):
        return self.numDOF
    def setDomain(self, theDomain):
        # to set a link to the enclosing Domain and to set the node pointers
        # also determines the number of dof associated
        # with the truss element, we set matrix and vector pointers, allocate space for t matrix,
        # determine the length and set the transformation matrix

        # check Domain is not null - invoked when object removed from the a domain
        if (self.theDomain==None):
            self.theNodes = [None, None]
            self.L = 0
            return
        # first set the node pointers
        Nd1 = self.connectedExternalNodes[0]
        Nd2 = self.connectedExternalNodes[1]
        self.theNodes[0] = theDomain.getNode(Nd1)
        self.theNodes[1] = theDomain.getNode(Nd2)
        # if can't find both - send a warning message
        if self.theNodes[0]==None or self.theNodes[1]==None:
            if self.theNodes[0]==None:
                print('Truss::setDomain() - truss '+ str(self.getTag())+' node '+str(Nd1)+' does not exist in the model.\n')
            else:
                print('Truss::setDomain() - truss '+ str(self.getTag())+' node '+str(Nd2)+' does not exist in the model.\n')
                
    
    # public methods to set the state of the element
    def revertToLastCommit(self):
        return self.theMaterial.revertToLastCommit()
    
    def update(self):
        # determine the current strain given trial displacements at nodes
        strain = self.computeCurrentStrain()
        rate = self.computeCurrentStrainRate()
        return self.theMaterial.setTrialStrain(strain, rate)

    # public methods to obtain stiffness, mass, damping and residual information

    # public methods for element output

    # private
    def computeCurrentStrain(self):
        # Note: method will not be called if L == 0
        # determine the strain
        disp1 = self.theNodes[0].getTrialDisp() # Vector
        disp2 = self.theNodes[1].getTrialDisp()
        dLength = 0.0
        if self.initialDisp == None:
            for i in range(0, self.dimension):
                dLength += (disp2[i] - disp1[i]) * self.cosX[i]
        else:
            for i in range(0, self.dimension):
                dLength += (disp2[i] - disp1[i] - self.initialDisp[i]) * self.cosX[i]

        # this method should never be called with L == 0
        return dLength/self.L

    
    def computeCurrentStrainRate(self):
        # Note: method will not be called if L == 0
        # determine the strain
        vel1 = self.theNodes[0].getTrialVel()
        vel2 = self.theNodes[1].getTrialVel()
        dLength = 0.0
        for i in range(0, self.dimension):
            dLength += (vel2[i] - vel1[i]) * self.cosX[i]
        # this method should never be called with L == 0
        return dLength/self.L
