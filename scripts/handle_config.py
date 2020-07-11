# -*- coding: utf-8 -*-
"""
------------------------------------
@Time    : 2020/7/4 19:14
@Author  : Destiny
@FileName: handle_config.py
@Software: PyCharm
------------------------------------
"""
from configparser import ConfigParser

from scripts.constants import Config_File_Path

class HandleConfig:
    """
    处理配置文件
    """
    def __init__(self, filename):
        self.filename = filename
        self.config = ConfigParser()
        self.config.read(self.filename, encoding="utf-8")

    def get_value(self, section, option):
        return self.config.get(section, option)

    def get_int(self, section, option):
        return self.config.getint(section, option)

    def get_float(self, section, option):
        return self.config.getfloat(section, option)

    def get_boolean(self, section, option):
        return self.config.getboolean(section, option)

    def get_eval_data(self, section, option):
        return eval(self.config.get(section, option))

    @staticmethod
    def write_configo(data, filename):
        if isinstance(data, dict):
            for value in data.values():
                if not isinstance(value.dict):
                    return "数据不合法"

            config = ConfigParser()
            for key in data:
                config[key] = data[key]
            with open(filename, "w") as file:
                config.write(file)


do_config = HandleConfig(Config_File_Path)

if __name__ == '__main__':
    pass