class Map(object):
    def __init__(self):
        self.theMap = {'a':1,'b':2,'c':3}
        self.myIter = iter(self.theMap)

    def __iter__(self): 
        return self.myIter

    # def __next__(self):   # 这个不需要
    #     return next(self.myIter)
    
    def addComponent(self):
        self.theMap['d'] = 4
        self.myIter = iter(self.theMap) # 要加这一行，否则会报错 RuntimeError:dictionary changed size during iteration

m = Map()
# for i in m:
#     print(i) # 不会发生异常：StopIteration

# for i, j in m:
#     print(j)
# 报错
m.addComponent()
for i in m:
    print(i)