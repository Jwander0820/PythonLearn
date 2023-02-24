import subprocess


def subprocess_call_exe():
    """
    subprocess呼叫執行exe
    'your_executable.exe' 放入需要執行的exe
    """
    cwd = "./"  # 設定工作目錄，工作目錄會影響寫入或讀取相對路徑的判斷
    subprocess.Popen(['calc.exe'], cwd=cwd,
                     creationflags=subprocess.CREATE_NEW_CONSOLE)  # 此設定為新開啟一個console


def subprocess_call_py():
    """
    subprocess呼叫執行py
    """
    # 1. env可以設定指向venv虛擬環境
    # 2. 若設為python則直接引用系統環境
    env = r"python"
    # 呼叫指定的python檔案
    call = r"./test_call_this_file.py"
    # 可以帶入初始傳入的參數
    arg1 = "test_arg1"
    arg2 = "test_arg2"
    # 設定工作目錄，工作目錄會影響寫入或讀取相對路徑的判斷
    cwd = r"./"

    # 輸入參數 # cmd第一行沒有加python的話，預設是會當前的環境變數
    cmd_input = [env, call, arg1, arg2]
    # subprocess.run會將另一個程式產出的東西回傳回來(CompletedProcess)，包含了命令的輸出信息，方便使用者查看和處理
    # 如果需要捕獲子程式的輸出，可以使用 stdout=subprocess.PIPE參數將子程式的輸出捕獲。
    result = subprocess.run(cmd_input, shell=False, cwd=cwd, stdout=subprocess.PIPE)
    output = result.stdout.decode('utf-8')  # 將捕獲的字節流(print)轉換為 Unicode 字符串。
    print(output)

    # subprocess.call則會直接將print、log相關直接輸出在呼叫的程式中，結束只會回傳狀態，無法再進一步處理
    result = subprocess.call(cmd_input, shell=False, cwd=cwd)
    print(result)  # 回傳結束狀態整數值，通常是 0 表示成功，非 0 則表示失敗

    """
    1. subprocess shell參數解釋
    在 subprocess.run 函數中，shell 參數用於指示是否將命令作為字符串傳遞給系統的 shell 進程執行。
    當 shell=False 時，args 應該是一個可調用對象（通常是一個列表），該對象的第一個元素是命令名，後面的元素是命令行參數。
    在這種情況下，subprocess.run 函數將直接執行該命令，而不需要使用 shell 進程。這種方式更加安全，因為它可以避免一些潛在的安全問題，例如 shell 注入攻擊。

    當 shell=True 時，args 應該是一個字符串，包含要執行的完整命令行。在這種情況下，subprocess.run 函數將使用默認的 shell
    （通常是 /bin/sh 或者 cmd.exe）執行該命令。使用 shell 模式可能會導致一些安全問題，因為它允許用戶執行任意的 shell 命令。

    因此，如果您想要執行一個簡單的命令，那麼最好將 shell 參數設置為 False，將命令及其參數分別傳遞給 subprocess.run 函數。
    如果您需要執行更複雜的命令或 shell 腳本，則可能需要將 shell 參數設置為 True。但請注意，這可能會帶來一些安全風險。
    
    2. subprocess.run() 和 subprocess.call() 都是用來執行外部命令的 Python 模組，不過在使用上有一些差異：
    a.  subprocess.run() 是 Python 3.5 之後新增的
        而 subprocess.call() 則是 Python 2.4 就已經有了。
    b.  subprocess.run() 返回一個 CompletedProcess 對象，該對象包含了命令的輸出訊息，方便使用者查看和處理。
        而 subprocess.call() 則是返回一個代表結束狀態的整數值（通常是 0 表示成功，非 0 則表示失敗）。
    c.  subprocess.run() 可以接收一個 check 參數，如果設置為 True，則在命令返回非零的退出碼時，會自動引發 CalledProcessError 異常。
        而 subprocess.call() 則需要使用者自己處理退出碼和異常。
    d.  subprocess.run() 支持使用 capture_output 參數來捕獲命令的標準輸出和標準錯誤輸出。
        而 subprocess.call() 則需要使用者自己進行標準輸出和標準錯誤輸出的處理。
    總體來說，subprocess.run() 功能更強大，也更方便使用。如果你在 Python 3.5 以上的版本中，建議使用 subprocess.run()。如果需要在 Python 2.x 中使用，則可以使用 subprocess.call()。
    """


if __name__ == "__main__":
    subprocess_call_py()
