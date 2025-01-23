naruto = 'Naruto'
# 变为小写
lowerStr = naruto.lower()
# 全变为大写
upperStr = naruto.upper()
print(f"original:{naruto},type:{naruto},lower:{lowerStr},up:{upperStr}")
# 分隔
splitList = naruto.split('r')
print(type(splitList))
print(splitList)
# count 计数
print(naruto.count('r'))
# find 查找数据，并返回第一次出现的索引，不存在则返回-1
print(naruto.find('r'))
print(naruto.find('s'))
# index 和find 功能相同，但是不存在时，程序会报错
print(naruto.index('r'))
# print(naruto.index('s')) #异常信息 ValueError: substring not found
#字符串是否以 传参 为开头 或结尾
print(naruto.startswith('n'))
print(naruto.startswith('N'))
print(naruto.endswith("o"))
print(type(naruto.endswith('O')))#查看返回值类型




