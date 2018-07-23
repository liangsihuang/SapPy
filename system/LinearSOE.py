from actor.MovableObject import MovableObject

class LinearSOE(MovableObject):

    def __init__(self, clasTag, theLinearSOESolver=None):
        super().__init__(clasTag)
        self._theSolver = theLinearSOESolver
