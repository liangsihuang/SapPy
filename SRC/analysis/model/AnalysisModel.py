from SRC.actor.MovableObject import MovableObject
from SRC.tagged.storage.ArrayOfTaggedObjects import ArrayOfTaggedObjects
from SRC.tagged.storage.MapOfTaggedObjects import MapOfTaggedObjects
from SRC.graph.Graph import Graph
from SRC.graph.Vertex import Vertex

# AnalysisModel: hold and provide access to the FE_Element and DOF_Group objects
class AnalysisModel(MovableObject):
    AnaMODEL_TAGS_AnalysisModel = 1
    START_EQN_NUM = 0
    START_VERTEX_NUM = 0
    def __init__(self):
        MovableObject.__init__(self, self.AnaMODEL_TAGS_AnalysisModel)

        self.theFEs = ArrayOfTaggedObjects()
        self.theDOFs = ArrayOfTaggedObjects()
        
        self.myDomain = None
        self.myHandler = None

        self.myDOFGraph = None      # 两者有什么区别？？？？？？？？
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
        self.theFEs.clearAll()
        self.theDOFs.clearAll()

        self.myDOFGraph = None
        self.myGroupGraph = None

        self.numFE_Ele = 0
        self.numDOF_Grp = 0
        self.numeqn = 0
    
    def clearDOFGraph(self):
        self.myDOFGraph = None

    def clearDOFGroupGraph(self):
        self.myGroupGraph = None

    # methods to access the FE_Elements and DOF_Groups and their numbers
    def getNumDOF_Groups(self):
        return self.numDOF_Grp

    def getDOF_Group(self, tag):
        return self.theDOFs.getComponent(tag)

    def getFEs(self):
        return self.theFEs
        
    def getDOFs(self):
        return self.theDOFs
    # methods to access the connectivity for SysOfEqn to size itself
    def setNumEqn(self, theNumEqn):
        self.numEqn = theNumEqn

    def getNumEqn(self):
        self.numEqn

    def getDOFGraph(self):
        if self.myDOFGraph == None:
            numVertex = self.getNumDOF_Groups()
            graphStorage = MapOfTaggedObjects() 
            self.myDOFGraph = Graph(graphStorage)

            # create a vertex for each dof
            theDOFs = self.getDOFs().getComponents()
            for dof in theDOFs:
                id1= dof.getID()
                size = id1.Size()
                for i in range(0, size):
                    dofTag = id1[i]
                    if dofTag >= AnalysisModel.START_EQN_NUM:
                        vertex = self.myDOFGraph.getVertex(dofTag)
                        if vertex == None: 
                            vertex = Vertex(dofTag, dofTag) 
                            if self.myDOFGraph.addVertex(vertex, False) == False:
                                print('WARNING AnalysisModel::getDOFGraph - error adding vertex.\n')
                                return self.myDOFGraph
            # now add the edges, by looping over the FE_elements, getting their IDs and adding edges between DOFs for equation numbers >= START_EQN_NUM
            theFEs = self.getFEs().getComponents()
            cnt = 0
            for ele in theFEs:
                id1 = ele.getID()
                cnt += 1
                size = id1.Size()
                for i in range(0, size):
                    eqn1 = id1[i]
                    # if eqnNum of DOF is a valid eqn number add an edge to all other DOFs with valid eqn numbers.
                    if eqn1 >= AnalysisModel.START_EQN_NUM:
                        for j in range(i+1, size):
                            eqn2 = id1[j]
                            if eqn2 >= AnalysisModel.START_EQN_NUM:
                                self.myDOFGraph.addEdge(eqn1 - AnalysisModel.START_EQN_NUM + AnalysisModel.START_VERTEX_NUM, 
                                eqn2 - AnalysisModel.START_EQN_NUM + AnalysisModel.START_VERTEX_NUM)
        return self.myDOFGraph
 
    def getDOFGroupGraph(self): # 和 getDOFGraph() 有什么区别？
        if self.myGroupGraph == None:
            numVertex = self.getNumDOF_Groups()
            if numVertex == 0:
                print('WARNING AnalysisMode::getGroupGraph - 0 vertices, has the Domain been populated?\n')
                # exit(self, -1)
            graphStorage = MapOfTaggedObjects()
            self.myGroupGraph = Graph(graphStorage) # 重点！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！
            # now create the vertices with a reference equal to the DOF_Group number.
            # and a tag which ranges from 0 through numVertex-1
            theDOFs = self.getDOFs().getComponents()
            count = AnalysisModel.START_VERTEX_NUM
            for dof in theDOFs:
                DOF_GroupTag = dof.getTag()
                DOF_GroupNodeTag = dof.getNodeTag()
                numDOF = dof.getNumFreeDOF()
                vertex = Vertex(DOF_GroupTag, DOF_GroupNodeTag, 0, numDOF)
                self.myGroupGraph.addVertex(vertex)
            # now add the edges, by looping over the Elements, getting their
            # IDs and adding edges between DOFs for equation numbers >= START_EQN_NUM
            theFEs = self.getFEs.getComponents()
            for ele in theFEs:
                id1 = ele.getDOFtags()
                size = id1.Size()
                for i in range(0, size):
                    dof1 = id1[i]
                    for j in range(0, size):
                        if i != j:
                            dof2 = id1[j]
                            self.myGroupGraph.addEdge(dof1, dof2)
        return self.myGroupGraph
    
    # methods to update the response quantities at the DOF_Groups,
    # which in turn set the new nodal trial response quantities
    def setResponse(self, disp, vel, accel):
        # all is Vector
        theDOFGrps = self.getDOFs().getComponents()
        for dof in theDOFGrps:
            dof.setNodeDisp(disp)
            dof.setNodeVel(vel)
            dof.setNodeAccel(accel)

    def setDisp(self, disp):
        theDOFGrps = self.getDOFs().getComponents()
        for dof in theDOFGrps:
            dof.setNodeDisp(disp)

    def setVel(self, vel):
        theDOFGrps = self.getDOFs().getComponents()
        for dof in theDOFGrps:
            dof.setNodeVel(vel)

    def setAccel(self, accel):
        theDOFGrps = self.getDOFs().getComponents()
        for dof in theDOFGrps:
            dof.setNodeAccel(accel)

    def incrDisp(self, disp):
        # disp 是 Vector
        theDOFGrps = self.getDOFs().getComponents()
        for dof in theDOFGrps:
            dof.incrNodeDisp(disp)

    def incrVel(self, vel):
        theDOFGrps = self.getDOFs().getComponents()
        for dof in theDOFGrps:
            dof.incrNodeVel(vel)

    def incrAccel(self, accel):
        theDOFGrps = self.getDOFs().getComponents()
        for dof in theDOFGrps:
            dof.incrNodeAccel(accel)
    
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
        self.myDomain = theDomain
        self.myHandler = theHandler

    def applyLoadDomain(self, pseudoTime):
        # check to see there is a Domain linked to the Model
        if self.myDomain == None:
            print('WARNING: AnalysisModel::applyLoadDomain - No Domain linked.\n')
            return None
        
        self.myDomain.applyLoad(pseudoTime)
        self.myHandler.applyLoad()

    def updateDomain(self): # 有重载
        # check to see there is a Domain linked to the Model
        if self.myDomain == None:
            print('WARNING: AnalysisModel::updateDomain. No Domain linked.\n')
            return -1
        
        res = self.myDomain.update()
        if res == 0:
            return self.myHandler.update()
        return res

    # def updateDomain(self, newTime, dT):
    #     pass

    def analysisStep(self, dT=0.0):
        # check to see there is a Domain linked to the Model
        if self.myDomain is None:
            print('WARNING: AnalysisModel::newStep. No domain linked.\n')
            return -1
        # invoke the method
        return self.myDomain.analysisStep(dT)

    def eigenAnalysis(self, numMode, generalized, findSmallest):
        pass

    def commitDomain(self):
        # check to see there is a Domain linked to the Model
        if self.myDomain == 0:
            print('WARNING: AnalysisModel::commitDomain. No Domain linked.\n')
            return -1
        # invoke the method
        if self.myDomain.commit() < 0:
            print('WARNING: AnalysisModel::commitDomain - Domain::commit() failed.\n')
            return -2
        return 0

    def revertDomainToLastCommit(self):
        if self.myDomain == None:
            print('WARNING: AnalysisModel::revertDomainToLastCommit. No Domain linked.\n')
            return -1
        if self.myDomain.revertToLastCommit() < 0:
            print('WARNING: AnalysisModel::revertDomainToLastCommit. Domain::revertToLastCommit() failed.\n')
            return -2
        return 0

    def getCurrentDomainTime(self):
        # check to see there is a Domain linked to the Model
        if self.myDomain == None:
            print('WARNING: AnalysisModel::getCurrentDomainTime - No Domain linked.\n')
            return None
        return self.myDomain.getCurrentTime()

    def setCurrentDomainTime(self, newTime):
        if self.myDomain == None:
            print('WARNING: AnalysisModel::getCurrentDomainTime. No Domain linked.\n')
            return -1
        return self.myDomain.getCurrentTime()

    def setRayleighDampingFactors(self, alphaM, betaK, betaKi, betaKc):
        pass

    def getDomain(self):
        return self.myDomain
    
    
    
    
        

        
