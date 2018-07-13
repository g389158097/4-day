#循环除以很多次
#把10不断除以2，直到不能除为止

# def calc(n):
#     n=int(n/2)
#     return n
# r1=calc(10)
# r2=calc(r1)
# print(r2)

#递归 在函数里面调用自己
# def calc(n):
#     n=int(n/2)
#     if n==0:
#         print('无法再除')
#     else:
#         print(n)
#         calc(n)
#
# calc(10)



#递归的执行逻辑
#一环套一环

#递归的返回值计数器
def calc(n,count):
    print(n,count)
    if count<5:
        return calc(n/2,count+1)#这边也需要一个返回值
    else:
        print('程序结束')
        return n#多层递归返回只返回最上面一层 上面的return不可或缺
res=calc(188,1)
print('res',res)






