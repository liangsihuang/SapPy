from system_of_eqn.LinearSOE.bandSPD.BandSPDLinSolver import BandSPDLinSolver

class BandSPDLinLapackSolver(BandSPDLinSolver):
    SOLVER_TAGS_BandSPDLinLapackSolver = 3

    def __init__(self):
        super().__init__(self.SOLVER_TAGS_BandSPDLinLapackSolver)
    
    def solve(self):
        if(self._theSOE==None):
            print('WARNING BandSPDLinLapackSolver::solve() - No LinearSOE object has been set. \n')
            return -1
        
        n = self._theSOE._size()
        kd = self._theSOE._half_band - 1
        
        
        
    def setSize(self):
        pass
        n = self._theSOE._size
        kd = self._half_band - 1
        ldA = kd + 1
        nrhs = 1
        ldB = n 
        A = self._theSOE._A
        X = self._theSOE._X
        B = self._theSOE._B

        # first copy B into X
        for i in range(0, n):
            