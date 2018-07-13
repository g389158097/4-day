#节省代码量
#变量可以指向为一个函数
def calc(x,y):
    return x*y

#那么一个函数就可以接受另一个函数作为参数
def func(x):
    return x
print(calc(func(5),10))
#这就叫高阶函数
#还有另一种 return 返回另一个函数
def func2(x,y):
    return abs,x,y
print(func2(3,-10))

