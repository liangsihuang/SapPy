from SRC.domain.domain.Domain import Domain
a = Domain()

<<<<<<< HEAD
if a is Domain:
    print('1')
else:
    print('2')
=======
if isinstance(a, Domain):
    print('1')  # 打印成功

# isinstance() 考虑继承：子类也是父类的类型

print(a is Domain)  # 打印 False

>>>>>>> 9240c810cff6f5636af03dfe0e71cb8366be9db7
