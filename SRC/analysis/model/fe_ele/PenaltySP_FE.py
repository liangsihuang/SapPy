from SRC.analysis.model.fe_ele.FE_Element import FE_Element
from SRC.matrix.ID import ID

class PenaltySP_FE(FE_Element):
    def __init__(self, tag, theDomain, theSP, alpha=1.0e8):
        self.theTag = tag
        self.myDOF_Groups = ID(1)
        self.numDOF = 1
        self.alpha = alpha
        self.theSP = theSP
        self.theNode = theDomain.getNode(theSP.getNodeTag())
        if self.theNode == None:
            print('FATAL PenaltySP_FE::PenaltySP_FE() - no Node: '+str(theSP.getNodeTag)+' in domain.\n')
        
        dofGrp = self.theNode.getDOF_Group()
        if dofGrp != None:
            self.myDOF_Groups[0] = dofGrp.getTag()
        
