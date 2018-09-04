from SRC.tagged.TaggedObject import TaggedObject

class MapOfTaggedObjects(TaggedObject):

    def __init__(self):
        self.theMap = {}

    def getComponent(self, tag):
        return self.theMap.get(tag, d=None)

    def addComponent(self, newComponent):
        tag = newComponent.getTag()
        # check if the ele already in map, if not we add
        if self.theMap.__contains__(tag) == False:
            self.theMap[tag] = newComponent
            # check if sucessfully added
            if self.theMap.__contains__(tag) == False:
                print('MapOfTaggedObjects::addComponent - dict(python) failed to add object with tag :'+str(newComponent.getTag())+'.\n')
                return False
            return True
        else:
            print('MapOfTaggedObjects::addComponent - not adding as one with similar tag exists, tag:'+str(newComponent.getTag())+'.\n')
            return False
    
    def removeComponent(self, tag):
        # return 0 if component does not exist, otherwise remove it
        theEle = self.theMap.get(tag, d=None)
        if theEle == None:
            return 0
        else:
            removed = self.theMap.pop(tag)
            return removed
        
    
    

         
        
            

        
            



    
