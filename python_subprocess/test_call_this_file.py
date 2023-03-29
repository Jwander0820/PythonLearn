import sys
from time import sleep


def main():
    print("call me maybe")
    sleep(1)
    list_of_args = sys.argv  # 本質是一個清單 第[0]位是執行檔案的檔名(main.py)
    arg1 = list_of_args[1]  # 取出第一個參數
    arg2 = list_of_args[2]  # 取出第一個參數
    print(f"first arg = {arg1}")
    print(f"second arg = {arg2}")


if __name__ == "__main__":
    main()
