import glob
import os

def replace_file_name(path, replaced_text, new_text):
    for root, dirs, files in os.walk(path, topdown=False):  # 取得路徑下所有檔案的根目錄與檔名
        for file_name in files:  # 循序讀取檔名清單
            if replaced_text in file_name:  # 若指定要替換的文字有在檔名中
                new_file_name = file_name.replace(replaced_text, new_text)  # 將其替換成新的檔名
                os.rename(os.path.join(root, file_name), os.path.join(root, new_file_name))  # 重新命名
                # print(file_name)
                # print(new_file_name)


if __name__ == "__main__":
    _path = f'./custom_dataset'
    _replaced_text = "道教的奧秘(燈籠魚)_內文掃描檔"
    _new_text = "The_Mystery_of_Taoism"
    replace_file_name(_path, _replaced_text, _new_text)
