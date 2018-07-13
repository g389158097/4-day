#函数就是把一堆代码封装起来，完成某一项功能
#返回值的初衷是为了确认函数的功能是否得到执行
#函数在执行过程中遇到return就会终止执行
def stu_register(name,age,course):
    print(name,age,course)
    if age>22:
        return False
    else:
        return name,age
status = stu_register('cbc',22,'PY')
print(status)
#没有return就返回none
#返回多个值返回的是元组
