import os
import shutil

if __name__ == "__main__":
    # os.system()，執行shell命令，呼叫出計算機
    cmd = "calc"
    os.system(cmd)

    # os.path.exists()、shutil.rmtree()
    # 如果資料夾路徑不存在，建立一個該資料夾(可以建立多層次資料夾)
    test_create_folder_path = "./test_create_folder/inner_folder"
    if not os.path.exists(test_create_folder_path):
        print("檔案路徑不存在")
        os.makedirs(test_create_folder_path) # 如果路徑不存在，建立資料夾

        # 判斷檔案路徑是否存在
        if os.path.exists(test_create_folder_path):
            print("資料夾路徑存在")

        # 而shutil可以清空刪除整個資料夾
        # os.remove 可以移除指定檔案，但好像有限制，不能刪除其他槽的資料，且只能刪除檔案不能刪除資料夾
        try:
            shutil.rmtree(test_create_folder_path)
        except OSError as e:
            print(e)
        else:
            print(f"成功刪除資料夾{test_create_folder_path}")

    # os.listdir()
    # 讀取資料夾內所有資料，也可以單獨提取某類型資料
    folder_path = r"./test_folder"
    load_files = os.listdir(folder_path)
    for file in load_files:
        print(file)
        # 檢測若file檔名包含.py，則可以單獨取出來，用於提取指定類型檔名很有用
        if '.py' in file:
            print(f"這是一個python檔案 {file}")

    # os.path.basename()
    # 從檔案路徑中提取出完整檔名(含副檔名)
    file_path = r"./test_folder/Lenna_(test_image).png"
    # basename 會是 "書名.tif"，[0]是書名 [1]是檔案類型(.tif)
    basename = os.path.basename(file_path)
    print(basename)
    # 透過splitext分隔符號從basename中提取出書名
    file_name = os.path.splitext(basename)[0]
    file_name_extension = os.path.splitext(basename)[1]
    print(file_name)
    print(file_name_extension)

    # os.rename()、os.renames()
    # os 將檔案重新命名
    old_file_name = "./os_rename_test/os_rename.txt"
    new_file_name = "./os_rename_test/os_new_name.py"
    os.rename(old_file_name, new_file_name)
    print(os.listdir("./os_rename_test/"))
    os.rename(new_file_name, old_file_name) # 命名回來==


    # shutil.move()
    # 搬移檔案至指定區域(資料夾)，搬移檔案可以順便重新命名
    test_move_file = "./test_move_file.txt"
    target_path = "./test_create_folder/test_move_file_rename.txt"
    shutil.move(test_move_file, target_path) # 搬移檔案
    folder_path = "./test_create_folder"
    load_files = os.listdir(folder_path) # 測試看看有沒有搬移到指定資料夾
    for file in load_files:
        print(file)
    shutil.move(target_path, test_move_file) # 搬回來==

    # os.path.split()
    # 把路徑分割成 dirname 和 basename，返回一個元組
    x = os.path.split('./test_folder/Lenna_(test_image).png')
    print(x)

