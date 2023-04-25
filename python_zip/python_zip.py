def zip_and_dict_demo(x, y):
    zipped = zip_lists(x, y)
    print("Zipped:")
    for i in zipped:
        print(i)

    zipped_dict = zipped_to_dict(x, y)
    print("\nZipped dict:")
    print(zipped_dict)
    find_value_in_dict(zipped_dict, 1234)

    print("\nIterate through keys:")
    iterate_keys(zipped_dict)

    print("\nIterate through values:")
    iterate_values(zipped_dict)

    print("\nIterate through items:")
    iterate_items(zipped_dict)


def zip_lists(x, y):
    """
    將兩個列表壓縮成一個 zip 對象
    """
    return zip(x, y)


def zipped_to_dict(x, y):
    """
    將兩個列表壓縮成一個字典
    """
    return dict(zip(x, y))


def find_value_in_dict(zipped_dict, value):
    """
    在字典中查找特定值
    """
    for key in zipped_dict:
        if zipped_dict[key] == value:
            print(f"鍵值 {key} 的資料為 {zipped_dict[key]}")


def iterate_keys(zipped_dict):
    """
    遍歷並打印字典的鍵
    """
    for key in zipped_dict.keys():
        print(key)


def iterate_values(zipped_dict):
    """
    遍歷並打印字典的值
    """
    for value in zipped_dict.values():
        print(value)


def iterate_items(zipped_dict):
    """
    遍歷並打印字典的鍵和值
    """
    for key, value in zipped_dict.items():
        print(key, value)


if __name__ == "__main__":
    x = [1, 2, 3, 4, 5, 6, 7]
    y = [12, 1234, 1234, 1231, 123, 12, 324]
    zip_and_dict_demo(x, y)
