# 装饰器 decorator
# 在定义的方法上，增加@+方法名，会在执行方法时，先执行@方法

def log(func):
    # 织入逻辑
    def wrapper(*args, **kw):
        print(f'func:{func.__name__},time:17:44')
        # 调用原始逻辑
        func(*args, **kw)

    return wrapper


@log
def nowTime():
    print('202503031')


nowTime()

#当然，也支持传入log参数，只不过需要封装3层，先接收参数，再接收方法名，再接收织入逻辑，不过打印的方法名会有问题，需要借助functools.wraps()获取被织入的原始方法名
