from tagged.TaggedObject import TaggedObject
from actor.MovableObject import MovableObject

class Material(TaggedObject, MovableObject):
    
    def __init__(self, tag, clasTag):
        TaggedObject.__init__(self, tag)
        MovableObject.__init__(self, clasTag)
    
    