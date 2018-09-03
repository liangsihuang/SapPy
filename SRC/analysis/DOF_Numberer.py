from SRC.actor.MovableObject import MovableObject

# DOF_Numberer: responsible for
# 1. assigning equation numbers to the dof in each DOF_Group object.
# 2. getting the FE_Element objects to determine the mapping of their local dof to the equation numbers.

class DOF_Numberer(MovableObject):
    NUMBERER_TAG_DOF_Numberer = 1
    def __init__(self, aGraphNumberer):
        super().__init__(self.NUMBERER_TAG_DOF_Numberer)
        self.theGraphNumberer = aGraphNumberer
        self.theAnalysisModel = None


    def setLinks(self, theModel):
        self.theAnalysisModel = theModel
    
    
    
    def numberDOF(self, lastDOF_Group): # 有重载怎么办？？？
        
        # check we have a model and a numberer
        theDomain = None
        if(self.theAnalysisModel!=None):
            theDomain = self.theAnalysisModel.getDomain()
        if((self.theAnalysisModel==None) or(theDomain==None)):
            print('WAERNING DOF_Numberer::numberDOF - Pointers are not set.\n')
            return -1
        if(self.theGraphNumberer==None):
            print('WARNING DOF_Numberer::numberDOF - subclasses must provide own implementation\n')
            return -2
        # check we cant do quick return
        if(self.theAnalysisModel.getNumDOF_Groups()==None):
            return 0
    
    def getAnalysisModel(self):
        return self.theAnalysisModel
    
    def getGraphNumberer(self):
        return self.theGraphNumberer
    
