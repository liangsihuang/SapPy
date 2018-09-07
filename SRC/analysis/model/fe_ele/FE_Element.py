from SRC.tagged.TaggedObject import TaggedObject
import numpy as np
from SRC.matrix.Vector import Vector

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
        self.myDOF_Groups = np.size(ele.getExternalNodes().Size())
        self.myID = np.zeros((ele.getNumDOF(),), dtype=int)
        # private variables - a copy for each object of the class  
        self.numDOF = ele.getNumDOF()
        self.theModel = None
        self.myEle = ele
        self.theResidual = None # vector
        self.theTangent = None # matrix
        self.theIntegrator = None # needed for subdomain???

        if(self.numDOF<=0):
            print('FE_Element::FE_Element() - element must have 1 dof')
        
        # get element domain and check if it is valid
        theDomain = ele.getDomain()
        if(theDomain==None):
            print('FE_Element::FE_Element() - element has no domain')
        
        numGroup = ele.getNumExternalNodes()
        nodes = ele.getExternalNodes()  # ID

    # public methods for setting/obtaining mapping information
    def getDOFtags(self):
        return self.myDOF_Groups

    def getID(self):
        return self.myID

    def setAnalysisModel(self, theAnalysisModel):
        self.theModel = theAnalysisModel

    def setID(self):
        current = 0
        if self.theModel == None:
            print('WARNING FE_Element::setID() - no AnalysisModel set.\n')
            return -1
        numGrps = self.myDOF_Groups.Size()
        for i in range(0, numGrps):
            tag = self.myDOF_Groups[i]
            dof = self.theModel.getDOF_Group(tag)
            if dof == None:
                print('WARNING FE_Element::setID: 0 DOF_Group Pointer.\n')
                return -2
            theDOFid = dof.getID()
            for j in range(0, theDOFid.Size()):
                if current < self.numDOF:
                    self.myID[current] = theDOFid[j]
                    current += 1
                else:
                    print('WARNING FE_Element::setID() - numDOF and  number of dof at the DOF_Groups.\n')
                    return -3
        return 0
    
    # methods to form and obtain the tangent and residual
    def getTangent(self, theNewIntegrator): # subdomain 未编
        self.theIntegrator = theNewIntegrator
        if self.myEle == None:
            print('FATAL FE_Element::getTangent() - no Element *given.\n')
            exit(self, -1)
        if self.myEle.isSubdomain() == False:
            if theNewIntegrator != None:
                theNewIntegrator.formEleTangent(self)
                return self.theTangent
        else:
            pass

    def getResidual(self, theNewIntegrator):
        self.theIntegrator = theNewIntegrator
        if self.theIntegrator == None:
            return self.theResidual
        if self.myEle == None:
            print('FATAL FE_Element::getTangent() - no Element *given.\n')
            exit(self, -1)
        if self.myEle.isSubdomain() == False:
            theNewIntegrator.formEleResidual(self)
            return self.theResidual
        else:
            pass
    
    # methods to allow integrator to build tangent
    def zeroTangent(self):
        if self.myEle != None:
            if self.myEle.isSubdomain() == False:
                self.theTangent.Zero()
            else:
                print('WARNING FE_Element::zeroTangent() - this should not be called on a Subdomain!\n')

    def addKtToTang(self, fact=1.0):
        if self.myEle != None:
            # check for a quick return	
            if fact == 0.0:
                return 
            elif self.myEle.isSubdomain() == False:
                self.theTangent.addMatrix(1.0, self.myEle.getTangentStiff(), fact)
            else:
                print('WARNING FE_Element::addKToTang() -this should not be called on a Subdomain!\n')

    def addKiToTang(self, fact=1.0):
        if self.myEle != None:
            # check for a quick return 
            if fact == 0.0:
                return 
            elif self.myEle.isSubdomain() == False:
                self.theTangent.addMatrix(1.0, self.myEle.getInitialStiff(), fact)
            else:
                print('WARNING FE_Element::addKiToTang() - this should not be called on a Subdomain!\n')

    def addKgToTang(self, fact=1.0):
        if self.myEle != None:
            # check for a quick return 
            if fact == 0.0:
                return 
            elif self.myEle.isSubdomain() == False:
                self.theTangent.addMatrix(1.0, self.myEle.getGeometricTangentStiff(), fact)
            else:
                print('WARNING FE_Element::addKgToTang() - this should not be called on a Subdomain!\n')


    def addCtoTang(self, fact=1.0):
        pass
    def addMtoTang(self, fact=1.0):
        pass

    def addKpToTang(self, fact=1.0, numP=0):
        if self.myEle != None:
            # check for a quick return 
            if fact == 0.0:
                return 
            elif self.myEle.isSubdomain() == False:
                thePrevMat = self.myEle.getPreviousK(numP)
                if thePrevMat != None:
                    self.theTangent.addMatrix(1.0, thePrevMat, fact)
            else:
                print('WARNING FE_Element::addKpToTang() - this should not be called on a Subdomain!\n')

    def storePreviousK(self, numP):
        res = None
        if self.myEle != None:
            res = self.myEle.storePreviousK(numP)
        return res
    
    # methods to allow integrator to build residual
    def zeroResidual(self):
        if self.myEle != None:
            if self.myEle.isSubdomain() == False:
                self.theResidual.Zero()
            else:
                print('WARNING FE_Element::zeroResidual() - this should not be called on a Subdomain!\n')
        else:
            print('FATAL FE_Element::zeroResidual() - no Element *given.\n')

    def addRtoResidual(self, fact=1.0):
        if self.myEle != None:
            # check for a quick return 
            if fact == 0.0:
                return 
            eleResisting = self.myEle.getResistingForce()
            self.theResidual.addVector(1.0, eleResisting, -fact)
        else:
            print('FATAL FE_Element::addRtoResidual() - no Element *given.\n')


    def addRIncInertiaToResidual(self, fact=1.0):
        pass
    
    # methods for ele-by-ele strategies
    def getTangForce(self, disp, fact=1.0):
        if self.myEle != None:
            # zero out the force vector
            self.theResidual.Zero()
            # check for a quick return
            if fact == 0.0:
                return self.theResidual
            # get the component we need out of the vector and place in a temporary vector
            tmp = Vector(self.numDOF)
            for i in range(0, self.numDOF):
                dof = self.myID[i]
                if dof >= 0:
                    tmp[i] = disp[dof]
                else:
                    tmp[i] = 0.0
            # form the tangent again and then add the force
            self.theIntegrator.formEleTangent(self)
            if self.theResidual.addMatrixVector(1.0, self.theTangent, tmp, fact) < 0:
                print('WARNING FE_Element::getTangForce() - addMatrixVector returned error.\n')
            return self.theResidual
        else:
            print('WARNING FE_Element::addTangForce() - no Element *given.\n')
            return FE_Element.errVector

    def getK_Force(self, disp, fact=1.0):
        if self.myEle != None:
            self.theResidual.Zero()
            if fact == 0.0:
                return self.theResidual
            tmp = Vector(self.numDOF)
            for i in range(0, self.numDOF):
                dof = self.myID[i]
                if dof >= 0:
                    tmp[i] = disp[dof]
                else:
                    tmp[i] = 0.0
            if self.theResidual.addMatrixVector(1.0, self.myEle.getTangentStiff(), tmp, fact) < 0:
                print('WARNING FE_Element::getKForce() - addMatrixVector returned error.\n')
            return self.theResidual
        else:
            print('WARNING FE_Element::getKForce() - no Element *given.\n')
            return FE_Element.errVector

    def getKi_Force(self, disp, fact=1.0):
        if self.myEle != None:
            self.theResidual.Zero()
            if fact == 0.0:
                return self.theResidual
            tmp = Vector(self.numDOF)
            for i in range(0, self.numDOF):
                dof = self.myID[i]
                if dof >= 0:
                    tmp[i] = disp[dof]
                else:
                    tmp[i] = 0.0
            if self.theResidual.addMatrixVector(1.0, self.myEle.getInitialStiff(), tmp, fact) < 0:
                print('WARNING FE_Element::getKForce() - addMatrixVector returned error.\n')
            return self.theResidual
        else:
            print('WARNING FE_Element::getKForce() - no Element *given.\n')
            return FE_Element.errVector



    def getC_Force(self, x, fact=1.0):
        pass
    def getM_Force(self, x, fact=1.0):
        pass

    def addM_Force(self, accel, fact=1.0):
        pass
    def addD_Force(self, vel, fact=1.0):
        pass

    def addK_Force(self, disp, fact=1.0):
        if self.myEle != None:
            if fact == 0.0:
                return
            tmp = Vector(self.numDOF)
            for i in range(0, self.numDOF):
                loc = self.myID[i]
                if loc >= 0:
                    tmp[i] = disp[loc]
                else:
                    tmp[i] = 0.0
            if self.theResidual.addMatrixVector(1.0, self.myEle.getTangentStiff(), tmp, fact) < 0:
                print('WARNING FE_Element::addK_Force() - addMatrixVector returned error.\n')
        else:
            print('WARNING FE_Element::addK_Force() - no Element *given.\n')

    def addKg_Force(self, disp, fact=1.0):
        if self.myEle != None:
            if fact == 0.0:
                return
            tmp = Vector(self.numDOF)
            for i in range(0, self.numDOF):
                loc = self.myID[i]
                if loc >= 0:
                    tmp[i] = disp[loc]
                else:
                    tmp[i] = 0.0
            if self.theResidual.addMatrixVector(1.0, self.myEle.getGeometricTangentStiff(), tmp, fact) < 0:
                print('WARNING FE_Element::addKg_Force() - addMatrixVector returned error.\n')
        else:
            print('WARNING FE_Element::addKg_Force() - no Element *given.\n')
    
    def updateElement(self):
        if self.myEle!=None:
            return self.myEle.update()
        # else: =None 不用 print 吗？
        return 0

    def getLastIntegrator(self):
        return self.theIntegrator

    def getLastResponse(self):
        if self.myEle!=None:
            if self.theIntegrator!=None:
                if self.theIntegrator.getLastResponse(self.theResidual, self.myID) < 0:
                    print('WARNING FE_Element::getLastResponse(void) - the Integrator had problems with getLastResponse().\n')
            else:
                self.theResidual.Zero()
                print('WARNING  FE_Element::getLastResponse() - No Integrator yet passed.\n')
            return self.theResidual
        else:
            print('WARNING  FE_Element::getLastResponse() - No Element passed in constructor.\n')
            return FE_Element.errVector

    def getElement(self):
        return self.myEle
    
    # protected:
    def addLocalM_Force(self, accel, fact=1.0):
        pass
    def addLocalD_Force(self, vel, fact=1.0):
        pass
        

    