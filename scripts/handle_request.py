# -*- coding: utf-8 -*-
"""
------------------------------------
@Time    : 2020/6/27 16:49
@Author  : Destiny
@FileName: handle_request.py
@Software: PyCharm
------------------------------------
"""
import json
import requests
import logging

class HandleRequest:
    """
定义接口测试方法
    """
    def __init__(self):
        self.one_session =requests.Session()

    def to_request(self, url, method="post", data=None, is_json=False, verify=None):
        # if isinstance(data ,str):
        #     try:
        #         data =json.loads(data)
        #     except Exception as e:
        #     #使用日志器来记录日志
        #     do_
        method = method.lower()
        if method == "get":
            res = self.one_session.get(url, params=data, verify=False)
        elif method == "post":
            if is_json:
                res = self.one_session.post(url, json=data, verify=False)
            else:
                res = self.one_session.post(url, data=data, verify=False)
        else:
            res = None
        return res

    def close(self):
        self.one_session.close()



if __name__ == '__main__':
    logging.captureWarnings(True)
    url = "https://login.test.zcygov.cn"
    data ={
    "loginType":"password",
    "username":"alixhcgdw",
    "password":"zcy123456"
}
    do_request = HandleRequest()

    response = do_request.to_request(url, method="post", data=data, verify=False)
    print(response)

    url1 = "https://www.test.zcygov.cn/front/detail/item/176617302"
    response1 = do_request.to_request(url1, method="get", verify=False)
    print(response1.text)

    pass


