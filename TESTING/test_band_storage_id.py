import numpy as np
		#     [ 4  2 -1  0  0  0]       [1]
		#     [ 2  5  2 -1  0  0]       [2]
		# A = [-1  2  6  2 -1  0]   b = [2]
		#     [ 0 -1  2  7  2 -1]       [3]
		#     [ 0  0 -1  2  8  2]       [3]
		#     [ 0  0  0 -1  2  9]       [3]

# ab[u + i - j, j] == a[i,j]   (if upper form; i <= j)

# answer: 
#     [ 0  0  0  0 -1  0]       
#     [ 0  0  0  2  0  0]      
#     [ 0  0 -1 -1  0 -1] 
#     [ 0  2  2  0  2  2] 
#     [ 6  5  4  7  8  9] 
A = np.array([[4, 2, -1, 0, 0, 0], [2, 5, 2, -1, 0, 0], [-1, 2, 6, 2, -1, 0], [0, -1, 2, 7, 2, -1], [0, 0, -1, 2, 8, 2], [0, 0, 0, -1, 2, 9]])
half_band = 5
rowNo = np.size(A, 0)
colNo = np.size(A, 1)
ab = np.zeros((half_band, colNo))

id1 = np.array([2, 1, 0, 3, 4, 5])
idSize = np.size(id1)

for i in range(0, idSize):
	row = id1[i]
	for j in range(0, idSize):
		col = id1[j]
		if row <= col:
			ab[half_band-1+row-col, col] += A[i,j]

print(ab)

