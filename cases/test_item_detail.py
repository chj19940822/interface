# -*- coding: utf-8 -*-
"""
------------------------------------
@Time    : 2020/7/5 11:07
@Author  : Destiny
@FileName: test_login.py
@Software: PyCharm
------------------------------------
"""
import unittest
import json
import logging
from libs.ddt import ddt, data
from scripts.handle_request import HandleRequest
from scripts.handle_mysql import HandleMysql
from scripts.handle_excel import HandleExcel
from scripts.handle_log import do_logger
from scripts.constants import Datas_File_Path
from scripts.handle_context import *

do_excel = HandleExcel(Datas_File_Path, "direct-page")
cases =do_excel.get_cases()


@ddt
class TestCreateDirectPage(unittest.TestCase):
    """
    登录接口
    """

    @classmethod
    def setUpClass(cls):
        cls.send_request = HandleRequest()  # 创建HttpRequest对象
        cls.send_mysql = HandleMysql()   # 创建HandleMysql对象
        do_logger.info("\n{:=^40s}".format("开始执行登录接口用例"))

    @classmethod
    def tearDownClass(cls):
        cls.send_request.close()  # 关闭request会话
        cls.send_mysql.close()  # 关闭mysql连接
        do_logger.info("\n{:=^40s}".format("结束执行登录接口用例"))

    @data(*cases)
    def create_direct_page(self, case):
        """
        创建下单页
        :param case:
        :return:
        """

        logging.captureWarnings(True)
        new_data = HandleContext.item(case['data'])
        url = do_config.get_value("test", "test_hall") + case['url'] + new_data
        print(url)
        res = HandleRequest().to_request(url, method="get", verify=False)

        case_id = case['case_id']
        expect_reuslt = case['expected']
        msg = '测试' + case['title']
        success_msg = do_config.get_value("msg", "success_result")
        fail_msg = do_config.get_value("msg", "fail_result")
        try:
                self.assertIn(expect_reuslt, res.text, msg=msg)
                do_excel.write_result(case_id + 1, res.text, success_msg)
                do_logger.debug("{},执行结果为:{}".format(msg, success_msg))
        except AssertionError as e:
            do_excel.write_result(case_id+1, res.text, fail_msg)
            do_logger.debug("{},执行结果为:{},具体异常为:{}".format(msg, fail_msg, e))
            raise e


if __name__ == '__main__':
    unittest.main()
    pass





