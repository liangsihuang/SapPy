from graph.GraphNumberer import GraphNumberer

class RCM(GraphNumberer):
    GraphNUMBERER_TAG_RCM = 1
    def __init__(self, gps=False):
        super().__init__(self.GraphNUMBERER_TAG_RCM)
        self._GPS = gps # flag for gibbs-poole-stodlymer

    def setTimeSeries(self, theSeries):
        pass