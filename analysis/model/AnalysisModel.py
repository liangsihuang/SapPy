from actor.MovableObject import MovableObject
from tagged.ArrayOfTaggedObjects import ArrayOfTaggedObjects

# AnalysisModel: hold and provide access to the FE_Element and DOF_Group objects
class AnalysisModel(MovableObject):
    AnaMODEL_TAGS_AnalysisModel = 1
    def __init__(self):
        MovableObject.__init__(self, self.AnaMODEL_TAGS_AnalysisModel)

        self._theFEs = ArrayOfTaggedObjects(256)
        self._theDOFs = ArrayOfTaggedObjects(256)
        
        self._myDomain = None
        self._myHandler = None

        self._myDOFGraph = None
        self._myGroupGraph = None

        self._numFE_Ele = 0         # number of FE_Elements objects added
        self._numDOF_Grp = 0        # number of DOF_Group objects added
        self._numEqn = 0            # numEqn set by the ConstraintHandler typically

    # methods to populate/depopulate the AnalysisModel
    def addFE_Element(self, theFE_Ele):
        pass
    def addDOF_Group(self, theDOF_Grp):
        pass
    def clearAll(self):
        # if the graphs have been constructed, delete them
        if(self._myDOFGraph!=None):
            self._myDOFGraph = None

        if(self._myGroupGraph!=None):
            self._myGroupGraph = None
    
    def clearDOFGraph(self):
        pass
    def clearDOFGroupGraph(self):
        pass
    # methods to access the FE_Elements and DOF_Groups and their numbers
    def getNumDOF_Groups(self):
        return self._numDOF_Grp
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
    def applyLoadDomain(self, newTime):
        pass
    def updateDomain(self):
        pass
    # def updateDomain(self, newTime, dT):
    #     pass
    def analysisStep(self, dT=0.0):
        # check to see there is a Domain linked to the Model
        if(self._myDomain==None):
            print('WARNING: AnalysisModel::newStep. No domain linked.\n')
        return self._myDomain.analysisStep(dT)

    def eigenAnalysis(self, numMode, generalized, findSmallest):
        pass
    def commitDomain(self):
        pass
    def revertDomainToLastCommit(self):
        pass
    def getCurrentDomainTime(self):
        pass
    def setCurrentDomainTime(self, newTime):
        pass
    def setRayleighDampingFactors(self, alphaM, betaK, betaKi, betaKc):
        pass
    def getDomain(self):
        return self._myDomain
    
    
    
    
        

        
