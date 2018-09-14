# Reverse Cuthill-mcKenn numbering scheme

# from scipy.sparse.csgraph._reordering import reverse_cuthill_mckee
# scipy.sparse.csgraph.reverse_cuthill_mckee(graph, symmetric_mode=False)
# graph 参数 必须是 csc_matrix，不通用
# from scipy.sparse import csc_matrix
# import numpy as np 
# a = np.array([[1, 0, 1, 0, 0, 0, 0, 1, 1],
#             [0, 1, 1, 0, 0, 1, 1, 1, 0],
#             [1, 1, 1, 0, 0, 0, 0, 0, 0],
#             [0, 0, 0, 1, 0, 0, 0, 1, 1],
#             [0, 0, 0, 0, 1, 0, 1, 1, 0],
#             [0, 1, 0, 0, 0, 1, 1, 0, 0],
#             [0, 1, 0, 0, 1, 1, 1, 0, 0],
#             [1, 1, 0, 1, 1, 0, 0, 1, 0],
#             [1, 0, 0, 1, 0, 0, 0, 0, 1]])
# a_csc = csc_matrix(a) # 储存了33个元素（33个1）
# b = reverse_cuthill_mckee(a_csc) # Array of permuted row and column indices.

from SRC.domain.Node import Node

node1 = Node(1, 2, 1, 0)
node2 = Node(2, 2, 2, 1)
node3 = Node(3, 2, 2, 0)
node4 = Node(4, 2, 0, 1)
node5 = Node(5, 2, 1, 2)
node6 = Node(6, 2, 3, 2)
node7 = Node(7, 2, 2, 2)
node8 = Node(8, 2, 1, 1)
node9 = Node(9, 2, 0, 0)

