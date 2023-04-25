def example1():
    # 使用 in 走訪清單內元素
    mylist = [0, 1, 2, 3, 5, 7]
    for item in mylist:
        print(item)


def example2():
    # 使用 enumerate 走訪元素和索引(index)
    my_list = ["apple", "banana", "cat"]
    for i, item in enumerate(my_list):
        print(i, item)


def example3():
    # 使用 zip 可以同時走訪多個list，以及做Dict的轉換
    names = ["John", "Tom", "Tina"]
    ages = [17, 23, 20]
    for x, y in zip(names, ages):
        print(x, y)

    # gender = ['M', 'M', 'F']
    # for x, y, z in zip(names, ages, gender):
    #     print(x, y, z)

    # 透過zip將兩組清單組成字典(dict)
    my_dict = dict(zip(names, ages))
    print(my_dict)


def example4():
    # 使用item走訪map 取得key,value
    names = ["John", "Tom", "Tina"]
    ages = [17, 23, 20]
    my_dict = dict(zip(names, ages))
    print(my_dict)
    for k, v in my_dict.items():
        print(k, v)
    # for key in my_dict:  # 較繁瑣，較不佳
    #     print(key, my_dict[key])


def example5():
    # 兩值交換，語法糖
    a = 10
    b = 87
    print(a, b)
    a, b = b, a
    print(a, b)


def example6():
    a = 50
    if 0 < a and a < 100:  # 較不佳，多個 and
        print("1 ~ 100 case")

    if 0 < a < 100:  # 較簡潔
        print("1 ~ 100 case")


def example7():
    flag = True
    mylist = []
    # 以下為不佳示範
    # if len(mylist) == 0:
    #     print("empty list")
    # if flag == True:
    #     print("flag true!")

    # 以下為正確用法
    if not mylist:  # 較簡潔
        print("empty list")
    if flag:  # 因為flge本身就是布林值，因此無須再做True or False的判斷
        print("flag true!")
    # 布林值為False的狀況通常有以下幾種
    # 1. False ； 2. None ； 3. 空的字串"" ； 4. 數字0 ； 5. 空的容器 [](){}set()


def example8():
    # 字串的連接用 join
    names = ['Tom', 'John', 'Tina']
    names_str = ", ".join(names)
    print(names_str)


def example9():
    # 注意 Python 的 string formatting 方式
    # 由於歷史因素，python 的 string formatting 有多種方式
    # 雖然舊版的 % 方式沒有停止支援，但還是建議使用新版的 str.format() 相關用法：
    name, method = 'Tom', 'A: string concate'
    print("Hi " + name + ", Using Method " + method + " is not a good idea...")

    name, method = 'Tom', 'B: old python2 formatting'
    print('Hi %s, Using Method %s is not a good idea, either.' % (name, method))

    name, method = 'Tom', 'C: python3 formatting'
    print('Hi {name}, Using Method {method} is a good idea!'.format(name=name, method=method))

    name, method = 'Tom', 'D: python3 f formatting'  # 建議使用新版方式(舊版通時並存但不建議)
    print(f'Hi {name}, Using Method {method} is a good idea, too.')

    # Hi Tom, Using Method A: string concate is not a good idea...
    # Hi Tom, Using Method B: old python2 formatting is not a good idea, either.
    # Hi Tom, Using Method C: python3 formatting is a good idea!
    # Hi Tom, Using Method D: python3 f formatting is a good idea, too.


def example10():
    def foo():
        a, b = 3, 5.5
        return a, b, a + b

    _, _, ans = foo()
    print(_)  # 交互變數 "_" 會保留最近一次的輸出，當想省略 function 回傳變數時，通常也用這個變數來接住省略的變數。
    print(ans)


def example11():
    from datetime import datetime
    import time

    # 在下面的函式範例中，datetime 不會每次更新且 list 狀態也不會每次清空。
    # 這個不符合預期的行為，是可變變數 (mutable variable) 保留前次呼叫的狀態所造成。
    def get_datetime_log_bad(mydate=datetime.now(), my_log_list=[]):
        my_log_list.append("current log {}".format(datetime.strftime(mydate, "%Y/%m/%d %H:%M:%S")))
        return my_log_list

    print(get_datetime_log_bad())
    time.sleep(1)
    print(get_datetime_log_bad())
    time.sleep(1)
    print(get_datetime_log_bad())

    def get_datetime_log_good(mydate=None, my_log_list=None):
        mydate = datetime.now() if mydate is None else mydate
        if my_log_list is None:
            my_log_list = []
        my_log_list.append("current log {}".format(datetime.strftime(mydate, "%Y/%m/%d %H:%M:%S")))
        return my_log_list

    print(get_datetime_log_good())
    time.sleep(1)
    print(get_datetime_log_good())
    time.sleep(1)
    print(get_datetime_log_good())


if __name__ == "__main__":
    example1()
    example2()
    example3()
    example4()
    example5()
    example6()
    example7()
    example8()
    example9()
    example10()
    example11()
