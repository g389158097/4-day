#形参 调用时分配内存单元   创建函数时给定的参数
#实参 调用函数是给的参数 必须在内存里真正存在的，什么类型都可以接受


#默认参数
def cbc(name,age, country='chinese'):
    print('my name is',name,'age is',age,'country is',country)
cbc('cv',25)
cbc('ab',25,'koera')
#一个要点 正常情况下，默认参数必须放在最后


#关键参数
#关键参数必须放在位置参数之后
#调用参数
cbc(23,country='usa',age=22)
cbc(25,'eu')


#非固定参数
#原来参数只有一个，随着发展，参数变为了好多个参数 参数之前加*
def send_alert(name,*user):
    print('快跑啊',name,user)
    for i in user:
        print(name,i)
send_alert('cbc',1,2,3,4)
#内部打包为元组形式
#方式一：带*
#方式二：直接传递一个列表或者元祖 注意 传递列表或者元祖的时候前面也要加*[1,2,3,4]
#带*的参数必须放在后面

#**另一种非固定参数**

