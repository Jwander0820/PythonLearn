import configparser
import os


def read_config_file(file_path: str):
    cf = configparser.ConfigParser()
    cf.read(file_path)

    return cf


def extract_config_data(cf: configparser.ConfigParser):
    secs = cf.sections()
    print(secs)

    options = cf.options("user1")
    print(options)

    items = cf.items("user1")
    print(items)

    name = cf.get("user1", "user_name")
    print(name)


class ReadConfig:
    @staticmethod
    def get_data(file_path: str, key: str, value: str):
        if os.path.exists(file_path):
            config = configparser.ConfigParser()
            config.read(file_path, encoding='UTF-8')
            return config.get(key, value)
        else:
            print("file is not exist")


def main():
    config_file = "config.ini"

    config = read_config_file(config_file)
    extract_config_data(config)

    module = ReadConfig.get_data(config_file, "user1", "user_name")
    print(module)

    config = configparser.ConfigParser()
    config.read(config_file)
    main_config = config["user1"]
    print(main_config)

    main_config = dict(main_config)
    print(main_config)

    for key, value in main_config.items():
        print(key, value)


if __name__ == '__main__':
    main()
