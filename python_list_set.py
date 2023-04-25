def list_sorting():
    # 1. 對清單排序
    x = [1, 3, 5, 2, 4]
    x_array = [[1, 2], [5, 4], [3, 0]]

    # 1.A 預設函數sorted，直接幫清單做排序，預設排序取第0位
    print(f"x清單排序 {sorted(x)}")
    print(f"二維x清單排序 {sorted(x_array)}")

    # 1.B sorted 進階排序，指定內部列表第n個元素為基礎做排序
    from operator import itemgetter
    x_array_sorted0 = sorted(x_array, key=itemgetter(0))
    x_array_sorted1 = sorted(x_array, key=itemgetter(1))
    print(f"二維x清單取第0個元素做排序 {x_array_sorted0}")
    print(F"二維x清單取第1個元素做排序 {x_array_sorted1}")
    print("\n")


def remove_duplicates():
    # 2. 刪除清單內重複項目
    x = [1, 3, 4, 1, 2, 2, 2]

    # 2.A 粗暴的for迴圈計算(會保留順序
    new_x_a = []
    for element in x:
        if element not in new_x_a:
            new_x_a.append(element)
    print(f"for迴圈刪除重複元素 {new_x_a}")

    # 2.B 函式計算(會保留順序)
    from collections import OrderedDict
    new_x_b = list(OrderedDict.fromkeys(x))
    print(f"函式刪除重複元素{new_x_b}")

    # 2.C 直接轉set(集合)再轉回來，這樣若有重複的元素值就會被消除，但須注意集合也會自動排序
    # 若非常在意順序的資料盡量避免使用
    new_x_c_set = list(set(x))
    print(f"集合刪除重複元素{new_x_c_set}")
    print("\n")


def set_operations():
    # 3. 集合基本運算操作
    # 3.0 基本集合運算
    x_set = {1, 3, 4}
    x_set.add(2)  # 加入元素資料
    print(x_set)
    x_set.add(1)  # 加入元素資料若已有元素，無作用
    print(x_set)
    x_set.remove(3)  # 移除指定元素
    print(x_set)
    x_set.clear()  # 清空集合
    print(x_set)

    # 3.A 集合判斷是否相同
    x = {1, 2, 3}
    y = {3, 1, 2}
    z = {1, 1, 1}
    print(x == y)  # 若集合相同 輸出True
    print(x == z)  # 若集合不同 輸出False

    # 3.B 集合運算(聯集、交集、差集、對稱差集)
    x = {1, 2, 3}
    y = {2, 4, 5}
    print(f"x y 取聯集 {x | y}")  # xy取聯集 合併兩個集合元素
    print(f"x y 取交集 {x & y}")  # xy取交集 兩個集合內相同的元素才會取出
    print(f"x 取 y 差集 {x - y}")  # x取y差集 (若 x 內有 y 集合內的元素，將其刪除)
    print(f"y 取 x 差集 {y - x}")  # y取x差集 (若 y 內有 x 集合內的元素，將其刪除)
    print(f"x y 取對稱差集 {x ^ y}")  # 對稱差集 = xy聯集 - xy交集

    # 判斷子集合
    print(x > z)  # a. 判斷 z 是否為 x 的子集合
    print(z.issubset(x))  # b. 判斷 z 是否為 x 的子集合(函式)
    print(x < z)  # 判斷 x 是否為 z 的子集合

    # 判斷超集合(較大的集合)
    print(x.issuperset(z))  # 判斷 x 是否為 z 的超集合(等效z為x的子集合)


if __name__ == "__main__":
    list_sorting()
    remove_duplicates()
    set_operations()
