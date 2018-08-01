from tagged.TaggedObject import TaggedObject
import numpy as np

class FE_Element(TaggedObject):
    # static variables - single copy for all objects of the class	
    errMatrix = None # matrix
    errVector = None # vector
    theMatrices = None # array of pointers to class wide matrices
    theVectors = None # array of pointers to class wide vectors
    numFEs = 0  # number of objects

    def __init__(self, tag, ele):
        super().__init__(tag)
        # protected variables - a copy for each object of the class  
        self._myDOF_Groups = np.size(ele.getExternalNodes())
        self._myID = np.zeros((ele.getNumDOF(),), dtype=int)
        # private variables - a copy for each object of the class  
        self._numDOF = ele.getNumDOF()
        self._theModel = None
        self._myEle = ele
        self._theResidual = None # vector
        self._theTangent = None # matrix
        self._theIntegrator = None # needed for subdomain???

        if(self._numDOF<=0):
            print('FE_Element::FE_Element() - element must have 1 dof')
        
        # get element domain and check if it is valid
        theDomain = ele.getDomain()
        if(theDomain==None):
            print('FE_Element::FE_Element() - element has no domain')
        
        numGroup = ele.getNumExternalNodes()
        nodes = ele.getExternalNodes()  # ID

    # public methods for setting/obtaining mapping information
    def getDOFtags(self):
        pass
    def getID(self):
        pass
    def setAnalysisModel(self, theModel):
        pass
    def setID(self):
        pass
    
    # methods to form and obtain the tangent and residual
    def getTangent(self, theIntegrator):
        pass
    def getResidual(self, theIntegrator):
        pass
    
    # methods to allow integrator to build tangent
    def zeroTangent(self):
        pass
    def addKtToTang(self, fact=1.0):
        pass
    def addKiToTang(self, fact=1.0):
        pass
    def addKgToTang(self, fact=1.0):
        pass
    def addCtoTang(self, fact=1.0):
        pass
    def addMtoTang(self, fact=1.0):
        pass
    def addKpToTang(self, fact=1.0, numP=0):
        pass
    def storePreviousK(self, numP):
        pass
    
    # methods to allow integrator to build residual
    def zeroResidual(self):
        pass
    def addRtoResidual(self, fact=1.0):
        pass
    def addRIncInertiaToResidual(self, fact=1.0):
        pass
    
    # methods for ele-by-ele strategies
    def getTangForce(self, x, fact=1.0):
        pass
    def getK_Force(self, x, fact=1.0):
        pass
    def getKi_Force(self, x, fact=1.0):
        pass
    def getC_Force(self, x, fact=1.0):
        pass
    def getM_Force(self, x, fact=1.0):
        pass

    def addM_Force(self, accel, fact=1.0):
        pass
    def addD_Force(self, vel, fact=1.0):
        pass
    def addK_Force(self, disp, fact=1.0):
        pass
    def addKg_Force(self, disp, fact=1.0):
        pass
    
    def updateElement(self):
        pass

    def getLastIntegrator(self):
        pass
    def getLastResponse(self):
        pass
    def getElement(self):
        pass
    
    # protected:
    def addLocalM_Force(self, accel, fact=1.0):
        pass
    def addLocalD_Force(self, vel, fact=1.0):
        pass
        

    