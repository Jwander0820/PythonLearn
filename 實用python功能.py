show = 1

if show == 1:
    # 使用 in 走訪清單內元素
    mylist = [0, 1, 2, 3, 5, 7]
    for item in mylist:
        print(item)

if show == 2:
    # 使用 enumerate 走訪元素和索引(index)
    my_list = ["apple", "banana", "cat"]
    for i, item in enumerate(my_list):
        print(i, item)

if show == 3:
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

if show == 4:
    # 使用item走訪map 取得key,value
    names = ["John", "Tom", "Tina"]
    ages = [17, 23, 20]
    my_dict = dict(zip(names, ages))
    print(my_dict)

    for k, v in my_dict.items():  # 較佳
        print(k, v)

    for key in my_dict:  # 較繁瑣，較不佳
        print(key, my_dict[key])

    for key in my_dict:
        print(key)

    for val in my_dict.values():
        print(val)

if show == 5:
    # 兩值交換
    a = 10
    b = 87
    print(a, b)
    a, b = b, a
    print(a, b)

if show == 6:
    a = 50
    if 0 < a and a < 100:  # 較不佳，多個 and
        print("1 ~ 100 case")

    if 0 < a < 100:  # 較簡潔
        print("1 ~ 100 case")

if show == 7:
    flag = True
    mylist = []
    if len(mylist) == 0:
        print("empty list")
    if flag == True:
        print("flag true!")
        # 以上為不佳的示範
    if not mylist:  # 較簡潔
        print("empty list")
    if flag:  # 因為flge本身就是布林值，因此無須再做True or False的判斷
        print("flag true!")
    # 布林值為Flase的狀況通常有以下幾種
    # 1. False ； 2. None ； 3. 空的字串"" ； 4. 數字0 ； 5. 空的容器 [](){}set()

if show == 99:
    # 僅做說明，python常用上下文管理器 with 來做文件的處理，執行完便會自動關閉檔案，不須再一行myfile.close
    with open('data.txt') as myfile:
        for line in myfile:
            print(line)

if show == 8:
    # 字串的連接用 join 
    names = ['Tom', 'John', 'Tina']
    names_str = names[0]
    for name in names[1:]:  # 錯誤示範
        names_str += ', ' + name
    print(names_str)

    names_str = ", ".join(names)
    print(names_str)

if show == 9:
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

if show == 10:
    # 而 python 的 Function 中有兩個好用的特色：
    # 1. 一次可以回傳多個值 2. 用 _ 省略忽略的回傳值
    def foo():
        a, b = 3, 5.5
        return a, b, a + b


    alpha, beta, ans = foo()
    _, _, ans = foo()
    print(_)  # 交互變數 "_" 會保留最近一次的輸出，當想省略 function 回傳變數時，通常也用這個變數來接住省略的變數。
    print(ans)

if show == 11:
    # 小心可變變數 (mutable variable) 作為參數 default 值造成的錯誤
    # 一個好的解法是把可變變數的參數位置用 None 作為預設值，進到函式再進行初始化。
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
