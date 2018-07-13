def func1():
    print('alex')
    def func2():
        print('eric')
    func2()
        #嵌套就是一个函数里面还有另一个函数
func1()#若无人调用func2，永远不会打印eric
#所以需要再函数内部再调用一次

age= 19
def func3():
    age =73
    print(age)
    def func4():
        print(age)
    func4()
func3()

#与global的关系
