# 元组学习
s = 1
# 元组的创建1
p = (1,)
# 元组的创建2 根据关键字，构造一个元组，传参为一个可以遍历的对象
t = tuple("string")
e = tuple([1, 3, 4, 5, 6, ])
print(type(s))
print(type(p))
print(t)
print(e)
del e
print(e)
p = p.__add__((12,))
print(p)

for item in p:
    print(f'value:{item}')

print(f"max", max(p))
print(f"is in", 2 in p)
