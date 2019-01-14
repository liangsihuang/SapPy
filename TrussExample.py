from SRC.analysis.algorithm.Linear import Linear
from SRC.analysis.analysis.StaticAnalysis import StaticAnalysis
from SRC.analysis.numberer.DOF_Numberer import DOF_Numberer
from SRC.analysis.handler.PenaltyConstraintHandler import \
    PenaltyConstraintHandler
from SRC.analysis.integrator.LoadControl import LoadControl
from SRC.analysis.model.AnalysisModel import AnalysisModel
from SRC.domain.domain.Domain import Domain
from SRC.domain.LoadPattern import LoadPattern
from SRC.domain.NodalLoad import NodalLoad
from SRC.domain.Node import Node
from SRC.domain.SP_Constraint import SP_Constraint
from SRC.domain.timeSeries.LinearSeries import LinearSeries
from SRC.element.Truss import Truss
from SRC.graph.RCM import RCM
from SRC.material.ElasticMaterial import ElasticMaterial
from SRC.system_of_eqn.LinearSOE.bandSPD.BandSPDLinLapackSolver import \
    BandSPDLinLapackSolver
from SRC.system_of_eqn.LinearSOE.bandSPD.BandSPDLinSOE import BandSPDLinSOE

theDomain = Domain()

node1 = Node(1, 2, 0.0, 0.0)
node2 = Node(2, 2, 144.0,  0.0)
node3 = Node(3, 2, 168.0,  0.0)
node4 = Node(4, 2,  72.0, 96.0)

theDomain.addNode(node1)
theDomain.addNode(node2)
theDomain.addNode(node3)
theDomain.addNode(node4)

theMaterial = ElasticMaterial(1, 3000.0)

truss1 = Truss(1, 2, 1, 4, theMaterial, 10.0)
truss2 = Truss(2, 2, 2, 4, theMaterial, 5.0)
truss3 = Truss(3, 2, 3, 4, theMaterial, 5.0)

theDomain.addElement(truss1)
theDomain.addElement(truss2)
theDomain.addElement(truss3)

sp1 = SP_Constraint(1, 1, 0.0, True)
sp2 = SP_Constraint(1, 2, 0.0, True)
sp3 = SP_Constraint(2, 1, 0.0, True)
sp4 = SP_Constraint(2, 2, 0.0, True)
sp5 = SP_Constraint(3, 1, 0.0, True)
sp6 = SP_Constraint(3, 2, 0.0, True)

theDomain.addSP_Constraint(sp1) 
theDomain.addSP_Constraint(sp2) 
theDomain.addSP_Constraint(sp3) 
theDomain.addSP_Constraint(sp4) 
theDomain.addSP_Constraint(sp5) 
theDomain.addSP_Constraint(sp6) 

theSeries = LinearSeries()
theLoadPattern = LoadPattern(1)
theLoadPattern.setTimeSeries(theSeries)
theDomain.addLoadPattern(theLoadPattern)

theLoadValues = [100.0, -50.0]
theLoad = NodalLoad(1, 4, theLoadValues)
theDomain.addNodalLoad(theLoad, 1)

theModel = AnalysisModel()
theSolnAlgo = Linear()
theIntegrator = LoadControl(1.0, 1, 1.0, 1.0)
theHandler = PenaltyConstraintHandler(1.0e8, 1.0e8)
theRCM = RCM()
theNumberer = DOF_Numberer(theRCM)
theSolver = BandSPDLinLapackSolver()
theSOE = BandSPDLinSOE(theSolver)

theAnalysis = StaticAnalysis(theDomain, theHandler, theNumberer, theModel, theSolnAlgo, theSOE, theIntegrator)

numSteps = 1
theAnalysis.analyze(numSteps)
