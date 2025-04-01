import logging

# 可以将日志输出到指定文件
logging.basicConfig(level=logging.INFO)


def divide():
    try:
        a = int(input("请输入被除数:"))
        b = int(input("请输入除数:"))
        # 会抛出一个AssertionError的异常,所以程序里，充满Assert和print不是一个好的编程习惯
        assert b != 0, '除数不能为零'
        print(a / b)
    except ZeroDivisionError:
        print("除数不能为零")
    except ValueError:
        print("输入格式不正确，请输入数字")
    # 捕获所有的异常，这里会出现提示，捕获过广异常
    except BaseException:
        logging.info("未知错误", exc_info=True)
    finally:
        print("程序结束")


if __name__ == '__main__':
    divide()
