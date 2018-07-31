from element.Element import Element
import numpy as np

class Truss(Element):
    ELE_TAG_Truss = 12

    def __init__(self, tag, dim, Nd1, Nd2, theMaterial, A, r=0.0, damp=0, cm=0):
        super().__init__(tag, Truss.ELE_TAG_Truss)
        self._theMaterial = theMaterial
        self._connectedExternalNodes = np.array([Nd1, Nd2])
        self._dimension = dim   # truss in 2 or 3d domain
        self._numDOF = 0        # number of dof for truss ??

        self._theLoad = None    # pointer to the load vector P
        self._theMatrix = None  # pointer to objects matrix (a class wide Matrix) ??
        self._theVector = None  # pointer to objects vector (a class wide Vector) ??

        self._L = 0.0       # length of truss based on undeformed configuration
        self._A = A         # area of truss
        self._rho = r       # rho: mass density per unit length

        self._doRayleighDamping = damp  # flag to include Rayleigh damping
        self._cMass = cm                # consistent mass flag

        self._cosX = [0, 0, 0]      # direction cosines
        self._theNodes = [None, None]
        self._initialDisp = None
    
    # public methods to obtain information about dof and connectivity
    def getNumExternalNodes(self):
        return 2
    def getExternalNodes(self):
        return self._connectedExternalNodes
    def getNode(self):
        return self._theNodes
    def getNumDOF(self):
        return self._numDOF
    def setDomain(self, theDomain):
        # to set a link to the enclosing Domain and to set the node pointers
        # also determines the number of dof associated
        # with the truss element, we set matrix and vector pointers, allocate space for t matrix,
        # determine the length and set the transformation matrix

        # check Domain is not null - invoked when object removed from the a domain
        if (self._theDomain==None):
            self._theNodes = [None, None]
            self._L = 0
        
        # first set the node pointers
        Nd1 = self._connectedExternalNodes[0]
         
    
    # public methods to set the state of the element
    def revertToLastCommit(self):
        return self._theMaterial.revertToLastCommit()
    # public methods to obtain stiffness, mass, damping and residual information

    # public methods for element output

