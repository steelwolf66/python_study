# if elif else
age = 2
if age > 20:
    print("age > 20")
elif age < 18:
    print("age < 18")
else:
    print("between 28~20")

# match
match age:
    case x if age > 20:
        print(f'{x}')
    case 18:
        print('==18')
    case _:
        print("not match")

# for
sum = 0
# 0-100
for x in range(101):
    sum = sum + x;
print(sum)

sum = 0
# while
y = 1
while y <= 100:
    sum = sum + y
    y = y + 1
print(sum)

# dict set
names = ['james', 'ad', 'wade', 'lucka']
scores = ['100', '93', '94', '96']
# 构建 dict ,注意，dict内部顺序和key value 放入顺序无关
name_score_dict = {}
for name in names:
    for score in scores:
        name_score_dict[name] = score
print(name_score_dict)
print(name_score_dict['james'])
# 用来判断是否包含Key，而value不能被判断
print('james' in name_score_dict)
print('96' in name_score_dict)
# get 方法返回value或缺省值
durant_score = name_score_dict.get('durant', '96')
karry_score = name_score_dict.get('karry')
print(durant_score)
# 没有数据时 返回None
print(f'karry_score:{karry_score}')
# 删除Key,不存在时会报错
# name_score_dict.pop('durant')

# dict 和List的区别
# dict 不会随着元素变多，查找和插入变慢，但是需要占用大量内存，内存浪费多
# list 查找和插入随着元素数量增加而变慢，但是占用空间小
# 所以 dict是空间换时间的典型表现
# dict 的Key必须是不可变对象

# set和dict类似，是一组Key的集合，但是不存储value，并且key不能重复，所以在set中，没有重复的key
set1 = {1, 2, 3}
print(set1)
# 自然也可以使用list作为set的入参
set2 = set([1, 2, 3, 4, 4, 4, 4, 4])
print(set2)
print(type(set2))
set2.add(5)
# set2.pop()
set2.remove(2)
print(f'set1：{set1}')
print(f'set2：{set2}')
# 交并
print(set1 & set2)
print(set1 | set2)


