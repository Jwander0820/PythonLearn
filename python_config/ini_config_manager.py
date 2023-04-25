import configparser
import os


class ConfigManager:
    def __init__(self, file_path: str):
        self.file_path = file_path
        self.config = configparser.ConfigParser()
        self.config.read(self.file_path, encoding='UTF-8')

    def get_sections(self):
        return self.config.sections()

    def get_options(self, section: str):
        return self.config.options(section)

    def get_items(self, section: str):
        return self.config.items(section)

    def get_value(self, section: str, option: str):
        return self.config.get(section, option)

    def set_value(self, section: str, option: str, value: str):
        if section not in self.config.sections():
            self.config.add_section(section)
        self.config.set(section, option, value)
        with open(self.file_path, 'w') as config_file:
            self.config.write(config_file)

    def remove_section(self, section: str):
        if section in self.config.sections():
            self.config.remove_section(section)
            with open(self.file_path, 'w') as config_file:
                self.config.write(config_file)


def main(config_file="config.ini"):
    config_manager = ConfigManager(config_file)

    print("Sections:", config_manager.get_sections())
    print("Options in user1:", config_manager.get_options("user1"))
    print("Items in user1:", config_manager.get_items("user1"))

    print("Value of user_name in user1:", config_manager.get_value("user1", "user_name"))

    # config_manager.set_value("user1", "new_option", "new_value")  # 新增一個項目
    # print("Added new option to user1:", config_manager.get_items("user1"))

    # config_manager.remove_section("user1")  # 刪除整個section
    # print("Removed user1 section. Current sections:", config_manager.get_sections())


if __name__ == '__main__':
    main()
