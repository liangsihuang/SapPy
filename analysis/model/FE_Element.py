from tagged.TaggedObject import TaggedObject
import numpy as np

class FE_Element(TaggedObject):
    def __init__(self, tag, ele):
        super().__init__(tag)

        # protected variables - a copy for each object of the class  
        self._myDOF_Groups = np.size(ele.getExternalNodes())
        self._myID = 