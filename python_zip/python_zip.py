# zip概念
x = [1, 2, 3, 4, 5, 6, 7]
y = [12, 1234, 1234, 1231, 123, 12, 324]
# zip生成一個可以被迭代的物件
# 返回一個元組迭代器，其中第i個元組包含每個引數序列或可迭代物件中的第i個元素。當最短的可迭代輸入耗盡時，迭代器將停止
zipped = zip(x, y)
for i in zipped:
    print(i)

zipped = dict(zipped) # 若先將zipped用for走訪完之後，再將zipped轉換成dict or list 會發現
print(zipped) # 印出來的是空值
# 是因為“zip對象” 是一个迭代器。 迭代器只能前進，不能後退。

# zip轉dict
zipped = dict(zip(x, y))
for i in zipped:
    print(f"key = {i}；value = {zipped[i]}")
    if zipped[i] == 1234: # 若資料為####則執行以下
        print(f"鍵值{i}的資料為{zipped[i]}")


# 字典迭代處理相關說明
for key in zipped.keys():  # 讀字典的鍵值，for迴圈讀取字典預設為讀鍵的形式(同keys())
    print(key)
for key in zipped:  # 同.keys()的用法
    print(key)
for value in zipped.values():  # 讀取字典的鍵對應的值，直接取值的方法
    print(value)
for key, value in zipped.items():  # 讀取出字典的鍵與值，並同時處理
    print(key, value)
