from actor.MovableObject import MovableObject

class DOF_Numberer(MovableObject):
    NUMBERER_TAG_DOF_Numberer = 1
    def __init__(self, aGraphNumberer):
        super().__init__(self.NUMBERER_TAG_DOF_Numberer)
        self._theGraphNumberer = aGraphNumberer

    def setTimeSeries(self, theSeries):
        pass