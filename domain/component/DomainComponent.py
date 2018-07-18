from tagged.TaggedObject import TaggedObject
from actor.MovableObject import MovableObject

class DomainComponent(TaggedObject, MovableObject):
    def __init__(self, tag, clasTag):
        # 父类
        self._theTag = tag
        self._classTag = clasTag


