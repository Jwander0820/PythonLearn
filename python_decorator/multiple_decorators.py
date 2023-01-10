"""
# 參考自 https://steam.oxxostudio.tw/category/python/basic/decorator.html
多重裝飾器的堆疊觸發順序為由下而上
"""


def a1(func):
    print('1')
    return func


def a2(func):
    print('2')
    return func


def a3(func):
    print('3')
    return func


@a1
@a2
@a3
def b():
    print('go!!!!')


if __name__ == "__main__":
    b()
