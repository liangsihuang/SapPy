from actor.MovableObject import MovableObject

# DOF_Numberer: responsible for
# 1. assigning equation numbers to the dof in each DOF_Group object.
# 2. getting the FE_Element objects to determine the mapping of their local dof to the equation numbers.

class DOF_Numberer(MovableObject):
    NUMBERER_TAG_DOF_Numberer = 1
    def __init__(self, aGraphNumberer):
        super().__init__(self.NUMBERER_TAG_DOF_Numberer)
        self._theGraphNumberer = aGraphNumberer
        self._theAnalysisModel = None


    def setLinks(self, theModel):
        self._theAnalysisModel = theModel
    
    
    
    def numberDOF(self, lastDOF_Group): # 有重载怎么办？？？
        
        # check we have a model and a numberer
        theDomain = None
        if(self._theAnalysisModel!=None):
            theDomain = self._theAnalysisModel.getDomain()
        if((self._theAnalysisModel==None) or(theDomain==None)):
            print('WAERNING DOF_Numberer::numberDOF - Pointers are not set.\n')
            return -1
        if(self._theGraphNumberer==None):
            print('WARNING DOF_Numberer::numberDOF - subclasses must provide own implementation\n')
            return -2
        # check we cant do quick return
        if(self._theAnalysisModel.getNumDOF_Groups()==None):
            return 0
    
    def getAnalysisModel(self):
        return self._theAnalysisModel
    
    def getGraphNumberer(self):
        return self._theGraphNumberer
    
