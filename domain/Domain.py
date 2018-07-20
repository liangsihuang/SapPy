from tagged.MapOfTaggedObject import MapOfTaggedObject

class Domain(object):
    def __init__(self):
        self._theElements = MapOfTaggedObject()
        self._theNodes    = MapOfTaggedObject()
        self._theSPs      = MapOfTaggedObject()
        self._thePCs      = MapOfTaggedObject()
        self._theMPs      = MapOfTaggedObject()
        self._theLoadPatterns = MapOfTaggedObject()
        self._theParameters   = MapOfTaggedObject()

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



        
    
    def addSP_Constraint(self, SP_Constraint):
        pass
    
    def addLoadPattern(self, LoadPattern):
        pass
# methods to add components to a LoadPattern object
    def addNodalLoad(self, NodalLoad, loadPatternTag):
        pass

