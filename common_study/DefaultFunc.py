str = 'hello'
#in    not in
print("e在hello中么",'e' in str)
print("a在hello中么",'a' in str)
print("a不在hello中么",'a' not in str)
#内置函数
print('len:',len(str))
print('max:',max(str))
print('min:',min(str))
# index函数，统计第一次出现的次数
print('s.index:',str.index('e'))
# print('s.index:',str.index('j')) #不存在，会报错 ValueError: substring not found
print('s.count:',str.count('l')) #不存在，会报错 ValueError: substring not found
