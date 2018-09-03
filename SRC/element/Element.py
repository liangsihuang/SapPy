from SRC.domain.component.DomainComponent import DomainComponent

class Element(DomainComponent):

    def __init__(self, tag, classTag):
        super().__init__(tag, classTag)
        self.alphaM = 0.0
        self.betaK = 0.0
        self.betaK0 = 0.0
        self.betaKc = 0.0
        self.Kc = None         # pointer to hold last committed matrix if needed for rayleigh damping
        self.previousK = None
        self.numPreviousK = 0

        self.index = -1
        self.nodeIndex = -1

    
    # methods dealing with nodes and number of external dof
    def getNumExternalNodes(self):
        pass # 纯虚函数
    def getExternalNodes(self):
        pass # 纯虚函数
    def getNode(self):
        pass # 纯虚函数
    def getNumDOF(self):
        pass # 纯虚函数
    def getCharacteristicLength(self):
        pass
        
    # methods dealing with commited state and update
    def commitState(self):
        pass
    def revertToLastCommit(self):
        pass # 纯虚函数
    def revertToStart(self):
        pass
    def update(self):
        pass
    def isSubdomain(self):
        return False # 有鬼用？（注意：虚函数）

    # methods to return the current linearized stiffness, damping and mass matrices
    def getTangentStiff(self):
        pass # 纯虚函数
    def getInitialStiff(self):
        pass # 纯虚函数
    def getDamp(self):
        pass
    def getMass(self):
        pass
    def getGeometricTangentStiff(self):
        pass

    # methods for applying loads
    def zeroLoad(self):
        pass # 空函数？有鬼用？（注意：虚函数）
    def addLoad(self, theLoad, loadFactor):
        pass
    # def addLoad(self, theLoad, loadFactors):
    def addInertiaLoadToUnbalance(self, accel):
        pass
    def setRayleighDampingFactors(self, alphaM, betaK, betaK0, betaKc):
        pass

    # methods for obtaining resisting force (force includes elemental loads)
    def getResistingForce(self):
        pass # 纯虚函数
    def getResistingForceIncInertia(self):
        pass

    # methods for obtaining information specific to an element
