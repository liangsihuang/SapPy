from system_of_eqn.LinearSOE.LinearSOE import LinearSOE

# subclass of LinearSOE
# It uses the LAPACK Upper storage scheme to store the components of the A matrix

class BandSPDLinSOE(LinearSOE):
    LinSOE_TAGS_BandSPDLinSOE = 3

    def __init__(self, theSolver):
        super().__init__(self.LinSOE_TAGS_BandSPDLinSOE, theSolver)
        # theSolver 是 BandSPDLinSolver 类
        self._size = 0
        self._half_band = 0
        # pointer array
        self._A = None
        self._B = None
        self._X = None
        # vector
        self._vectX = None
        self._vectB = None

        self._Asize = 0
        self._Bsize = 0
        self._factored = False

    def getNumEqn(self):
        return self._size
    
    def setSize(self, theGraph):
        result = 0
        oldSize = self._size
        self._size = theGraph.getNumVertex()
        self._half_band = 0
        theVertices = theGraph.getVertices()
        for tag, vertex in theVertices:
            vertexNum = vertex.getTag()
            theAdjacency = vertex.getAdjacency()
            for i in range(0, theAdjacency.Size()):
                otherNum = theAdjacency[i]
                diff = vertexNum - otherNum # 不用加绝对值吗？？
                if(self._half_band < diff):
                    self._half_band = diff
        self._half_band = self._half_band + 1 # include the diagonal

        if(self._half_band*self._size > self._Asize):
            pass
    
    def addA(self, matrix, id, fact = 1.0):
        pass
    def addColA(self, col, colIndex, fact = 1.0):
        pass
    
    def addB(self, vector, id, fact = 1.0):
        pass
    def setB(self, vector, fact = 1.0):
        pass
    
    def zeroA(self):
        pass
    def zeroB(self):
        pass
    
    def getX(self):
        pass
    def getB(self):
        pass
    def normRHS(self):
        pass
    
    def setX(self, loc, value):
        pass # 有重载
    
    def setBandSPDSolver(self, newSolver):
        pass
    