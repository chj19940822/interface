# -*- coding: utf-8 -*-
"""
------------------------------------
@Time    : 2020/7/5 11:18
@Author  : Destiny
@FileName: handle_context.py
@Software: PyCharm
------------------------------------
"""
import re
from scripts.handle_config import do_config


class HandleContext:
    """

    """
    test_purchaser_username = r"\${test_purchaser_username}"
    test_itemid = r"\${test_itemid}"
    test_skuid = r"\${test_skuid}"



    @classmethod
    def purchasername(cls, data):
       if re.search(cls.test_purchaser_username, data):
            purchasername = do_config.get_value("test", "test_purchaser_username")
            data = re.sub(cls.test_purchaser_username, purchasername, data)
       return data


    @classmethod
    def purchaser_username(cls, data):
        """
        用户名参数化
        :param data:
        :return:
        """
        if re.search(cls.test_purchaser_username, data):
            username = do_config.get_value("test", "test_purchaser_username")
            data = re.sub(cls.test_purchaser_username, username, data)
        return data


    @classmethod
    def item(cls, data):
        """
        商品详情页接口itemid参数化
        :param data:
        :return:
        """
        if re.search(cls.test_itemid, data):
            item_id = do_config.get_value("test", "test_itemid")
            data = re.sub(cls.test_itemid, item_id, data)
        return data

    @classmethod
    def skuid(cls, data):
        """
        商品skuid参数化
        :param data:
        :return:
        """
        if re.search(cls.test_skuid, data):
            sku_id = do_config.get_value("test", "test_skuid")
            data = re.sub(cls.test_skuid, sku_id, data)
        return data



if __name__ == '__main__':
    str ='{"loginType":"password","username":"${test_purchaser_username}","password":"zcy123456"}'
    print(HandleContext.username(str))
    pass