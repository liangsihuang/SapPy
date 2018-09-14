d = {'a':1,'b':2,'c':3}
# next(d) 报错
# dict is iterable, but not an iterator

# iterable 可以用for 循环
# for i in d:
#     print(d[i])

# for i, j in d.items():
#     print(i)
#     print(j)

# 可先转换为 iterator
it = iter(d)
# print(next(it)) # print: a, 说明：next 返回的是 key
# print(next(it)) 
# print(next(it)) 
# print(next(it)) # 发生异常：StopIteration

while True:
    try:
        print(next(it))
    except StopIteration:  # 这样就不会报错
        break