# -*- coding: utf-8 -*-

""" 
隱藏的變數名稱 __name__ ，若是在原始檔案下則會印出 __main__
若是被其他檔案引用的情況下，__name__ 會變成本檔案名稱 cool
範例可以參考other cool.py的執行結果
如此一來，本檔案被其他檔案引用時，下面的 if...就不會觸發執行條件
這樣的好處是 
1. 若是要測試函式能否正常執行，直接寫在該if區塊即可，不需要另外開檔案
2. 完成函式後也不必刪除該測試區塊，因為被其他檔案引用時不會觸發執行條件
3. 如果寫一個大的程式，且要call很多function，if __name__ == '__main__' 絕對是你的好碰油
"""


def cool_func():
    print('cool_func(): Super Cool!')


if __name__ == '__main__':
    print('Call it locally')
    cool_func()

print('__name__ = ', __name__)

if __name__ == 'cool':
    print('如果name為cool的話，列印出 Oh My God ')
    print('Oh My God')
