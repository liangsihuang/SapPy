from actor.MovableObject import MovableObject
from tagged.ArrayOfTaggedObjects import ArrayOfTaggedObjects

class AnalysisModel(MovableObject):
    AnaMODEL_TAGS_AnalysisModel = 1
    def __init__(self):
        MovableObject.__init__(self, self.AnaMODEL_TAGS_AnalysisModel)
        theFEs = ArrayOfTaggedObjects()
        theDOFs = ArrayOfTaggedObjects()

    def setTimeSeries(self, theSeries):
        pass