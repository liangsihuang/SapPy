from SRC.tagged.TaggedObject import TaggedObject

class MapOfTaggedObjects(TaggedObject):

    def __init__(self):
        self.theMap = {}
    
    def hasComponent(self, tag):
        return self.theMap.__contains__(tag)

    def getComponent(self, tag):
        return self.theMap.get(tag, 0)

    def addComponent(self, newComponent):
        tag = newComponent.getTag()
        # check if the ele already in map, if not we add
        if(self.hasComponent(tag)==False):
            self.theMap[tag] = newComponent
        self.theMap[tag] = newComponent


    
