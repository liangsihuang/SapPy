from analysis.handler.ConstraintHandler import ConstraintHandler

class PenaltyConstraintHandler(ConstraintHandler):
    HANDLER_TAG_PenaltyConstraintHandler = 3
    def __init__(self, sp, mp):
        ConstraintHandler.__init__(self, self.HANDLER_TAG_PenaltyConstraintHandler)
        self._alphaSP = sp
        self._alphaMP = mp

    def setTimeSeries(self, theSeries):
        pass