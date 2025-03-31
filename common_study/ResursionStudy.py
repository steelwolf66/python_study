# 阶乘，递归调用，处理特殊情况1
def fact(n):
    if n == 1:
        return 1
    return fact(n - 1) * n


print(fact(8))
