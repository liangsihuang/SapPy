from SRC.tagged.TaggedObject import TaggedObject
from SRC.actor.MovableObject import MovableObject

class DomainComponent(TaggedObject, MovableObject):
    
    def __init__(self, tag, clasTag):
        TaggedObject.__init__(self, tag)
        MovableObject.__init__(self, clasTag)
        self.theDomain = None
    
    def setDomain(self, model):
        self.theDomain = model
    
    def getDomain(self):
        return self.theDomain




