from SRC.system_of_eqn.LinearSOE.LinearSOESolver import LinearSOESolver

class BandSPDLinSolver(LinearSOESolver):

    def __init__(self,clasTag):
        super().__init__(clasTag)
        self.theSOE = None
    
    def setLinearSOE(self, theBandSPDSOE):
        self.theSOE = theBandSPDSOE
        