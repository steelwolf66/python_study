# 创建字典1
d = {"1": "2", "2": "3"}
print(d)
print(type(d))

# 使用zip命令，创建映射关系的Dict
list1 = [1, 2, 3, 4]
list2 = ['naruto', 'boroto', 'james']
# zip命令，将俩个list，按照索引，映射成zip对象，如果需要获取dict对象，需要强转下，
# 这里需要注意，两个list下标不相等时，会以短下标为基准，生成字典对象
ziped = zip(list1, list2)
print(f'zip类型：{type(ziped)}')
zipDict = dict(ziped)
print(f'converted:{type(zipDict)}')
print(zipDict)
print('-' * 20)
# 第三种创建字典的方式，这里注意，key不能使用引号引起来，而value，是一个对象，key是程序会给加一个引号
d2 = dict(key1='value1', key2=2)
print(d2)
print(d2.get(2, '不存在'))
print('-' * 20)
# 遍历字典1
for key, value in zipDict.items():
    print(f'key:{key},value:{value}')
print('-' * 20)
# 遍历字典2
for index, item in enumerate(zipDict):
    print(f'index:{index},key:{key},value:{value}')
print('*-' * 20)
# 遍历3
for item in zipDict.items():
    print(item)  # 得到元祖
    print(f'key:{item[0]},value:{item[1]}')
keys = zipDict.keys();
print(type(keys))
for item in keys:
    print(item)