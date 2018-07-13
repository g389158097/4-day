def calu(x,y):
    return x*y


func=lambda x,y:x*y #声明一个匿名函数


print(calu(2,5))

print(func(3,5))

#lambda不支持复杂的逻辑关系  但是支持三元运算

#但是匿名函数的意义是什么呢？
#与其他的方法相结合使用
data = list(range(10))
print(data)

for index,i in enumerate(data):
    data[index] = i*i
print(data)


#map 方法 列表内的每一个函数都交给map执行一遍
#map(f2，data)
