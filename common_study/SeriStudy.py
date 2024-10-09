# 序列
# 	下列四种，被成为 组合数据类型
# 		列表 有序序列
# 		元组 有序序列
# 		字典 无序序列
# 		集合 无序序列
# 索引，用来访问序列数据 支持正向访问，也支持反向访问 方向访问时，最后一个下标为 -1,倒数第二个为-2,.....

str = "helloword"
print(f'length:{len(str)}')
print(f'lastWord:{str[-1]}')
for i in range(len(str)):
    print(f'{str[i]},i:{i}')

# 切片 访问序列中元素的一种方法
# 序列[start:end:step]  [) 开始下标，结束下标，步长默认为1
# start：切片的开始索引（包含） end:切片结束的索引（不包含） step:步长，默认为1,指从开始索引后，每次跳转到加上步长的索引后的数据
print(str[0:5:2])  # 即获取 0,2,4 的数据切片
print(str[0:5])  # 省略步长
print(str[:5])  # 省略开始索引和步长
print(str[1::])  # 省略结束索引和步长，默认取到最后的索引为止
print(str[0:30:])  # 省略结束索引和步长，默认取到最后的索引为止，结束索引可以大于序列的最大索引
# 打印分隔符
print('*' * 40)
# 反向访问 步长的± ，控制了切片方向
outOfControlStr = "0123456789"
print(outOfControlStr[-1:-11:-1])
print(outOfControlStr[-1:2:-1])
print('*' * 40)
print(outOfControlStr[-1:-8:1])  # 没有数据 根据切片方向，开始下标大于结束下标，所以没有数据 [9,2)
print(outOfControlStr[-1:9:1])  # 没有数据，因为下标为9，是不包括数据的，实际上，-1和9，对应的是同一个数据，所以被抛弃 [9,9)
print(outOfControlStr[9:9:1])  # 等价于上一个表达式
print(outOfControlStr[-1:10:1])  # 有数据， 开始下标和结束下标为[)区间 ，在这里，可以转化为 [9,10) ,所以，9可以被打印
print(outOfControlStr[-1:-8:-1])  # 有正常数据，反向打印
print(outOfControlStr[-1::-1])  # 省略写法，反向打印
