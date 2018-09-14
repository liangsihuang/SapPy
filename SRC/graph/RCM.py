from SRC.graph.GraphNumberer import GraphNumberer
from SRC.matrix.ID import ID
# Reverse Cuthill-mcKenn numbering scheme
class RCM(GraphNumberer):
    GraphNUMBERER_TAG_RCM = 1
    def __init__(self, gps=False):
        super().__init__(self.GraphNUMBERER_TAG_RCM)
        self.numVertex = -1
        self.theRefResult = None # a ID pointer
        self.GPS = gps # flag for gibbs-poole-stodlymer

    def number(self, theGraph, startVertex=-1): # 有重载
        # first check our size, if not same make new
        if self.numVertex != theGraph.getNumVertex():
            # delete the old
            self.theRefResult = None
            self.numVertex = theGraph.getNumVertex()
            self.theRefResult = ID(self.numVertex)

        # see if we can do quick return
        if self.numVertex == 0:
            return self.theRefResult

        # we first set the Tmp of all vertices to -1, indicating they have not yet been added.
        vertexs = theGraph.getVertices().getComponents()
        for key, vertex in vertexs.items():
            vertex.setTmp(-1)
        
        # we now set up; setting our markers and getting first vertex
        startVertexTag = startVertex
        if startVertexTag != -1:
            vertex = theGraph.getVertex(startVertexTag)
            if vertex == None:
                print('WARNING:  RCM::number - No vertex with tag '+str(startVertexTag)+'Exists - using first come from iter.\n')
                startVertexTag = -1
        
        # if no starting vertex use the first one we get from the VertexIter
        vertexIter2 = iter(theGraph.getVertices().getComponents())
        if startVertexTag == -1:
            vertex = next(vertexIter2)
            start = vertex
            # if GPS true use gibbs-poole-stodlmyer determine the last level set 
            # assuming a starting vertex and then use one of the nodes in this set to base the numbering on	
            if self.GPS==True:
                currentMark = self.numVertex - 1    # marks current vertex visiting
                nextMark = currentMark - 1          # marks where to put next Tag
                startLastLevelSet = nextMark
                self.theRefResult[currentMark] = vertex.getTag()
                vertex.setTmp(currentMark)

                # we continue till the ID is full
                while nextMark >= 0:
                    # get the current vertex and its adjacency
                    vertex = theGraph.getVertex(self.theRefResult[currentMark])
                    adjacency = vertex.getAdjacency()

                    # go through the vertices adjacency and add vertices which have not yet been Tmp'ed to the (*theRefResult)
                    size = adjacency.Size()
                    for i in range(0, size):
                        vertexTag = adjacency[i]
                        vertex = theGraph.getVertex(vertexTag)
                        if vertex.getTmp() == -1:
                            vertex.setTmp(nextMark)
                            self.theRefResult[nextMark] = vertexTag
                            nextMark -= 1
                    # go to the next vertex
                    # we decrement because we are doing reverse Cuthill-McKee
                    currentMark -= 1
                    if startLastLevelSet == currentMark:
                        startLastLevelSet = nextMark
                    # check to see if graph is disconneted
                    if currentMark==nextMark and currentMark>=0:
                        # loop over iter till we get a vertex not yet Tmped
                        vertex = next(vertexIter2)
                        while vertex != None and vertex.getTmp() != -1:
                            nextMark -= 1
                            startLastLevelSet = nextMark
                            vertex.setTmp(currentMark)
                            self.theRefResult[currentMark] = vertex.getTag()

                # create an id of the last level set
                if startLastLevelSet > 0:
                    lastLeverSet = ID(startLastLevelSet)
                    for i in range(0, startLastLevelSet):
                        lastLeverSet[i] = self.theRefResult[i] 
                    return self.number(theGraph, lastLeverSet)  # 用到了重载的函数
            else:
                vertex = start

        vertexIter3 = theGraph.getVertices().getComponents()
        # set to -1 all the vertices 
        for key, other in vertexIter3:
            other.setTmp(-1)

        vertexIter4 = theGraph.getVertices().getComponents()

        currentMark = self.numVertex - 1    # marks current vertex visiting
        nextMark = currentMark - 1          # indiactes where to put next Tag in ID
        self.theRefResult[currentMark] = vertex.getTag()
        vertex.setTmp(currentMark)

        # we continue till the ID is full
        while nextMark >= 0:
            # get the current vertex and its adjacency
            vertex = theGraph.getVertex(self.theRefResult[currentMark])
            adjacency = vertex.getAdjacency()
            # go through the vertices adjacency and add vertices which have not yet been Tmp'ed to the (*theRefResult)
            size = adjacency.Size()
            for i in range(0, size):
                vertexTag = adjacency[i]
                vertex = theGraph.getVertex(vertexTag)
                if vertex.getTmp() == -1:
                    vertex.setTmp(nextMark)
                    self.theRefResult[nextMark] = vertexTag
                    nextMark -= 1
            # go to the next vertex, we decrement because we are doing reverse Cuthill-McKee
            currentMark -= 1
            # check to see if graph is disconneted
            if currentMark==nextMark and currentMark>=0:
                # 有一段不知所措
                nextMark -= 1
                vertex.setTmp(currentMark)
                self.theRefResult[currentMark] = vertex.getTag()
        
        # now set the vertex references instead of the vertex tags
        # in the result, we change the Tmp to indicate number and return
        for i in range(0, self.numVertex):
            vertexTag = self.theRefResult[i]
            vertex = theGraph.getVertex(vertexTag)
            vertex.setTmp(i+1)  # 1 through numVertex
            self.theRefResult[i] = vertex.getTag()
        
        return self.theRefResult





