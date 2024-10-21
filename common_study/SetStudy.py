# 创建集合
s = {1, 2, 3}

s.add(4)
s.remove(2)
print(s)
# s.clear()
# print(s)
# 遍历1
for item in s:
    print(f"value:{item}")

for index, item in enumerate(s):
    print(f'index:{index},value:{item}')

# 集合生成式
s = {i for i in range(0, 10)}
print(s)

p = {i for i in range(0, 10) if i % 2 == 1}
print(p)
