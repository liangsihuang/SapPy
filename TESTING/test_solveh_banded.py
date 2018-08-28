from scipy.linalg import solveh_banded
import numpy as np
# Solve the banded system A x = b, where::
        #     [ 4  2 -1  0  0  0]       [1]
        #     [ 2  5  2 -1  0  0]       [2]
        # A = [-1  2  6  2 -1  0]   b = [2]
        #     [ 0 -1  2  7  2 -1]       [3]
        #     [ 0  0 -1  2  8  2]       [3]
        #     [ 0  0  0 -1  2  9]       [3]

# answer: array([ 0.03431373,  0.45938375,  0.05602241,  0.47759104,  0.17577031,  0.34733894])

# upper storage: 
#     [ 0  0 -1 -1 -1 -1]       
#     [ 0  2  2  2  2  2]      
#     [ 4  5  6  7  8  9] 

ab = np.array([[0, 0, -1, -1, -1, -1], [0, 2, 2, 2, 2, 2], [4, 5, 6, 7, 8, 9]])
b = np.array([1, 2, 2, 3, 3, 3])

x = solveh_banded(ab, b)
print(x)
