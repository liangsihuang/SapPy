import numpy as np 
a = 2
# b = np.array(None)
b = None
if a > 0  and b == None:
    print('1')  # ok!

# 发生异常: ValueError
# The truth value of an array with more than one element is ambiguous. Use a.any() or a.all()
# b = np.array([1,2])
# if a > 0  and b == None:
#     print('1') 


b = np.array([1,2])
if a > 0  and (b == None).all():
    print('1') # ok!
