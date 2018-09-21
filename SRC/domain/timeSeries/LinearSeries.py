from SRC.domain.timeSeries.TimeSeries import TimeSeries

class LinearSeries(TimeSeries):
    TSERIES_TAG_LinearSeries = 1
    
    def __init__(self, tag=0, theFactor=1.0):
        TimeSeries.__init__(self, tag, self.TSERIES_TAG_LinearSeries)
        self._cFactor = theFactor # factor = pseudoTime * cFactor

    def addNode(self, Node):
        pass