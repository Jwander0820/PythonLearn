import asyncio
import time


# 同步(Synchronous): 循序處理，接到一個任務後，需要等到它完成，才能繼續執行下一個任務。
# 非同步(Asynchronous): 平行處理，無需等待第一個任務完成，即可執行其它的任務，只要第一個任務完成了，就回來處理。

# 同步函數
def sync_print_word():
    print("Hello")
    time.sleep(1)
    print("World")


# 非同步函數
async def async_print_word():
    print("Hello")
    await asyncio.sleep(1)
    print("World")


# 執行同步函數並計算執行時間
def run_sync():
    start = time.time()
    sync_print_word()
    sync_print_word()
    sync_print_word()
    end = time.time()
    processing_time = end - start
    print(f"同步執行時間:{processing_time} 秒")


# 執行非同步函數並計算執行時間
async def run_async():
    start = time.time()
    await asyncio.gather(async_print_word(), async_print_word(), async_print_word())
    end = time.time()
    processing_time = end - start
    print(f"非同步處理執行時間:{processing_time} 秒")


# 主函數
def main():
    print("開始執行同步函數")
    run_sync()

    print("開始執行非同步函數")
    asyncio.run(run_async())


if __name__ == "__main__":
    main()
