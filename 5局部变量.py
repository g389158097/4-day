name = 'black'#全局变量
def change_name():
    name='HEISE'#只能在局部生效 局部变量
    print(name)
print(name)
change_name()
print(name)
#在函数里面定义的变量就叫做局部变量
#一个函数可以算作一个局部
#局部变量的优先级大于全局变量
#函数里面可以调用全局变量，但是函数外面不可以调用全局变量


