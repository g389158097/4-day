#作用域
#在python中，一个函数就是一个作用域
#局部变量的范围就是作用域
#作用域在定义完成后就已经生成了，作用链向上查找

age= 19
def func3():
    age =73
    print(age)
    def func4():
        print(age)
    func4()
func3()
#以后不管在哪调用，永远回到最早的地方去寻找作用域
