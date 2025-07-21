import re

s = 'abc123'

matched = re.match(r'^.+', s)

if matched:
    print(matched)
    print(matched.group())
else:
    print('匹配失败')
