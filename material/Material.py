from tagged.TaggedObject import TaggedObject
from actor.MovableObject import MovableObject

class Material(TaggedObject, MovableObject):
    
    def __init__(self, tag, clasTag):
        self._theTag = tag
        self._classTag = clasTag