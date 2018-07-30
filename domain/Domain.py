from tagged.MapOfTaggedObjects import MapOfTaggedObjects

class Domain(object):
    def __init__(self):
        self._theElements = MapOfTaggedObjects()
        self._theNodes    = MapOfTaggedObjects()
        self._theSPs      = MapOfTaggedObjects()
        self._theMPs      = MapOfTaggedObjects()
        self._thePCs      = MapOfTaggedObjects()
        self._theLoadPatterns = MapOfTaggedObjects()
        self._theParameters   = MapOfTaggedObjects()    

        self._currentTime = 0.0     # current pseudo time
        self._committedTime = 0.0   # the committed pseudo time
        self._dT = 0.0              # difference between committed and current time

        self._currentGeoTag = 0                 # an integer used mark if domain has changed
        self._hasDomainChangedFlag = False      # a bool flag used to indicate if GeoTag needs to be ++
        self._lastGeoSendTag = -1               # the value of currentGeoTag when sendSelf was last invoked

        self._nodeGraphBuiltFlag = False 
        self._eleGraphBuiltFlag = False

    # methods to populate a domain (add components to a domain)
    def addNode(self, node):
        nodTag = node.getTag()
        # 先要看看 theNodes 里面有没有已经存在 node，输入 node 的节点号 nodTag
        if(self._theNodes.hasComponent(nodTag)):
            print('node with tag '+str(nodTag)+' already exist in domain./n' )
        else:
            self._theNodes.addComponent(node)
            node.setDomain(self)

        # 还要： see if the physical bounds are changed
    
    def addElement(self, element):
        eleTag = element.getTag()
        # check all the element nodes exists in the domain
        nodes = element.getExternalNodes()
        for i in ragne(0,nodes.len()):
            if(self._theNodes.hasComponent(nodes[i]):
                pass
            else:
                print('WARNING Domain::addElement - In element '+str(eleTag))
                print('\n no Node '+str(nodes[i])+' exists in the domain.\n')
        # check if an Element with a similar tag already exists in the Domain
        if(self._theElements.hasComponent(eleTag)):
            print('element with tag '+str(eleTag)+' already exist in domain./n')
        else:
            self._theElements.addComponent(element)
            element.setDomain(self)
        
        # 还要：
        # finally check the ele has correct number of dof
        # mark the Domain as having been changed
    
    def addSP_Constraint(self, spConstraint):
        nodeTag = spConstraint.getNodeTag()
        dof = spConstraint.getDOF_Number()
        # check node exists in the domain
        if(self._theNodes.hasComponent(nodeTag)):
            pass
        else:
            print('Domain::addSP_Constraint - cannot add as node with tag ')
            print(str(nodeTag)+' dose not exist in the domain.\n')
        # check that the DOF specified exists at the Node
        node = self.getNode(nodeTag)
        numDOF = node.getTag()
        if(numDOF<dof):
            print('Domain::addSP_Constraint - cannnot add as node with tag ')
            print(str(nodeTag)+' does not have associated constrainted DOF\n')
        # check if an exsiting SP_Constraint exists for that dof at the node
        found = False
        # theExistingSPs = self.getSPs()
        # for k, v in theExistingSPs.items():
        for k, v in self._theSPs.items():
            spNodeTag = v.getNodeTag()
            spDof = v.getDOF_Number()
            if(nodeTag == spNodeTag & dof == spDof):
                found = True
        if(found == True):
            print('Domain::addSP_Constraint - cannot add as node already constrained in that dof by existing SP_Constraint.\n')
        # check that no other object with similar tag exists in model
        tag = spConstraint.getTag()
        if(self._theSPs.hasComponent(tag)):
            print('Domain::addSP_Constraint - cannot add as constraint with tag ')
            print(str(tag)+' already exists in the domain.\n')
        else:
            self._theSPs.addComponent(spConstraint)
            spConstraint.setDomain(self)

    def addPressure_Constraint(self):
        pass

    def addMP_Constraint(self):
        pass
        

    def addLoadPattern(self, LoadPattern):
        pass

    # methods to add components to a LoadPattern object
    def addNodalLoad(self, load, pattern):
        nodTag = load.getNodeTag()
        res = self.getNode(nodTag)
        if(res==0):
            print('Domain::addNodalLoad() - no node with tag '+str(nodTag)+' exists in the model.\n')
            print('Not adding the nodal load.')
        # now add it to the pattern
        thePattern = self._theLoadPatterns.getComponent(pattern)
        if(thePattern == 0):
            print('Domain::addNodalLoad() - no pattern with tag '+str(pattern)+' exists in the model.\n')
            print('Not adding the nodal load.')
        thePattern.addNodalLoad(load)
        load.setDomain(self)

    def addElementalLoad(self):
        pass

    def addSP_Constraint(self):
        pass
    # methods to remove the components
    def clearAll(self):
        pass
    def removeElement(self, tag):
        pass
    def removeNode(self, tag):
        pass
    def removeSP_Constraint(self, tag):
        pass
    def removePressure_Constraint(self, tag):
        pass
    def removeMP_Constraint(self, tag):
        pass

    def removeLoadPattern(self, tag):
        pass
    def removeNodalLoad(self, loadPattern):
        pass
    def removeElementLoad(self, loadPattern):
        pass
    # def removeSP_Constraint(self, loadPattern):

    # methods to access the components of a domain
    def getElements(self):
        return self._theElements
    def getNodes(self):
        return self._theNodes
    def getPCs(self):
        return self._thePCs
    def getMPs(self):
        return self._theMPs
    def getSPs(self):
        return self._theSPs
    def getLoadPatterns(self):
        return self._theLoadPatterns
    def getDomainAndLoadPatternSPs():
        pass
    # def getParameters():
    #     pass
    def getElement(self, tag):
        pass
    def getNode(self, tag):
        return self._theNodes.get(tag, defalut=0)
    def getSP_Constraint(self, tag):
        pass
    def getPressure_Constraint(self, tag):
        pass
    def getMP_Constraint(self, tag):
        pass
    def getLoadPattern(self, tag):
        pass

    # methods to query the state of the domain
    def getCurrentTime(self):
        return self._currentTime
    def getCommitTag(self):
        pass
    def getNumElements(self):
        pass
    def getNumNodes(self):
        pass
    def getNumSPs(self):
        pass
    def getNumPCs(self):
        pass
    def getNumMPs(self):
        pass
    def getNumLoadPatterns(self):
        pass
    
    def getPysicalBounds(self):
        pass
        # vector
    def getNodeResponse(self, nodeTag):
        pass
        # vector
    def getElementResponse(self, eleTag):
        pass
        # vector
    

    # methods to get element and node graph
    def getElmentGraph(self):
        pass
    def getNodeGraph(self):
        pass
    def clearElementGraph(self):
        pass
    def clearNodeGraph(self):
        pass
    
    # methods to update the domain
    def setCommitTag(self, newTag):
        pass
    def setCurrentTime(self, newTime):
        pass
    def setCommittedTime(self, newTime):
        pass
    def applyLoad(self, timeStep):
        # set the pseudo time in the domai to be newTime
        self._currentTime = timeStep
        self._dT = self._currentTime - self._committedTime
        # first loop over nodes and elements getting them to first zero their loads
        for tag, node in self._theNodes:
            node.zeroUnbalancedLoad()
        for tag, ele in self._theElements:
            if(ele.isSubdomain()==False):
                ele.zeroLoad()
        # now loop over load patterns, invoking applyLoad on them
        for tag, loadPat in self._theLoadPatterns:
            loadPat.applyLoad(timeStep)
        # finally loop over the MP_Constraints and SP_Constraints of the domain
        # for tag, theMP in self._theMPs:
            # theMP.applyConstraint(timeStep)
        for tag, theSP in self._theSPs:
            theSP.applyConstraint(timeStep)
    
    def setLoadConstant(self):
        pass
    def unsetLoadConstant(self):
        pass
    def initialize(self):
        pass
    def setRayleighDampingFactors(self, alphaM, betaK, betaK0, betaKc):
        pass
    
    def commit(self):
        pass
    def revertToLastCommit(self):
        # first invoke revertToLastCommit on all nodes and elements in the domain
        for tag, node in self._theNodes:
            node.revertToLastCommit()
        for tag, ele in self._theElements:
            ele.revertToLastCommit()
        # set the current time and load factor in the domain to last commited
    def revertToStart(self):
        pass
    def update(self):
        pass
    

    def analysisStep(self, dT):
        return 0
    def eigenAnalysis(self, numMode, generalized, findSmallest):
        pass
        
    # methods for eigenvalue analysis
    # methods for other objects to determine if model has changed
    def hasDomainChanged(self):
        # if the flag, indicating the domain has changed since the last call to this method, has changed
        # increment the integer and reset the flag
        result = self._hasDomainChangedFlag
        self._hasDomainChangedFlag = False
        if(result==True):
            self._currentGeoTag = self._currentGeoTag + 1
            self._nodeGraphBuiltFlag = False
            self._eleGraphBuiltFlag = False
        return self._currentGeoTag
    def getDomainChangeFlag(self):
        pass
    def domainChange(self):
        pass
    def setDomainChangeStamp(self):
        pass
        
    # methods for output
    # nodal methods required in domain interface for parallel interpreter


    



      
