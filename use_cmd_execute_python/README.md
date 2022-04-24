**以cmd形式呼叫Python檔案**

在指定的資料夾路徑欄位中輸入 cmd 呼叫windows的命令提示字元

目的是可以直接開啟指向該路徑的命令提示字元，不須再cd 到指定路徑

接下來輸入指令來調用main.py 

main.py需要輸入一個參數， 而main.py會幫你把輸入的參數列印出來，有兩種調用方式

`py main.py “隨便一個參數"`

`python main.py “隨便一個參數"`

執行後會印出三行

第一行為 sys.argv[0] 印出執行檔案的檔案名稱
第三行為 sys.argv[1] 你填入的參數，印出來的結果

