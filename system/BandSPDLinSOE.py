from system.LinearSOE import LinearSOE
class BandSPDLinSOE(LinearSOE):
    LinSOE_TAGS_BandSPDLinSOE = 3
    def __init__(self, theSolver):
        super().__init__(self.LinSOE_TAGS_BandSPDLinSOE, theSolver)
        # theSolver 是 BandSPDLinSolver 类