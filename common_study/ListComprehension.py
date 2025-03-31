# 列表推导
squares = [x * 2 for x in range(10)]
print(f'squares{squares}')

# 列表生成式
list1 = [x for x in range(11)]
list2 = [x * x for x in list1]

list3 = [x * x for x in list1 if x % 2 == 0]
print(f'list1:{list1},list2:{list2},list3:{list3}')
