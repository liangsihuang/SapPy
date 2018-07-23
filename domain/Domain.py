from tagged.MapOfTaggedObjects import MapOfTaggedObjects

class Domain(object):
    def __init__(self):
        self._theElements = MapOfTaggedObjects()
        self._theNodes    = MapOfTaggedObjects()
        self._theSPs      = MapOfTaggedObjects()
        self._thePCs      = MapOfTaggedObjects()
        self._theMPs      = MapOfTaggedObjects()
        self._theLoadPatterns = MapOfTaggedObjects()
        self._theParameters   = MapOfTaggedObjects()

# methods to populate a domain
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


# methods to access the components of a domain
    def getNode(self, tag):
        return self._theNodes.get(tag, defalut=0)
    
    def getSPs(self):
        return self._theSPs

