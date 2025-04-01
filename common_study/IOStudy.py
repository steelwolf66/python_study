
with open('D:\\催记.txt', mode='r') as f:
    print(type(f))
    dataList = f.readlines()
    for item in dataList:
        print(item.strip())