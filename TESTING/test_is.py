from SRC.domain.domain.Domain import Domain
a = Domain()

if isinstance(a, Domain):
    print('1')  # 打印成功

# isinstance() 考虑继承：子类也是父类的类型

print(a is Domain)  # 打印 False

