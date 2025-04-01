from types import MethodType
from enum import Enum,unique

# 支持多继承
class student(object):
    # 类属性，如果实例属性不存在，则默认使用类属性，修改实例属性，类属性不会被修改
    age = 22

    def __init__(self, name, score):
        self.name = name
        self.score = score

    def print_info(self):
        print(f'name:{self.name},score:{self.score},age:{self.age}')


# 继承
class Animal(object):
    def runing(self):
        print('animal is running')


class Cat(Animal):
    pass


class Dog(Animal):
    pass


def set_age(self, age):
    self.age = age


def set_score(self, score):
    self.score = score


class Person(object):
    # 限制该实例只能有两个属性，就不能通过 person.score设置新属性
    # 只在本类的实例中生效，继承无效
    __slots__ = ('age', 'name')

    def run(self):
        print('person is running')


# 多继承
class Man(Animal, Person):
    name = None

#枚举类
@unique
class Weekday(Enum):
    SUN = 0
    Mon = 1

if __name__ == '__main__':
    james = student('james', 22)
    james.print_info()
    dog = Dog()
    dog.runing()
    cat = Cat()
    cat.runing()
    # 继承的类，也是父级的实例
    print(isinstance(dog, Animal))
    # 获取类属性和方法，返回一个list
    print(dir(dog))
    print(dir(james))
    # 反射
    james.__setattr__('score', 100)
    print(james.__getattribute__('score'))
    # 公共方法，也可以用来获取方法
    # print(hasattr(james, 'name'))
    # getattr()
    # setattr()
    james.print_info()
    # 给实例绑定属性和方法
    james.length = 25
    print(hasattr(james, 'length'))
    james.set_age = MethodType(set_age, james)
    james.set_age(40)
    james.print_info()
    # 给类绑定方法
    student.set_score = set_score
    # 多继承方法调用，方法名相同时，优先执行被优先继承的父类的方法
    man = Man()
    man.runing()
    man.run()
    # 枚举类
    day1 = Weekday.Mon
    print(day1)
    print(type(day1))
    print('hello %s' % 'world')
