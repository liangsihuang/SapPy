from actor.MovableObject import MovableObject
from tagged.ArrayOfTaggedObjects import ArrayOfTaggedObjects

class AnalysisModel(MovableObject):
    AnaMODEL_TAGS_AnalysisModel = 1
    def __init__(self):
        MovableObject.__init__(self, self.AnaMODEL_TAGS_AnalysisModel)
        self._theFEs = ArrayOfTaggedObjects()
        self._theDOFs = ArrayOfTaggedObjects()
        self._myDomain = None

    def analysisStep(self, dT):
        # check to see there is a Domain linked to the Model
        if(self._myDomain==None):
            print('WARNING: AnalysisModel::newStep. No domain linked.\n')
        return self._myDomain.analysisStep(dT)
    
    