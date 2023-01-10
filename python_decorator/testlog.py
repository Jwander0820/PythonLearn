import time
from logger import create_logger, log_filter
from timer import timer
from class_decorators import Log


@log_filter
def test_plus(a, b):
    c = a + b
    return c


@Log
def test_timer(a):
    time.sleep(1.5)
    return a


if __name__ == "__main__":
    # test_plus(1, 3)
    # test_plus(1, "1")  # 刻意引發錯誤
    # test_plus()  # 刻意引發錯誤
    test_timer(1)
