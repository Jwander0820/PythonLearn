import concurrent.futures
import time
from concurrent.futures import ThreadPoolExecutor


def thread_job(num):
    num = num ** num
    print(f"Child thread:{num}")
    time.sleep(1)


if __name__ == "__main__":
    param_list = []
    for i in range(10):
        param_list.append(i)

    thread_worker = 4
    start = time.time()
    with ThreadPoolExecutor(max_workers=thread_worker) as executor:
        # map僅接受單一參數，亦可以改用starmap可以接受多參數
        executor.map(thread_job, param_list)
    end = time.time()
    print(end - start)

    start = time.time()
    for i in range(10):
        thread_job(i)
    end = time.time()
    print(end - start)