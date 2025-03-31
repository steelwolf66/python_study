value = abs(-2)
print(value)

maxValue = max(1, 1, 2, 3, 4)
print(maxValue)


# 定义一个函数，获取list集合中的最大绝对值的数据
def maxAbsoluteValue(param: list | tuple, max_default=100):
    for i in range(len(param)):
        param[i] = abs(param[i])
    print(param)
    return max_default if max(param) > max_default else max(param)


maxAbsolute = maxAbsoluteValue([1, 2, -93, 0, -99, 101])
print(maxAbsolute)


#  默认参数和位置参数，以及指定参数
def register(name, age, grade=1, city='beijing'):
    print(f'name:{name},age:{age},grade:{grade},city:{city}')


register('lu', '29')
register('lu', '29', 7)
register('lus', '29', 8, 'wuhan')
register('lu', '29', city='shanghai')


# 默认参数的坑
def add_end(L=[]):
    L.append("end")
    return L


# 修改
def add_end_new(L=None):
    # 这样多次调用返回的便是新的空对象
    if L is None:
        L = []
    L.append("end")
    return L


# 可变参数,这些可变参数，会被自动封装为tuple，而关键字参数会被封装为一个dict
def dynamicParam(*param):
    for item in param:
        print(item)
        print('**********')


# 关键字参数,这样可以更加灵活的调用，除了必须的信息要传入
def person(name, age, **kw):
    print(f'name:{name},age:{age},other:{kw}')


if __name__ == '__main__':
    param = [1]
    add_end(param)
    print(param)
    # add_end 调用两次后，默认参数的list使用的是一个对象，出现问题，和预期不一样
    add_end()
    print(add_end())
    print('*********************')
    # 处理后的方法，进行判断
    add_end_new()
    print(add_end_new())
    print('*********************')
    dynamicParam(1, 2, 3, 4)
    dynamicParam()
    # 如果已经拿到了一个list，需要将这里边的元素作为参数传入，可以在对象前加*
    list1 = [5, 6]
    dynamicParam(*list1)

    person("james", 12)
    person("james1", 12, city='beijing')
    person("james2", 13, city='beijing', grade=12)
    # 上述写法可以简化为下面的写法，进入方法后，kw变动，不会影响到other的值
    other = {'city': 'wuhan', 'grade': 15}
    person("james3", 14, **other)

