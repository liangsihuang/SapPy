from SRC.actor.MovableObject import MovableObject

class SolutionAlgorithm(MovableObject):

    def __init__(self, clasTag):
        super().__init__(clasTag)
        self.theRecorders = None
        self.numRecorders = 0

    def domainChanged(self):
        return 0 # 有鬼用
    
    # methods for monitoring the analysis during an algorithm
    def addRecorder(self, theRecorder):
        pass
    
    def record(self, track):
        pass

    
    
