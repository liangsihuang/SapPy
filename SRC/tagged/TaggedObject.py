# 继承自：无
class TaggedObject(object):
    def __init__(self, tag):
        self._theTag = tag 
# tag 是 int
    def getTag(self):
        return self._theTag
