# 继承自：无
class TaggedObject(object):
    def __init__(self, tag):
        self.__theTag = tag 

    def getTag(self):
        return self.__theTag
