def test_more(*args, **kwargs):
    """
    關鍵字引數說明
    :param args:
    :param kwargs:
    :return:
    """
    get_args = args
    get_kwargs = kwargs
    return get_args, get_kwargs


print(test_more(1, 2, key='word', key2='wwwww'))  # ((1, 2), {'key': 'word', 'key2': 'wwwww'})

print(test_more(1, 2, 3, 4, apple=45, mark=100, allen=300))  # ((1, 2, 3, 4), {'apple': 45, 'mark': 100, 'allen': 300})

print(test_more(1, 2, 3, 4, None))  # ((1, 2, 3, 4, None), {})

print(test_more(apple='eat', mark=100, allen=300,
                test=[1, 2, 5]))  # ((), {'apple': 'eat', 'mark': 100, 'allen': 300, 'test': [1, 2, 5]})

get_args, get_kwargs = test_more(1, 2, 3, 4, None, apple='eat', mark=100, allen=500, test=[1, 2, 3, 5])
print(get_args)  # (1, 2, 3, 4, None)

print(get_kwargs)  # {'apple': 'eat', 'mark': 100, 'allen': 500, 'test': [1, 2, 3, 5]}

print(type(get_args))  # <class 'tuple'>
print(type(get_kwargs))  # <class 'dict'>


def test_use_arg_to_def(**kwargs):
    print(kwargs)


if __name__ == "__main__":
    test_use_arg_to_def(module="moduleCFAE", deal_page=10)
