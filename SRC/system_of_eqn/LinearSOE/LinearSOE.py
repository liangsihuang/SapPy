from SRC.actor.MovableObject import MovableObject

# LinearSOE:
# storing linear system of equations of form Ax = b
# abstract base class, subclasses are:
# BandSPDLinearSOE
# SparseSPDLinearSOE
# BandGeneralLinearSOE
# EleByEleLinearSOE
# subclass do not actually store the components of the system, for example the A matrix

class LinearSOE(MovableObject):

    def __init__(self, clasTag, theLinearSOESolver=None):
        
        super().__init__(clasTag)
        self._theAnalysisModel = None
        self._theSolver = theLinearSOESolver

    def solve(self):
        if(self._theSolver!=0):
            return self._theSolver.solve()
        else:
            return -1
    
    def setLinks(self, theModel):
        self._theAnalysisModel = theModel
    
    def setSize(self, theGraph):
        pass # 纯虚
    def getNumEqn(self):
        pass # 纯虚
    def addA(self, matrix, id, fact=1.0):
        pass # 纯虚
    def addB(self, vector, id, fact=1.0):
        pass # 纯虚
    def setB(self, vector, fact=1.0):
        pass # 纯虚
    
    # def addA(self, matrix) 有重载
    def addColA(self, col, colIndex, fact=1.0):
        pass # 纯虚
    def zeroA(self):
        pass # 纯虚
    def zeroB(self):
        pass # 纯虚
    
    def formAp(self, p, Ap):
        pass # 纯虚
    
    def getX(self):
        pass # 纯虚
    def getB(self):
        pass # 纯虚
    def getA(self):
        pass # 纯虚
    def getDeterminant(self):
        pass # 纯虚
    def normRHS(self):
        pass # 纯虚
    
    def setX(self, loc, value):
        pass # 纯虚
    # def setX(self, X) 有重载

    def getSolver(self):
        return self._theSolver
    

    
    

    


