from system.LinearSOESolver import LinearSOESolver
class BandSPDLinSolver(LinearSOESolver):
    def __init__(self,clasTag):
        super().__init__(clasTag)