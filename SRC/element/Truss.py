from SRC.element.Element import Element
from SRC.matrix.Vector import Vector
from SRC.matrix.ID import ID
from SRC.matrix.Matrix import Matrix
from math import sqrt
import numpy as np
class Truss(Element):
    ELE_TAG_Truss = 12
    trussM2 = Matrix(2, 2)
    trussM4 = Matrix(4, 4)
    trussM6 = Matrix(6, 6)
    trussM12 = Matrix(12, 12)
    trussV2 = Vector(2) 
    trussV4 = Vector(4)
    trussV6 = Vector(6)
    trussV12 = Vector(12)


    def __init__(self, tag, dim, Nd1, Nd2, theMaterial, A, r=0.0, damp=0, cm=0):
        super().__init__(tag, Truss.ELE_TAG_Truss)
        self.theMaterial = theMaterial
        
        self.connectedExternalNodes = ID(2)  # 存储节点号
        self.connectedExternalNodes[0] = Nd1
        self.connectedExternalNodes[1] = Nd2

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
        self.theNodes = [None, None] # 存储节点本身
        self.initialDisp = None     # narray
    
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
        # check Domain is not null - invoked when object removed from the a domain
        if (theDomain==None):
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
                # fill this in so don't segment fault later
                self.numDOF = 2
                self.theMatrix = Truss.trussM2 # ????
                self.theVector = Truss.trussV2
                return
        # now determine the number of dof and the dimesnion   
        dofNd1 = self.theNodes[0].getNumberDOF()
        dofNd2 = self.theNodes[1].getNumberDOF()
        # if differing dof at the ends - print a warning message
        if dofNd1 != dofNd2:
            print('WARNING Truss::setDomain(): nodes '+str(Nd1)+' and '+str(Nd2)+'have differing dof at ends for truss '+str(self.getTag())+'.\n')
            # fill this in so don't segment fault later
            self.numDOF = 2
            self.theMatrix = Truss.trussM2
            self.theVector = Truss.trussV2
            return
        # call the base class method
        super().setDomain(theDomain)
        # now set the number of dof for element and set matrix and vector pointer
        if self.dimension == 1 and dofNd1 == 1:
            self.numDOF = 2
            self.theMatrix = Truss.trussM2 # ????
            self.theVector = Truss.trussV2
        elif self.dimension == 2 and dofNd1 == 2:
            self.numDOF = 4
            self.theMatrix = Truss.trussM4 # ????
            self.theVector = Truss.trussV4
        elif self.dimension == 2 and dofNd1 == 3:
            self.numDOF = 6
            self.theMatrix = Truss.trussM6 # ????
            self.theVector = Truss.trussV6
        elif self.dimension == 3 and dofNd1 == 3:
            self.numDOF = 6
            self.theMatrix = Truss.trussM6 # ????
            self.theVector = Truss.trussV6
        elif self.dimension == 3 and dofNd1 == 6:
            self.numDOF = 12
            self.theMatrix = Truss.trussM12 # ????
            self.theVector = Truss.trussV12
        else:
            print('WARNING Truss::setDomain cannot handle '+str(self.dimension)+' dofs at nodes in '+str(dofNd1)+' problem.\n')
            self.numDOF = 2
            self.theMatrix = Truss.trussM2 # ????
            self.theVector = Truss.trussV2
            return
        # create the load vector
        if self.theLoad == None:
            self.theLoad = Vector(self.numDOF)
        elif self.theLoad.Size() != self.numDOF:
            self.theLoad = Vector(self.numDOF)
        # now determine the length, cosines and fill in the transformation
        # Note: t = -t(every one else uses for residual calc)
        end1Crd = self.theNodes[0].getCrds() # 都是Vector
        end2Crd = self.theNodes[1].getCrds()
        end1Disp = self.theNodes[0].getDisp()
        end2Disp = self.theNodes[1].getDisp()

        if self.dimension == 1:
            dx = end2Crd[0] - end1Crd[0]
            if self.initialDisp == None:
                iDisp = end2Disp[0] - end1Disp[0]
                if iDisp != 0:
                    self.initialDisp = np.zeros(1)
                    self.initialDisp[0] = iDisp
                    dx += iDisp
            L = sqrt(dx*dx)
            if L == 0.0:
                print('WARNING Truss::setDomain() - truss '+str(self.getTag())+' has zero length.\n')
                return
            self.cosX[0] = 1.0
        elif self.dimension == 2:
            dx = end2Crd[0] - end1Crd[0]
            dy = end2Crd[1] - end1Crd[1]
            if self.initialDisp == None:
                iDispX = end2Disp[0] - end1Disp[0]
                iDispY = end2Disp[1] - end1Disp[1]
                if iDispX!=0 or iDispY!=0:
                    self.initialDisp = np.zeros(2)
                    self.initialDisp[0] = iDispX
                    self.initialDisp[1] = iDispY
                    dx += iDispX
                    dy += iDispY
            L = sqrt(dx*dx+dy*dy)
            if L == 0.0:
                print('WARNING Truss::setDomain() - truss '+str(self.getTag())+' has zero length.\n')
                return
            self.cosX[0] = dx/L
            self.cosX[1] = dy/L
        else:
            dx = end2Crd[0] - end1Crd[0]
            dy = end2Crd[1] - end1Crd[1]
            dz = end2Crd[2] - end1Crd[2]
            if self.initialDisp == None:
                iDispX = end2Disp[0] - end1Disp[0]
                iDispY = end2Disp[1] - end1Disp[1]
                iDispZ = end2Disp[2] - end1Disp[2]
                if iDispX!=0 or iDispY!=0 or iDispZ!=0:
                    self.initialDisp = np.zeros(3)
                    self.initialDisp[0] = iDispX
                    self.initialDisp[1] = iDispY
                    self.initialDisp[2] = iDispZ
                    dx += iDispX
                    dy += iDispY
                    dz += iDispZ
            L = sqrt(dx*dx+dy*dy+dz*dz)
            if L == 0.0:
                print('WARNING Truss::setDomain() - truss '+str(self.getTag())+' has zero length.\n')
                return
            self.cosX[0] = dx/L
            self.cosX[1] = dy/L
            self.cosX[2] = dz/L

        
    
    # public methods to set the state of the element
    def commitState(self):
        if self. Kc != None:
            Kc = self.getTangentStiff()    
        retVal = self.theMaterial.commitState()
        return retVal
    
    def revertToLastCommit(self):
        return self.theMaterial.revertToLastCommit()
    def revertToStart(self):
        pass
    def update(self):
        # determine the current strain given trial displacements at nodes
        strain = self.computeCurrentStrain()
        rate = self.computeCurrentStrainRate()
        return self.theMaterial.setTrialStrain(strain, rate)

    # public methods to obtain stiffness, mass, damping and residual information
    def getKi(self):
        pass
    def getTangentStiff(self):
        if self.L == 0.0: # - problem in setDomain() no further warnings
            self.theMatrix.Zero()
            return self.theMatrix
        E = self.theMaterial.getTangent()
        # come back later and redo this if too slow
        stiff = self.theMatrix
        numDOF2 = self.numDOF / 2
        EAoverL = E * self.A / self.L
        for i in range(0, self.dimension):
            for j in range(0, self.dimension):
                temp = self.cosX[i] * self.cosX[j] * EAoverL
                stiff[i, j] = temp
                stiff[i+numDOF2, j] = -temp
                stiff[i, j+numDOF2] = -temp
                stiff[i+numDOF2, j+numDOF2] = temp
        return stiff

    def getInitialStiff(self):
        if self.L == 0.0: # - problem in setDomain() no further warnings
            self.theMatrix.Zero()
            return self.theMatrix
        E = self.theMaterial.getInitialTangent()  
        # come back later and redo this if too slow
        stiff = self.theMatrix
        numDOF2 = self.numDOF / 2
        EAoverL = E * self.A / self.L
        for i in range(0, self.dimension):
            for j in range(0, self.dimension):
                temp = self.cosX[i] * self.cosX[j] * EAoverL
                stiff[i, j] = temp
                stiff[i+numDOF2, j] = -temp
                stiff[i, j+numDOF2] = -temp
                stiff[i+numDOF2, j+numDOF2] = temp
        return stiff

    def getDamp(self):
        pass
    def getMass(self):
        pass
    
    def zeroLoad(self):
        self.theLoad.Zero()

    def addLoad(self, theLoad, loadFactor): # Truss 单元没有分布力
        print('Truss::addLoad - load type unknown for truss with tag: '+str(self.getTag())+'.\n')
        return -1

    def addInertiaLoadToUnbalance(self, accel):
        pass

    def getresistingForce(self):
        if self.L == 0.0: # - problem in setDomain() no further warnings
            self.theVector.Zero()
            return self.theVector
        
        # R = Ku - Pext
        # Ku = F * transformation
        force = self.A * self.theMaterial.getStress()
        numDOF2 = self.numDOF / 2
        for i in range(0, self.dimension):
            temp = self.cosX[i] * force
            self.theVector[i] = -temp
            self.theVector[i+numDOF2] = temp
        return self.theVector 
        

    def getResistingForceIncInertia(self):
            return super().getResistingForceIncInertia()
    

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
