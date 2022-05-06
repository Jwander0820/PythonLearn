import os

dir_path = r".."
for root, dirs, files in os.walk(dir_path, topdown=False):
    for name in files:  # 取得路徑下所有檔案
        print(os.path.join(root, name))
    for name in dirs:  # 取得路徑下所有資料夾
        print(os.path.join(root, name))
