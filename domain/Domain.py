from tagged.MapOfTaggedObject import MapOfTaggedObject

class Domain(object):
    def __init__(self):
        self.theElements = MapOfTaggedObject()
        self.theNodes    = MapOfTaggedObject()
        self.theSPs      = MapOfTaggedObject()
        self.thePCs      = MapOfTaggedObject()
        self.theMPs      = MapOfTaggedObject()
        self.theLoadPatterns = MapOfTaggedObject()
        self.theParameters   = MapOfTaggedObject()

# methods to populate a domain
    def addNode(self, node):
        nodTag = node.getTag()
        # 先要看看 theNodes 里面有没有已经存在 node，输入 node 的节点号 nodTag
        if(theNodes.hasComponent(nodTag)):
            print('node with tag'+str(nodTag)+'already exist in domain./n' )
            else:
                theNodes.addCompenent(node)
    
    def addElement(self, Element):
        pass
    
    def addSP_Constraint(self, SP_Constraint):
        pass
    
    def addLoadPattern(self, LoadPattern):
        pass
# methods to add components to a LoadPattern object
    def addNodalLoad(self, NodalLoad, loadPatternTag):
        pass

