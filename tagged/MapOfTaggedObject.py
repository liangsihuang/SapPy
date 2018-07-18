from tagged.TaggedObject import TaggedObject

class MapOfTaggedObject(TaggedObject):

    def __init__(self):
        self._theMap = {}
    
    def hasComponent(self, tag):
        return self._theMap.__contains__(tag)

    def getComponent(self, tag):
        return self._theMap[tag]

    def addComponent(self, newComponent):
        tag = newComponent.getTag()
        self._theMap[tag] = newComponent
    
    


    
