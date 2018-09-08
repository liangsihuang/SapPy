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

    def number(self, theGraph, lastVertex=-1): # 有重载
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
        


