from analysis.algorithm.EquiSolnAlgo import EquiSolnAlgo

class Linear(EquiSolnAlgo):
    EquiALGORITHM_TAGS_Linear = 1

    def __init__(self, theTangent=CURRENT_TANGENT, Fact = 0):
        EquiSolnAlgo.__init__(self.EquiALGORITHM_TAGS_Linear)

    def setTimeSeries(self, theSeries):
        pass