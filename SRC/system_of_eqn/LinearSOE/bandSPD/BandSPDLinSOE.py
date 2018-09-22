from SRC.system_of_eqn.LinearSOE.LinearSOE import LinearSOE
import numpy as np
from SRC.matrix.Vector import Vector

# subclass of LinearSOE
# It uses the LAPACK Upper storage scheme to store the components of the A matrix
# 
#       *    *   a13  a24  a35  a46      
#       *   a12  a23  a34  a45  a56    
#      a11  a22  a33  a44  a55  a66 
# 行数 = half_band(包括对角线) ， 列数 = size(方程数 n)

class BandSPDLinSOE(LinearSOE):
    LinSOE_TAGS_BandSPDLinSOE = 3

    def __init__(self, theSolver):
        super().__init__(self.LinSOE_TAGS_BandSPDLinSOE, theSolver)
        # theSolver 是 BandSPDLinSolver 类
        self.size = 0
        self.half_band = 0
        # numpy array
        self.A = None # 以rank-2 array A来储存矩阵A
        self.B = None
        self.X = None
        # Vector
        self.vectX = None
        self.vectB = None

        self.Asize = 0  # 矩阵A的行数×列数
        self.Bsize = 0  # size 和 Bize 有什么区别？
        self.factored = False

    def getNumEqn(self):
        return self.size
    
    def setSize(self, theGraph):
        result = 0
        oldSize = self.size
        self.size = theGraph.getNumVertex() # 几何上的节点数 = 方程数
        # 求半带宽（包括对角线）
        self.half_band = 0
        theVertices = theGraph.getVertices()
        for tag, vertex in theVertices:
            vertexNum = vertex.getTag()
            theAdjacency = vertex.getAdjacency()
            for i in range(0, theAdjacency.Size()):
                otherNum = theAdjacency[i]
                diff = vertexNum - otherNum # 不用加绝对值吗？ 可能theAdjacency只储存了节点号比本身小的
                if(self.half_band < diff):
                    self.half_band = diff
        self.half_band += 1 # include the diagonal

        self.A = np.zeros((self.half_band,self.size), dtype=float) # rank-2 array
        self.Asize = self.half_band * self.size
        self.factored = False

        self.B = np.zeros(self.size, dtype=float)
        self.X = np.zeros(self.size, dtype=float)
        
        self.vectX = Vector(self.X, self.size)
        self.vectB = Vector(self.B, self.size)

        self.Bsize = self.size #???
        
        # invoke setSize() on the Solver
        theSolver = self.getSolver()
        solverOK = theSolver.setSize()
        if solverOK<0:
            print('WARNING: BandSPDLinSOE::setSize() - solver failed setSize().\n')
            return solverOK

        return result

    def addA(self, m, id1, fact = 1.0):
        # 刚度矩阵组装
        # m 是 Matrix 类，单元刚度矩阵
        # id1 是 ID 类 , id是保留字，所以用id1，一个单元里所有节点的自由度=方程数，方程数从0开始
        # check for a quick return
        if fact == 0.0:
            return 0
        # check that m and id are of similar size
        idSize = id1.Size()
        if idSize!=m.noRow() and idSize!=m.noCols() :
            print('BandSPDLinSOE::addA() - Matrix and ID not of similar sizes.\n')
            return -1

        for i in range(0, idSize):
            row = id1[i] 
            for j in range(0, idSize):
                col = id1[j]
                if row<=col:
                    self.A[self.half_band-1+row-col] += m[j,i]*fact

        return 0


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
    