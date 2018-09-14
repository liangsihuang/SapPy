import numpy as np
from SRC.matrix.ID import ID
id1 = ID()

a = np.array([1])

# test getitem
id1.setData(a)
print(id1[0])

# test setitem
id1[0] = 2
print(id1[0])


        
    
    


