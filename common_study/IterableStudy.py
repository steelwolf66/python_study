from _collections_abc import Iterable
# list
L = [1, 2, 3, 4, 4]
# set
S = {1, 2, 2, 3}

# 判断是否可迭代
print(isinstance(L,Iterable))

for item in L:
    print(item)

for item in S:
    print(item)
#带有索引的遍历方式
enumerated = enumerate(L)
print(type(enumerated))
for item in enumerated:
    print(item)