from SRC.tagged.storage.MapOfTaggedObjects import MapOfTaggedObjects

class Graph(object):
    START_VERTEX_NUM = 0

    def __init__(self):
        self.myVertices = MapOfTaggedObjects()
        self.numEdge = 0
        self.nextFreeTag = Graph.START_VERTEX_NUM

    def addVertex(self, vertex, checkAdjacency):
        # check the vertex and its adjacency list
        # 略
        self.myVertices.addComponent(vertex)
        if vertex.getTag() >= self.nextFreeTag:
            self.nextFreeTag = self.nextFreeTag + 1
    
    def addEdge(self):
        pass
    
    def getVertex(self):
        pass
    
    def getVertexs(self):
        pass
    
    def getNumVertex(self):
        pass
    
    def getNumEdge(self):
        pass
    def getFreeTag(self):
        pass
    def removeVertex(self, tag, removeEdgeFlag = True):
        pass
    
    def merge(self, other):
        pass
    
    


    
