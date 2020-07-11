# -*- coding: utf-8 -*-
"""
------------------------------------
@Time    : 2019/8/6 17:23
@Author  : Destiny
@FileName: runner.py
@Software: PyCharm
------------------------------------
"""
import unittest
from datetime import datetime
from libs.HTMLTestRunnerNew import HTMLTestRunner
from scripts.constants import Test_Case, Report_Dir


suite = unittest.defaultTestLoader.discover(Test_Case)
now_time = datetime.strftime(datetime.now(), "%Y%m%d%H%M%S")
test_report = Report_Dir + '/' + "report_" + now_time + ".html"
with open(test_report, mode="wb") as report:
    runner = HTMLTestRunner(stream=report,
                            verbosity=2,
                            title="小天测试报告",
                            description="接口测试",
                            tester="小天")
    runner.run(suite)



