from actor.MovableObject import MovableObject
# 这是个纯虚类，啥都没有
class LinearSOESolver(MovableObject):
    def __init__(self, clasTag):
        super().__init__(clasTag)
