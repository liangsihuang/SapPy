from SRC.tagged.TaggedObject import TaggedObject
from SRC.matrix.ID import ID

class Vertex(TaggedObject):
    def __init__(self, tag, ref, weight, color):
        super().__init__(tag)
        self.myRef = ref
        self.myWeight = weight
        self.myColor = color

        self.myDegree = 0  # ??
        self.myTmp = 0
        self.myAdjacency = ID(size=0, arraySize=8)

    # set method
    def setWeight(self, newWeight):
        self.myWeight = newWeight
    
    def setColor(self, newColor):
        self.myColor = newColor
    
    def setTmp(self, newTmp):
        self.myTmp = newTmp
    
    # get method
    def getRef(self):
        return self.myRef
    def getWeight(self):
        return self.myWeight
    def getColor(self):
        return self.myColor
    def getTmp(self):
        return self.myTmp
    def getDegree(self):
        return self.myDegree
    def getAdjacency(self):
        return self.myAdjacency
    
    # add method
    def addEdge(self, otherTag):
        # don't allow itself to be added
        if(otherTag==self.getTag()):
            return 0
        # check the otherVertex has not already been added??? 在 ID::insert 内部自动check
        return self.myAdjacency.insert(otherTag)






