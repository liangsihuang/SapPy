from SRC.actor.MovableObject import MovableObject

# solve the system of equations stored in a LinearSOE object
# abstract base class

class LinearSOESolver(MovableObject):

    def __init__(self, clasTag):
        super().__init__(clasTag)
    
    def getDeterminant(self):
        pass
