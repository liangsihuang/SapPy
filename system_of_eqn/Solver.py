from actor.MovableObject import MovableObject

class Solver(MovableObject):
    def __init__(self, theTag):
        super().__init__(theTag)

    def solve(self):
        pass # pure virtual
        