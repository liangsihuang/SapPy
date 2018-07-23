from tagged.TaggedObject import TaggedObject

class MapOfTaggedObjects(TaggedObject):

    def __init__(self):
        self._theMap = {}
    
    def hasComponent(self, tag):
        return self._theMap.__contains__(tag)

    def getComponent(self, tag):
        return self._theMap.get(tag, 0)

    def addComponent(self, newComponent):
        tag = newComponent.getTag()
        # 一般时调用的时候check有没有重复，这里不用check了
        # check if the ele already in map, if not we add
        # if(self.hasComponent(tag)==False):
            # self._theMap[tag] = newComponent
        self._theMap[tag] = newComponent
        # check if 
    


    
