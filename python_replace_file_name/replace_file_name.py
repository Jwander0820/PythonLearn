import glob
import os


class ReplaceFileName:
    @staticmethod
    def replace_file_name(path, replaced_text, new_text):
        """
        使用指定字詞批量替換資料夾內的檔名
        :param path: 資料夾路徑
        :param replaced_text: 要被替換的字詞
        :param new_text: 替換成該字詞
        :return:
        """
        for root, dirs, files in os.walk(path, topdown=False):  # 取得路徑下所有檔案的根目錄與檔名
            for file_name in files:  # 循序讀取檔名清單
                if replaced_text in file_name:  # 若指定要替換的文字有在檔名中
                    new_file_name = file_name.replace(replaced_text, new_text)  # 將其替換成新的檔名
                    os.rename(os.path.join(root, file_name), os.path.join(root, new_file_name))  # 重新命名

    def add_prefix_suffix(self, path, detect_word=None, prefix_text=None, suffix_text=None):
        """
        在指定資料夾內，指定共通檔名 or 全資料夾內的檔案，統一添加前綴詞 or 後綴詞
        :param path: 資料夾路徑
        :param detect_word: 指定的檔名or字詞，若符合才執行添加前綴詞or後綴詞
        :param prefix_text: 要添加的前綴詞，會添加在檔案的最前方
        :param suffix_text: 要添加的後綴詞，會添加在副檔名的前方
        :return:
        """
        for root, dirs, files in os.walk(path, topdown=False):  # 取得路徑下所有檔案的根目錄與檔名
            for file_name in files:  # 循序讀取檔名清單
                if detect_word:  # 若有檢測字詞才會調用這行
                    if detect_word in file_name:  # 若指定要替換的文字有在檔名中
                        new_file_name = self._filename_add_prefix_suffix(file_name,
                                                                         prefix_text=prefix_text,
                                                                         suffix_text=suffix_text)
                        os.rename(os.path.join(root, file_name), os.path.join(root, new_file_name))  # 重新命名
                else:
                    new_file_name = self._filename_add_prefix_suffix(file_name,
                                                                     prefix_text=prefix_text,
                                                                     suffix_text=suffix_text)
                    os.rename(os.path.join(root, file_name), os.path.join(root, new_file_name))  # 重新命名

    def _filename_add_prefix_suffix(self, file_name, prefix_text=None, suffix_text=None):
        """
        添加前綴詞和後綴詞
        """
        if prefix_text:
            file_name = prefix_text + file_name
        if suffix_text:
            tmp_file_name = os.path.splitext(file_name)[0]
            tmp_file_extension = os.path.splitext(file_name)[1]
            file_name = f"{tmp_file_name}{suffix_text}{tmp_file_extension}"
        return file_name


if __name__ == "__main__":
    _path = f'./custom_dataset'
    _replaced_text = "道教的奧秘(燈籠魚)_內文掃描檔"
    _new_text = "The_Mystery_of_Taoism"
    # 替換資料夾內指定字詞
    replace_file_name(_path, _replaced_text, _new_text)

    # 將資料夾內所有檔案 or 指定字詞的檔案，統一添加前綴詞或後綴詞
    # ReplaceFileName().add_prefix_suffix(_path, prefix_text="這是前綴", suffix_text="這是後綴")
