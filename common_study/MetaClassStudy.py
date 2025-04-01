class Animal(object):
    name = 'james'

    def printInfo(self):
        print(self.name)


def printClassInfo(self, name='world'):
    print('name:%s' % name)


def fn(self, name='world'):  # 先定义函数
    print('Hello, %s.' % name)


if __name__ == '__main__':
    # 使用type创建一个Class
    Hello = type('Hello', (object,), dict(hello=fn))  # 创建Hello class hello=fn 是将fn方法赋值给hello方法
    h = Hello()
    h.hello()

    Fish = type('Fish', (object,), dict(fish=printClassInfo))
    f = Fish()
    f.fish('s')

    animal = Animal()
    animal.printInfo()
    print(type(animal))