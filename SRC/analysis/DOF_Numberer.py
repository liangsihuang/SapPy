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
    
    
    
    def numberDOF(self, lastDOF_Group): # 有重载怎么办？？？DOF_Numberer::numberDOF(ID &lastDOFs)
        
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
        
        # we first number the dofs using the dof group graph
        orderedRefs = self.theGraphNumberer.number(self.theAnalysisModel.getDOFGroupGraph(), lastDOF_Group)
        self.theAnalysisModel.clearDOFGroupGraph()

        # we now iterate through the DOFs first time setting -2 values
        eqnNumber = 0
        if orderedRefs.Size() != self.theAnalysisModel.getNumDOF_Groups():
            print('WARNING DOF_Numberer::numberDOF - Incompatable Sizes.\n')
            return -3
        result = 0
        size = orderedRefs.Size()
        for i in range(0, size):
            dofTag = orderedRefs[i]
            dof = self.theAnalysisModel.getDOF_Group(dofTag)
            if dof == None:
                print('WARNING DOF_Numberer::numberDOF - DOF_Group '+str(dofTag)+' not in AnalysisModel!.\n')
                result = -4
            else:
                theID = dof.getID()
                idSize = theID.Size()
                for j in range(0, idSize):
                    if theID[j] == -2:
                        dof.setID(j, eqnNumber)
                        eqnNumber += 1
        
        # iterate throgh  the DOFs second time setting -3 values
        for k in range(0, size):
            dofTag = orderedRefs[k]
            dof = self.theAnalysisModel.getDOF_Group(dofTag)
            if dof != None:
                theID = dof.getID()
                idSize = theID.Size()
                for j in range(0, idSize):
                    if theID[j] == -3:
                        dof.setID(j, eqnNumber)
                        eqnNumber += 1
        
        # iterate through the DOFs one last time setting any -4 values
        tDOFs = self.theAnalysisModel.getDOFs()
        for dof in tDOFs:
            theID = dof.getID()
            have4s = 0
            for i in range(0, theID.Size()):
                if theID[i] == -4:
                    have4s = 1
            if have4s == 1:
                nodeID = dof.getNodeTag()
                # loop through the MP_Constraints to see if any of the
                # DOFs are constrained, note constraint matrix must be diagonal
                # with 1's on the diagonal
                theMPs = theDomain.getMPs()
                for key, mp in theMPs.items():
                    # note keep looping over all in case multiple constraints
                    # are used to constrain a node -- can't assume intelli user
                    if mp.getNodeConstrained() == nodeID:
                        nodeRetained = mp.getNodeRetained() # int 
                        nodeRetainedPtr = theDomain.getNode(nodeRetained) # Node
                        retainedDOF = nodeRetainedPtr.getDOF_Group() # DOF_Group
                        # ID
                        retainedDOFIDs = retainedDOF.getID()
                        constrainedDOFs = mp.getConstrainedDOFs()
                        retainedDOFs = mp.getRetainedDOFs()
                        for i in range(0, constrainedDOFs.Size()):
                            dofC = constrainedDOFs[i]
                            dofR = retainedDOFs[i]
                            dofID = retainedDOFIDs[dofR]
                            dof.setID(dofC, dofID)
        
        numEqn = eqnNumber
        # iterate through the FE_Element getting them to set their IDs
        theEle = self.theAnalysisModel.getFEs()
        for ele in theEle:
            ele.setID()
        
        # set the numOfEquation in the Model
        self.theAnalysisModel.setNumEqn(numEqn)

        if result == 0:
            return numEqn
        
        return result
                        

    
    def getAnalysisModel(self):
        return self.theAnalysisModel
    
    def getGraphNumberer(self):
        return self.theGraphNumberer
    
