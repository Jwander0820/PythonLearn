import os
import logging
import datetime


class Log(object):
    """
    以類作為裝飾器，需要再類的__init__()方法中記錄傳入的函數
    再在__call__()調用修飾的函數及其他額外處理
    """
    def __init__(self, fn):
        # 初始化操作在此完成
        self.__fn = fn
        if not os.path.exists("./logs"):  # 若logs不存在，建立該資料夾
            os.makedirs("./logs")

        # 獲得log日誌紀錄器，設定日誌等級
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel('DEBUG')
        # 設定日誌格式
        formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s", datefmt="%Y-%m-%d %H:%M:%S")

        consoleHandler = logging.StreamHandler()  # 輸出到控制台的handler
        consoleHandler.setLevel(logging.DEBUG)  # 設定層級(控制台)
        consoleHandler.setFormatter(formatter)  # 設定日誌格式

        timestamp = datetime.datetime.now().strftime("%Y-%m-%d")
        fileHandler = logging.FileHandler(f"./logs/{timestamp}_test.log", 'a', 'utf-8')  # 輸出到.log的handler
        fileHandler.setLevel(logging.DEBUG)  # 設定層級(.log)
        fileHandler.setFormatter(formatter)  # 設定日誌格式

        # 日誌紀錄器增加此handler
        # 若handler為空，才會添加logger.handlers，避免添加一堆handler重複輸出log
        if not self.logger.handlers:
            self.logger.addHandler(fileHandler)
            self.logger.addHandler(consoleHandler)

    # 實現__call__方法，表示對象是一個可調用對象，可以像調用函數一樣進行調用。
    def __call__(self, *args, **kwargs):
        # 添加裝飾功能
        try:
            res = self.__fn(*args, **kwargs)
            self.logger.debug(f"func: {self.__fn.__name__} - input: {args, kwargs} -> output: {res}")
            return res
        except Exception as e:
            self.logger.error(f"func: {self.__fn.__name__} - error message: {e}", exc_info=True)
        # self.__fn()


@Log
def test_decorator():
    print("測試裝飾器")


if __name__ == "__main__":
    test_decorator()
