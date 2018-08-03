from actor.MovableObject import MovableObject

# SystemOfEqn: responsible for
# 1. storing the system of equations used in the analysis

class SystemOfEqn(MovableObject):

    def __init__(self, theTag):
        super().__init__(theTag)
    
    def solve(self):
        pass # 纯虚
    