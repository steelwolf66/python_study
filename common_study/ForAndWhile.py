# 获取1-999的水仙花数 水仙花数：一个数的各个位数的三次方相加后，等于这个数的本身 eg:153 = 1*1*1 + 5*5*5 + 3*3*3
# / 除以 // 整除 % 取余
rangeValue = range(1, 1000)
for i in rangeValue:
    if i < 10:  # 个位数
        if i * i * i == i:
            print(i)
    elif i < 100:  # 两位数
        t = i // 10 % 10  # 十位
        s = i % 10  # 个位
        if t ** 3 + s ** 3 == i:
            print(i)
    else:  # 三位数
        o = i // 100  # 百位
        t = i // 10 % 10  # 十位
        s = i % 10  # 个位
        if s ** 3 + t ** 3 + o ** 3 == i:
            print(i)
            print(f'o:{o},t:{t},s:{s}')

# 无限循环
# 用户输入数据，并转换数据类型
user_input = input('请输入数据：')
user_input_value = int(user_input)
count = 10
while user_input_value >= 100:
    print(f'value:{user_input}')
    count -= 1
    if count == 0:
        break
else:
    print("value less than 100")

# 空语句 pass
for item in rangeValue:
    pass
