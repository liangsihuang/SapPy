from actor.MovableObject import MovableObject

class Integrator(MovableObject):
    def __init__(self, clasTag):
        MovableObject.__init__(self, clasTag)
        

    def setTimeSeries(self, theSeries):
        pass