import configparser
import os

cf = configparser.ConfigParser()
cf.read("config.ini")  # 讀取配置文件

secs = cf.sections()  # 提取文件中所有的section(一個配置文件中可以有多個配置)
print(secs)

options = cf.options("user1")  # 提取某個section名為user1所對應的鍵
print(options)

items = cf.items("user1")  # 提取section名為user1所對應的全部鍵與其值
print(items)

name = cf.get("user1", "user_name")  # 提取user1中user_name對應的值
print(name)


class ReadConfig:
    @staticmethod
    def get_data(key, value):
        config_path = r"config.ini"
        if os.path.exists(config_path) is True:
            config = configparser.ConfigParser()
            config.read(config_path, encoding='UTF-8')
            return config.get(key, value)
        else:
            print("file is not exist")


if __name__ == '__main__':
    module = ReadConfig().get_data("user1", "user_name")
    print(module)

    config = configparser.ConfigParser()
    config.read("config.ini")  # 讀取配置文件config
    main_config = config["user1"]  # 儲存main section下的config設定
    print(main_config)
    main_config = dict(main_config)  # 可以轉成字典
    print(main_config)
    for key, value in main_config.items():  # items 取key, value
        print(key, value)
