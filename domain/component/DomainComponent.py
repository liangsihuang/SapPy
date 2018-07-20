from tagged.TaggedObject import TaggedObject
from actor.MovableObject import MovableObject

class DomainComponent(TaggedObject, MovableObject):
    
    def __init__(self, tag, clasTag):
        # _theTag 继承自 TaggedObject
        # _classTag 继承自 MovableObject
        self._theTag = tag
        self._classTag = clasTag
        self._theDomain = None
    
    def setDomain(self, model):
        self._theDomain = model



