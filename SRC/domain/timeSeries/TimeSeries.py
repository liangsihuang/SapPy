from SRC.tagged.TaggedObject import TaggedObject
from actor.MovableObject import MovableObject

class TimeSeries(TaggedObject, MovableObject):

    def __init__(self, tag, classTag):
        TaggedObject.__init__(self, tag)
        MovableObject.__init__(self, classTag)

    def addNode(self, Node):
        pass