import time


def timer(func):
    """
    計時器，紀錄函數執行時間
    :param func: 函數
    :return:
    """
    def inner(*args, **kwargs):
        start_time = time.time()  # 紀錄起始時間
        try:
            res = func(*args, **kwargs)  # 執行函數
            end_time = time.time()  # 紀錄結束時間
            print(f"time consume {sec2sec(start_time, end_time)} sec.")
            return res
        except Exception as e:
            end_time = time.time()
            print(f"time consume {sec2sec(start_time, end_time)} sec.")
    return inner


def sec2min(start_time, end_time, decimal_places=2):
    """
    將計時器的總秒數轉換成 x 分 y 秒
    :param start_time:計時器開始的時間
    :param end_time:計時器結束的時間
    :param decimal_places:要呈現多少位小數點
    :return:元組(x,y)代表 x 分 y 秒
    """
    calculating_time_sec = round(end_time - start_time, decimal_places)
    calculating_time_min = (round(calculating_time_sec // 60), round(calculating_time_sec % 60, decimal_places))
    return calculating_time_min


def sec2sec(start_time, end_time, decimal_places=2):
    """
    將計時器的總秒數轉換成 x 秒
    :param start_time:計時器開始的時間
    :param end_time:計時器結束的時間
    :param decimal_places:要呈現多少位小數點
    :return:
    """
    calculating_time_sec = round(end_time - start_time, decimal_places)
    return calculating_time_sec
