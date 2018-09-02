from SRC.actor.MovableObject import MovableObject
from SRC.tagged.storage.ArrayOfTaggedObjects import ArrayOfTaggedObjects

# AnalysisModel: hold and provide access to the FE_Element and DOF_Group objects
class AnalysisModel(MovableObject):
    AnaMODEL_TAGS_AnalysisModel = 1
    def __init__(self):
        MovableObject.__init__(self, self.AnaMODEL_TAGS_AnalysisModel)

        self.theFEs = ArrayOfTaggedObjects(256)
        self.theDOFs = ArrayOfTaggedObjects(256)
        
        self.myDomain = None
        self.myHandler = None

        self.myDOFGraph = None
        self.myGroupGraph = None

        self.numFE_Ele = 0         # number of FE_Elements objects added
        self.numDOF_Grp = 0        # number of DOF_Group objects added
        self.numEqn = 0            # numEqn set by the ConstraintHandler typically

    # methods to populate/depopulate the AnalysisModel
    def addFE_Element(self, theFE_Ele):
        # check we don't add a null pointer or this is a subclass trying to use this method when it should'nt
        if theFE_Ele == None or self.getFEs == None:
            return False
        # check if an Element with a similar tag already exists in the Domain
        tag = theFE_Ele.getTag()
        other = self.theFEs.getComponent(tag)
        if other!=None:
            print('AnalysisModel::addFE_Element - fe_element with tag '+str(tag)+' already exists in model.\n')
            return False
        # add 
        result = self.theFEs.addComponent(theFE_Ele)
        if result == True:
            theFE_Ele.setAnalysisModel(self)
            self.numFE_Ele += 1
            return True
        else:
            return False

    def addDOF_Group(self, theDOF_Grp):
        # check we don't add a null pointer or this is a subclass trying to use a method it should'nt be using
        if theDOF_Grp == None or self.theDOFs == None:
            return False
        
        # check if a DOF_Group with a similar tag already exists in the Model
        tag = theDOF_Grp.getTag()
        other = self.theDOFs.getComponent(tag)
        if other!=None:
            print('AnalysisModel::addDOF_Group - dof_group with tag '+str(tag)+' already exists in model.\n')
            return False
        
        # add
        result = self.theDOFs.addComponent(theDOF_Grp)
        if result == True:
            self.numDOF_Grp += 1
            return True
        else:
            return False

    def clearAll(self):
        # if the graphs have been constructed, delete them
        if(self.myDOFGraph!=None):
            self.myDOFGraph = None

        if(self.myGroupGraph!=None):
            self.myGroupGraph = None
    
    def clearDOFGraph(self):
        pass
    def clearDOFGroupGraph(self):
        pass
    # methods to access the FE_Elements and DOF_Groups and their numbers
    def getNumDOF_Groups(self):
        return self.numDOF_Grp
    def getDOF_GroupPtr(self, tag):
        pass

    def getFEs(self):
        pass
        
    def getDOFs(self):
        pass
    # methods to access the connectivity for SysOfEqn to size itself
    def setNumEqn(self, theNumEqn):
        pass
    def getNumEqn(self):
        pass
    def getDOFGraph(self):
        pass
    def getDOFGroupGraph(self):
        pass
    
    # methods to update the response quantities at the DOF_Groups,
    # which in turn set the new nodal trial response quantities
    def setResponse(self, disp, vel, accel):
        pass
    def setDisp(self, disp):
        pass
    def setVel(self, vel):
        pass
    def setAccel(self, accel):
        pass

    def incrDisp(self, disp):
        pass
    def incrVel(self, vel):
        pass
    def incrAccel(self, accel):
        pass
    
    # methods added to store the eigenvalues and vectors in the domain
    def setNumEigenvectors(self, numEigenvectors):
        pass
    def setEigenvector(self, mode, eigenvalue):
        pass
    def setEigenvalues(self, eigenvalue):
        pass
    def getEigenvalues(self):
        pass
    def getModelDampingFactors(self):
        pass
    def inclModalDampingMatrix(self):
        pass
    
    # methods which trigger operations in the Domain
    def setLinks(self, theDomain, theHandler):
        pass

    def applyLoadDomain(self, pseudoTime):
        # check to see there is a Domain linked to the Model
        if self.myDomain == None:
            print('WARNING: AnalysisModel::applyLoadDomain - No Domain linked.\n')
            return None
        
        self.myDomain.applyLoad(pseudoTime)
        self.myHandler.applyLoad()

    def updateDomain(self):
        pass
    # def updateDomain(self, newTime, dT):
    #     pass
    def analysisStep(self, dT=0.0):
        # check to see there is a Domain linked to the Model
        if(self.myDomain==None):
            print('WARNING: AnalysisModel::newStep. No domain linked.\n')
        # invoke the method
        return self.myDomain.analysisStep(dT)

    def eigenAnalysis(self, numMode, generalized, findSmallest):
        pass
    def commitDomain(self):
        pass
    def revertDomainToLastCommit(self):
        pass

    def getCurrentDomainTime(self):
        # check to see there is a Domain linked to the Model
        if self.myDomain == None:
            print('WARNING: AnalysisModel::getCurrentDomainTime - No Domain linked.\n')
            return None
        return self.myDomain.getCurrentTime()

    def setCurrentDomainTime(self, newTime):
        pass
    def setRayleighDampingFactors(self, alphaM, betaK, betaKi, betaKc):
        pass
    def getDomain(self):
        return self._myDomain
    
    
    
    
        

        
