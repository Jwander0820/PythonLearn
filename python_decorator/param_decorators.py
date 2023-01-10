"""'
參考自: https://bbs.huaweicloud.com/blogs/344728
"""


def logging(flag):
    def decorator(fn):
        def inner(num1, num2):
            if flag == "+":
                print("--正在努力加法計算--")
            elif flag == "-":
                print("--正在努力減法計算--")
            result = fn(num1, num2)
            return result
        return inner

    # 返回裝飾器
    return decorator


# 使用裝飾器裝飾函數
@logging("+")
def add(a, b):
    result = a + b
    return result


@logging("-")
def sub(a, b):
    result = a - b
    return result


if __name__ == "__main__":
    print(add(1, 2))
    print(sub(1, 2))
