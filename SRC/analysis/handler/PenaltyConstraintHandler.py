from SRC.analysis.handler.ConstraintHandler import ConstraintHandler
from SRC.analysis.model.dof_grp.DOF_Group import DOF_Group
from SRC.analysis.model.fe_ele.FE_Element import FE_Element
from SRC.analysis.model.fe_ele.PenaltySP_FE import PenaltySP_FE

class PenaltyConstraintHandler(ConstraintHandler):
    HANDLER_TAG_PenaltyConstraintHandler = 3
    def __init__(self, sp, mp):
        ConstraintHandler.__init__(self, self.HANDLER_TAG_PenaltyConstraintHandler)
        self.alphaSP = sp
        self.alphaMP = mp

    def handle(self, nodesNumberedLast=None):
        theDomain = self.getDomain()
        theModel = self.getAnalysisModel()
        theIntegrator = self.getIntegrator()
        
        # first check links exist to a Domain and an AnalysisModel object
        if theDomain==None or theModel==None or theIntegrator==None:
            print('WARNING PenaltyConstraintHandler::handle() - setLinks() has not been called.\n')
            return -1
        
        # get number of elements and nodes in the domain and init the theFEs and theDOFs arrays
        numSPs = (theDomain.getSPs()).getNumComponents()
        # initialse the DOF_Groups and add them to the AnalysisModel. must of course set the initial IDs
        theNodes = theDomain.getNodes()
        numDofGrp = 0
        count3 = 0
        countDOF = 0
        for tag in theNodes:
            node = theNodes.getComponent(tag)
            dofGroup = DOF_Group(numDofGrp, node)
            numDofGrp += 1
            # initially set all the ID value to -2 (明明在构造函数中就设好了，不比重复做了吧)
            node.setDOF_Group(dofGroup)
            theModel.addDOF_Group(dofGroup)
            id1 = dofGroup.getID()
            countDOF += id1.Size()
        
        theModel.setNumEqn(countDOF)

        # see if we have to set any of the dof to -3
        if nodesNumberedLast!=None:
            for i in range(0,nodesNumberedLast.Size()):
                nodeID = nodesNumberedLast[i]
                node = theDomain.getNode(nodeID)
                if node!=None:
                    dofGrp = node.getDOF_Group()
                    id2 = dofGrp.getID()
                    # set all the dof values to -3
                    for j in range(0, id2.Size()):
                        if id2[j] == -2:
                            dofGrp.setID(j, -3)
                            count3 += 1
                        else:
                            print('WARNING PenaltyConstraintHandler::handle() - boundary sp constraint in subdomain'
                            +' this should not be - results suspect. \n')
        theEles = theDomain.getElements()
        numFeEle = 0
        for tag in theEles:
            ele = theEles.getComponent(tag)
            fe = FE_Element(numFeEle, ele)
            numFeEle += 1
            theModel.addFE_Element(fe)
        
        # create the PenaltySP_FE for the SP_Constraints and add to the AnalysisModel
        theSPsList = theDomain.getDomainAndLoadPatternSPs()
        for sp in theSPsList:
            fe = PenaltySP_FE(numFeEle, theDomain, sp, self.alphaSP)
            theModel.addFE_Element(fe)
            numFeEle += 1

        # create the PenaltyMP_FE for the MP_Constraints and add to the AnalysisModel
        # MP_Constraint 暂时不编
        return count3

        

