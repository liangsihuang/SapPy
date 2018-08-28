import numpy as np
		#     [ 4  2 -1  0  0  0]       [1]
		#     [ 2  5  2 -1  0  0]       [2]
		# A = [-1  2  6  2 -1  0]   b = [2]
		#     [ 0 -1  2  7  2 -1]       [3]
		#     [ 0  0 -1  2  8  2]       [3]
		#     [ 0  0  0 -1  2  9]       [3]

# ab[u + i - j, j] == a[i,j]   (if upper form; i <= j)

# answer: 
#     [ 0  0 -1 -1 -1 -1]       
#     [ 0  2  2  2  2  2]      
#     [ 4  5  6  7  8  9] 
A = np.array([[4, 2, -1, 0, 0, 0], [2, 5, 2, -1, 0, 0], [-1, 2, 6, 2, -1, 0], [0, -1, 2, 7, 2, -1], [0, 0, -1, 2, 8, 2], [0, 0, 0, -1, 2, 9]])
half_band = 3
rowNo = np.size(A, 0)
colNo = np.size(A, 1)
ab = np.zeros((half_band, colNo))

for i in range(0, rowNo):
	for j in range(0, colNo):
		if i <= j:
			ab[half_band-1+i-j, j] += A[i,j]

print(ab)

