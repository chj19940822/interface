# -*- coding: utf-8 -*-
"""
------------------------------------
@Time    : 2020/7/4 19:15
@Author  : Destiny
@FileName: constants.py
@Software: PyCharm
------------------------------------
"""
import os

# 获取根目录路径
Base_Dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# config配置文件路径
Config_Dir = os.path.join(Base_Dir, "configs")
Config_File_Path = os.path.join(Config_Dir, "testcase.conf")

# testcase测试数据路径
Datas_Dir = os.path.join(Base_Dir, "datas")
Datas_File_Path = os.path.join(Datas_Dir, "cases.xlsx")

# 测试用例路径
Test_Case = os.path.join(Base_Dir, "cases")

# 测试报告路径
Report_Dir = os.path.join(Base_Dir, "reports")

# 日志文件所在目录路径
Log_Dir = os.path.join(Base_Dir, "logs")
