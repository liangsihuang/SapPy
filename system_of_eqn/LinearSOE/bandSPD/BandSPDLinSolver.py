from system_of_eqn.LinearSOE.LinearSOESolver import LinearSOESolver

class BandSPDLinSolver(LinearSOESolver):

    def __init__(self,clasTag):
        super().__init__(clasTag)
        self._theSOE = None
    
    def solve(self):
        pass # pure virtual
    
    def setLinearSOE(self, theBandSPDSOE):
        self._theSOE = theBandSPDSOE
        