from tagged.TaggedObject import TaggedObject
from actor.MovableObject import MovableObject

class DomainComponent(TaggedObject, MovableObject):
    
    def __init__(self, tag, clasTag):
        TaggedObject.__init__(tag)
        MovableObject.__init__(clasTag)
        self._theDomain = None
    
    def setDomain(self, model):
        self._theDomain = model
    
    def getDomain(self):
        return self._theDomain




