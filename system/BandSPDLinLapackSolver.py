from system.BandSPDLinSolver import BandSPDLinSolver

class BandSPDLinLapackSolver(BandSPDLinSolver):
    SOLVER_TAGS_BandSPDLinLapackSolver = 3

    def __init__(self):
        super().__init__(self.SOLVER_TAGS_BandSPDLinLapackSolver)
        