#调用下一次递归时使用return
def calc(n):
    return calc(n+1)

#当递归的结果与上一次送的无关时，就可以减少栈的使用，进行优化
