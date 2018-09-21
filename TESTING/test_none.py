a = None
import numpy as np 
b = np.array([2, 1])
c = None

print(a is None) # True

print(b is None) # False

print(c is None) # True

# is 比较两个对象的 id 值是否相等，是否指向同一个内存地址；
# == 比较的是两个对象的内容是否相等，值是否相等；默认会调用对象的 __eq__()方法。
# is 运算符比 == 效率高，在变量和None(有且仅有一个)进行比较时，应该使用 is。