def test_args(*args):
    print(args)


def test_kwargs(**kwargs):
    print(kwargs)
    print(type(kwargs))
    for key, value in kwargs.items():
        print(f"{key} == {value}")


def test_all(*args, **kwargs):
    print(args)
    print(kwargs)
    print(kwargs.get("a"))  # 透過get取得kwargs的值
    kwargs.setdefault("test", "新增")  # 若預設值不存在，則新增該鍵值
    print(kwargs)
    kwargs.setdefault("a", "預設值")  # 若預設值不存在，則新增該鍵值
    print(kwargs)


if __name__ == "__main__":
    # 1. 測試傳入多個變數，透過args組合成元組
    print("EXP 1.")
    test_args('name', 'age', 'address', 'sex')
    print("\n")

    # 2. 測試傳入多個指定鍵值與變數，透過kwargs組合成字典
    print("EXP 2.")
    test_kwargs(name='tel', age=30, address='beijing')
    print("\n")

    # 3. 合併arg和kwarg的用法
    print("EXP 3.")
    test_all('name', 'age', name='tel', age=30)
    print("\n")

    # 4. 定義一個元組和字典，外部拆包再傳進去
    _tuple = (100, 2, 3, 4, 5)
    _dict = {'a': 100, 'b': 2, 'c': 3}
    # 測試拆包傳參數
    print("EXP 4.")
    test_all(*_tuple, **_dict)
    print("\n")
    # 若是沒有拆包，則會全部被判別為arg，被包成元組
    print("EXP 5.")
    test_all(_tuple, _dict)
