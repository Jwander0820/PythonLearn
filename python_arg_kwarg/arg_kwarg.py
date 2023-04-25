def test_more(*args, **kwargs):
    """
    收集位置引數和關鍵字引數，並將它們作為tuple和dict分別返回。

    :param args: 位置引數
    :param kwargs: 關鍵字引數
    :return: 位置引數tuple和關鍵字引數dict
    """
    return args, kwargs


def test_use_arg_to_def(**kwargs):
    """
    使用關鍵字引數作為輸入，並打印它們。

    :param kwargs: 關鍵字引數
    """
    print(kwargs)


def main():
    print(test_more(1, 2, key='word', key2='wwwww'))  # ((1, 2), {'key': 'word', 'key2': 'wwwww'})

    print(test_more(1, 2, 3, 4, apple=45, mark=100,
                    allen=300))  # ((1, 2, 3, 4), {'apple': 45, 'mark': 100, 'allen': 300})

    print(test_more(1, 2, 3, 4, None))  # ((1, 2, 3, 4, None), {})

    print(test_more(apple='eat', mark=100, allen=300,
                    test=[1, 2, 5]))  # ((), {'apple': 'eat', 'mark': 100, 'allen': 300, 'test': [1, 2, 5]})

    args, kwargs = test_more(1, 2, 3, 4, None, apple='eat', mark=100, allen=500, test=[1, 2, 3, 5])
    print(args)  # (1, 2, 3, 4, None)

    print(kwargs)  # {'apple': 'eat', 'mark': 100, 'allen': 500, 'test': [1, 2, 3, 5]}

    print(type(args))  # <class 'tuple'>
    print(type(kwargs))  # <class 'dict'>

    test_use_arg_to_def(module="classifier", deal_page=10)


if __name__ == "__main__":
    main()
