from actor.MovableObject import MovableObject

class SolutionAlgorithm(MovableObject):

    def __init__(self, clasTag):
        super().__init__(self, clasTag)
        self._theRecorders = None
        self._numRecorders = 0

    def domainChanged(self):
        return 0 # 有鬼用
    
    # methods for monitoring the analysis during an algorithm
    def addRecorder(self, theRecorder):
        pass
    
    def record(self, track):
        pass

    
    
