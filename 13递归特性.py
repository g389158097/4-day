#1.必须要有一个明确的终止条件
#2.每次进入一个更深层次的递归是，复杂程度都应当减小 每一次都应当有所作为
#3.递归的效率不高 层次过多导致栈溢出

#递归练习题
import sys
menus = [
    {
        'text':'北京',
        'children':[
            {
                'text':'朝阳','children':[]
            },
            {
                'text':'昌平','children':
                [
                {
                    'text':'沙河','children':[]
                },
                {
                    'text':'回龙观','children':[]
                }
                ]
            }


        ]

    },
    {
        'text':'上海',
        'children':[
            {
                'text':'宝山','children':[]
            },
            {
                'text':'金山','children':[]
            }


        ]

    }
]
# print(menus[0]['children'][1])



#深度查询
#1.打印所有的节点
#2.输入一个节点名字，找到了就打印，并返回true
# def pra(n,count=0):
#     print('--------开始打印节点--------')
#     long=len(n)
#     print(long)
#     print(n[count])
#     if count+1==long:
#         print('打印完毕')
#     else:
#        pra(n,count+1)
#
# pra(menus)
#
def recurPrintPath(dic):
    for i in dic:
        print(i)
        #判断下一级是否还是字典，如果是字典继续递归
        if type(i) == type({}):
            recurPrintPath(i)
        else:
            print (dic[i])
            print ('--------------')

recurPrintPath(menus)

