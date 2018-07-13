#想在函数里面修改全局变量 global
name = 'black'#全局变量
def change_name():
    global name
    name= 'heise'#顺序不能颠倒，先声明global
    print(name)
print(name)
change_name()
print(name)
#实际开发建议，尽量不要用global，容易把全局变量给改了


#但是如果全局变量是一个列表，修改里表里面的元素，整个代码的列表都会被修改了
#因为整个列表是一个固定的内存地址
#可以被修改字典列表元组等等
