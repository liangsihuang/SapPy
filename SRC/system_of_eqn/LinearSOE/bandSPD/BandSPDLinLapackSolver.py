from SRC.system_of_eqn.LinearSOE.bandSPD.BandSPDLinSolver import BandSPDLinSolver
from scipy.linalg import solveh_banded
class BandSPDLinLapackSolver(BandSPDLinSolver):
	SOLVER_TAGS_BandSPDLinLapackSolver = 3

	def __init__(self):
		super().__init__(BandSPDLinLapackSolver.SOLVER_TAGS_BandSPDLinLapackSolver)
	
	def solve(self):
		if(self.theSOE==None):
			print('WARNING BandSPDLinLapackSolver::solve() - No LinearSOE object has been set. \n')
			return -1

		A = self.theSOE.A
		B = self.theSOE.B

		# first copy B into X ???
		# for i in range(0, n):
		# 	X[i] = B[i]

		# now solve AX = B
		if self.theSOE.factored == False: 
			# factored == cholesky decomposition
			# factored and solve
			self.theSOE.X = solveh_banded(A, B)
		
		self.theSOE.factored = True
		return 0