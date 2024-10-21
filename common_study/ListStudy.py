# 列表：有序，可变
# 操作列表中数据，该列表的内存地址不变
# 列表中各个数据的类型可以不同，这与Java中的泛型有所区别
list1 = [1, 2, 3, 4]
# del list1 删除列表 ，后续代码则会报错
# 方式1
for item in list1:
    print(item)
print('*' * 40)
# 方式2
for i in range(0, len(list1)):
    print(list1[i])
print('*' * 40)

# 方式3 enumerate:枚举类 其中index不是索引，而是指定的一个序号，start用来设置开始的序号
for index, item in enumerate(list1, start=2):
    print(index, item)

print('*' * 40, '列表操作')
print(f'原列表：{list1}')
print(list1.append(5))
print(f'操作1列表：{list1}')
list1.remove(1)
print(f'操作2列表：{list1}')
