import os
import glob

"""
1. os.walk();他會讀取整個資料夾內所有子資料夾與其文件

# topdown預設為True，代表會先走訪最頂層資料夾的文件，處理完才會走訪內層的子資料夾
# 若是設為False，則會依照命名的順序，直接完整走訪完一個子資料夾後才會往下繼續走訪子資料夾，兩者差再提取的順序，
# os.walk 可以按照深度優先的順序遍歷整個資料夾，並且當它遍歷到一個新的(子)資料夾時候會產生一個 3 個元素的元組
# (dirpath, dirname, filenames)，這其中也包括最高階別的給定資料夾本身。
"""
hash_database_path = ".."  # 提取上一層的資料夾

# os.walk() 提取出來為生成器的形式，需要透過for迴圈來提取
x = os.walk(hash_database_path, topdown=False)
print(type(x))
for root, dirs, files in os.walk(hash_database_path, topdown=False):
    # root 表示根目錄
    # dirs 表示該文件下的子目錄名清單(list)
    # files表示該資料夾下的文件清單(list)
    for file_name in files:  # 針對檔名做提取
        file_path = os.path.join(root, file_name)
        # print(file_path)
        # file_path印出來會包含子資料夾內所有資料，所以會較亂
        # 可以透過指定路徑限縮提取的範圍

        if "python-if__name__explain" in file_path:
            print(file_path)

"""
2. os.listdir();返回指定路徑下的文件和資料夾列表

# 此種方法僅為返回一層的文件清單，同時也不會篩選出資料夾與文件，就是單純的提取出檔案名稱
# 適合輕度使用，若要完整搜尋檔案不建議使用該方法
"""
dirs = os.listdir("../python-if__name__explain")
# 輸出所有資料夾和文件
for file in dirs:
    print(file)

"""
3. glob.glob();返回結果是匹配給定模式的帶完整路徑的檔名

# glob 模組是按照給定的檔案的模式來去匹配資料夾中的內容，模式遵循的是 Unix shell 中的規則。
# glob.glob 返回結果是匹配給定模式的帶"完整路徑的檔名"。
# 我們需要查詢的是所有檔案，它們符合的命名模式是*.*，這裡萬用字元*匹配的是任意長度的字串。

# 此方法彈性高，也可以透過萬用字元更細節的檔案，但需要注意
# glob.glob 方法不能保證列出來的所有結果都是檔案，因為它只是檢查路徑名符不符合給定的模式，但它不檢查它到底是一個資料夾還是一個資料夾。
# 比如，假如一個資料夾的名字是 test.test，它也符合*.*模式，那這個資料夾也會在結果中出現。
# 假如你需要確保輸出結果只包含檔案的話，需要用 os.path.isfile 函式來驗證。
"""
result = glob.glob("../*/*")
for file in result:
    print(file)
