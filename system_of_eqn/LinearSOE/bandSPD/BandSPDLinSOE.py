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

        # 看看size 有没有大于 Asize, Bsize
        if(self._half_band*self._size > self._Asize):
            pass
        
        # invoke setSize() on the Solver
        theSolver = self.getSolver()
        solverOK = theSolver.setSize()
        if solverOK<0:
            print('WARNING: BandSPDLinSOE::setSize() - solver failed setSize().\n')
            return solverOK

        return result

    def addA(self, m, the_id, fact = 1.0):
        # m 是 matrix
        # check for a quick return
        if fact == 0.0:
            return 0
        # check that m and id are of similar size
        idSize = the_id.Size()
        if idSize!=m.noRow() and idSize!=m.noCols() :
            print('BandSPDLinSOE::addA() - Matrix and ID not of similar sizes. \n')
            return -1
        if fact==1.0: # do not need to multiply
            for i in range(0, idSize):
                col = the_id[i]
                if (col<self._size) and (col>=0) :
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
    