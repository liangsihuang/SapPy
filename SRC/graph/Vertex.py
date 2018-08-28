from tagged.TaggedObject import TaggedObject
from matrix.ID import ID

class Vertex(TaggedObject):
    def __init__(self, tag, ref, weight, color):
        super().__init__(tag)
        self._myRef = ref
        self._myWeight = weight
        self._myColor = color

        self._myDegree = 0  # ??
        self._myTmp = 0
        self._myAdjacency = ID(size=0, arraySize=8)

    # set method
    def setWeight(self, newWeight):
        self._myWeight = newWeight
    
    def setColor(self, newColor):
        self._myColor = newColor
    
    def setTmp(self, newTmp):
        self._myTmp = newTmp
    
    # get method
    def getRef(self):
        return self._myRef
    def getWeight(self):
        return self._myWeight
    def getColor(self):
        return self._myColor
    def getTmp(self):
        return self._myTmp
    def getDegree(self):
        return self._myDegree
    def getAdjacency(self):
        return self._myAdjacency
    
    # add method
    def addEdge(self, otherTag):
        # don't allow itself to be added
        if(otherTag==self.getTag()):
            return 0
        # check the otherVertex has not already been added??? 在 ID::insert 内部自动check
        return self._myAdjacency.insert(otherTag)






