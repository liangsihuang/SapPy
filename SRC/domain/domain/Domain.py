from SRC.tagged.MapOfTaggedObjects import MapOfTaggedObjects

class Domain(object):
    def __init__(self):
        self.theElements = MapOfTaggedObjects()
        self.theNodes    = MapOfTaggedObjects()
        self.theSPs      = MapOfTaggedObjects()
        self.theMPs      = MapOfTaggedObjects()
        self.thePCs      = MapOfTaggedObjects()
        self.theLoadPatterns = MapOfTaggedObjects()
        self.theParameters   = MapOfTaggedObjects()    

        self.currentTime = 0.0     # current pseudo time
        self.committedTime = 0.0   # the committed pseudo time
        self.dT = 0.0              # difference between committed and current time

        self.currentGeoTag = 0                 # an integer used mark if domain has changed
        self.hasDomainChangedFlag = False      # a bool flag used to indicate if GeoTag needs to be ++
        self.lastGeoSendTag = -1               # the value of currentGeoTag when sendSelf was last invoked

        self.nodeGraphBuiltFlag = False # 干啥的？
        self.eleGraphBuiltFlag = False

    # methods to populate a domain (add components to a domain)
    def addNode(self, node):
        nodTag = node.getTag()
        # 先要看看 theNodes 里面有没有已经存在 node，输入 node 的节点号 nodTag
        if(self.theNodes.hasComponent(nodTag)):
            print('node with tag '+str(nodTag)+' already exist in domain./n' )
        else:
            self.theNodes.addComponent(node)
            node.setDomain(self)

        # 还要： see if the physical bounds are changed
    
    def addElement(self, element):
        eleTag = element.getTag()
        # check all the element nodes exists in the domain
        nodes = element.getExternalNodes()
        for i in ragne(0,nodes.len()):
            if(self.theNodes.hasComponent(nodes[i]):
                pass
            else:
                print('WARNING Domain::addElement - In element '+str(eleTag))
                print('\n no Node '+str(nodes[i])+' exists in the domain.\n')
        # check if an Element with a similar tag already exists in the Domain
        if(self.theElements.hasComponent(eleTag)):
            print('element with tag '+str(eleTag)+' already exist in domain./n')
        else:
            self.theElements.addComponent(element)
            element.setDomain(self)
        
        # 还要：
        # finally check the ele has correct number of dof
        # mark the Domain as having been changed
    
    def addSP_Constraint(self, spConstraint):
        nodeTag = spConstraint.getNodeTag()
        dof = spConstraint.getDOF_Number()

        # check node exists in the domain
        if(self.theNodes.hasComponent(nodeTag)):
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
        for k, v in self.theSPs.items():
            spNodeTag = v.getNodeTag()
            spDof = v.getDOF_Number()
            if(nodeTag == spNodeTag & dof == spDof):
                found = True
        if(found == True):
            print('Domain::addSP_Constraint - cannot add as node already constrained in that dof by existing SP_Constraint.\n')
            
        # check that no other object with similar tag exists in model
        tag = spConstraint.getTag()
        if(self.theSPs.hasComponent(tag)):
            print('Domain::addSP_Constraint - cannot add as constraint with tag ')
            print(str(tag)+' already exists in the domain.\n')
        else:
            self.theSPs.addComponent(spConstraint)
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
        thePattern = self.theLoadPatterns.getComponent(pattern)
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
        return self.theElements
    def getNodes(self):
        return self.theNodes
    def getPCs(self):
        return self.thePCs
    def getMPs(self):
        return self.theMPs
    def getSPs(self):
        return self.theSPs
    def getLoadPatterns(self):
        return self.theLoadPatterns
    def getDomainAndLoadPatternSPs(self):
        allSPs = []
        allSPs.append(self.theSPs)
        for key, value in self.theLoadPatterns:
            allSPs.append(value)
        return allSPs
        # 怎么return loadPattern 里面的 theSPs ，loadPattern的个数并不确定，怎么办？ 返回一个 list
        

    # def getParameters():
    #     pass
    def getElement(self, tag):
        pass
    def getNode(self, tag):
        return self.theNodes.get(tag, defalut=0)
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
        return self.currentTime
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
        # set the pseudo time in the domain to be newTime
        self.currentTime = timeStep
        self.dT = self.currentTime - self.committedTime
        # first loop over nodes and elements getting them to first zero their loads
        for tag, node in self.theNodes:
            node.zeroUnbalancedLoad()
        for tag, ele in self.theElements:
            if(ele.isSubdomain()==False):
                ele.zeroLoad()
        # now loop over load patterns, invoking applyLoad on them
        for tag, loadPat in self.theLoadPatterns:
            loadPat.applyLoad(timeStep)
        # finally loop over the MP_Constraints and SP_Constraints of the domain
        # for tag, theMP in self._theMPs:
            # theMP.applyConstraint(timeStep)
        for tag, theSP in self.theSPs:
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
        for tag, node in self.theNodes:
            node.revertToLastCommit()
        for tag, ele in self.theElements:
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
        result = self.hasDomainChangedFlag
        if(result==True):
            self.currentGeoTag += 1
            self.nodeGraphBuiltFlag = False
            self.eleGraphBuiltFlag = False
        # 复位
        self.hasDomainChangedFlag = False
        # return the integer so user can determine if domain has changed since their last call to this method
        return self.currentGeoTag

    def getDomainChangeFlag(self):
        return self.hasDomainChangedFlag

    def domainChange(self):
        self.hasDomainChangedFlag = True

    def setDomainChangeStamp(self, newStamp):
        self.currentGeoTag = newStamp
        
    # methods for output
    # nodal methods required in domain interface for parallel interpreter


    



      
