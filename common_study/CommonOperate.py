import keyword

print("hello world")
a = 100
b = 2
print(f"计算的结果为：{a * b}")
print("hello world", "sss")
# Assic码值
print(chr(98))
print('C')

# 输出文件到指定目录
filePrint = open("note.txt", 'w')
# sep：分隔符 end 结束符号 file：文件流
print("hello world1", "aaa", sep='%', end='---》', file=filePrint)
filePrint.close()

# 关键字
print(keyword.kwlist)
print(len(keyword.kwlist))

# 动态语言
luck_number = 8
luck_number2 = 8
luck_number2 = 'suska'
my_name = 'naruto'
my_name2 = 'naruto'
print('luck_number', type(luck_number))
print('my_name', type(my_name))

# 内存地址
print('luck_number 内存地址', id(luck_number))
print('luck_number2 内存地址', id(luck_number2))
print('my_name2 内存地址', id(my_name2))
print('my_name 内存地址', id(my_name))

# 数据类型 整数、浮点型、复数(分为实数、虚数两部分)
int_value = 10
float_value = 20.2
print('int_value:', type(int_value))
print('float_value:', type(float_value))
# 浮点型数据计算有尾差
print(0.1 + 0.3)
print(round(0.1 + 0.3, 1))
