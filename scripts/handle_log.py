# -*- coding: utf-8 -*-
"""
------------------------------------
@Time    : 2020/7/4 20:09
@Author  : Destiny
@FileName: handle_log.py
@Software: PyCharm
------------------------------------
"""
import os
import logging

from scripts.handle_config import do_config
from scripts.constants import Log_Dir

class HandleLog:
    """
    日志处理类
    """

    def __init__(self):
        # 1.定义日志收集器
        self.case_logger = logging.getLogger(do_config.get_value("log", "logger_name"))

        # 2.指定日志收集器的日志等级
        self.case_logger.setLevel(do_config.get_value("log", "logger_level"))

        # 3.定义日志输出渠道
        # 输出到控制台
        console_handle = logging.StreamHandler()
        # 输出到文件
        file_handle = logging.FileHandler(os.path.join(Log_Dir, do_config.get_value("log", "log_filename")),
                                          encoding="utf-8")

        # 4.定义日志输出渠道的日志等级
        console_handle.setLevel(do_config.get_value("log", "console_level"))
        file_handle.setLevel(do_config.get_value("log", "file_level"))

        # 5.定义日志显示的格式
        simple_formatter = logging.Formatter(do_config.get_value("log", "simple_formatter"))
        verbose_formatter = logging.Formatter(do_config.get_value("log", "verbose_formatter"))

        # 控制台显示简单的日志
        console_handle.setFormatter(simple_formatter)
        # 日志文件中显示详细的日志
        file_handle.setFormatter(verbose_formatter)

    def get_logger(self):
        """
        获取logger日志器对象
        :return:
        """
        return self.case_logger


do_logger = HandleLog().get_logger()

if __name__ == '__main__':

    do_logger.debug("这是一个debug级别的日志")  # 手动记录日志
    do_logger.info("这是一个info级别的日志")
    do_logger.warning("这是一个warning级别的日志")
    do_logger.error("这是一个error级别的日志")
    do_logger.critical("这是一个critical级别的日志")
    pass