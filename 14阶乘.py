# def calc(num):
#     global result
#     result=result*num
#     num=num-1
#     if num>1:
#      calc(num)
#     else:
#         print(result)
#
#
# result=1
# calc(10)
#屌丝版


def calc(n):
    if n>1:
     return n*calc(n-1)
    else:
        return 1
print(calc(10))
