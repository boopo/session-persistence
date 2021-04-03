import logging
import time

import requests
from flask import request, abort, g

from App.ext import redis_client


def login_required(fun):
    def wrapper(*args, **kwargs):
        username = request.headers.get('username')
        password = request.headers.get('password')
        if not username or not password:
            abort(401)
        g.username = username
        g.password = password
        return fun(*args, **kwargs)

    return wrapper


class CheckAndUpdate():
    def __init__(self, username):
        self.username = username

    # 验证融合门户 cookie
    def check_portal_cookie(self):
        if redis_client.get(self.username):
            url = 'http://portal.cumt.edu.cn/portal/api/v1/api/http/8'
            header = {
                "Cookie": str(redis_client.get(self.username), encoding='utf-8')
            }
            r = requests.get(url=url, headers=header)
            if r.text.__sizeof__() >= 1000:  # 正确 432 错误 75044
                return False
            else:
                return True
        else:
            logging.info("无jess" + str(self.username))
            return False

    # 验证教务系统cookie
    def check_jwxt_cookie(self):
        if redis_client.get("j" + self.username):
            url = 'http://jwxt.cumt.edu.cn/jwglxt/xtgl/index_cxYhxxIndex.html?xt=jw'
            header = {
                "Cookie": str(redis_client.get("j" + self.username), encoding='utf-8')
            }
            r = requests.get(url=url, headers=header)
            if r.text.__sizeof__() >= 5000:  # 正确返回1336 错误返回34002
                return False
            else:
                return True
        else:
            logging.info("无jwxt" + str(self.username))
            return False

    # 验证一卡通cookie
    def check_card_cookie(self):
        if redis_client.get("y" + self.username):
            url = 'http://ykt.cumt.edu.cn/User/GetCardInfo'
            header = {
                "Cookie": str(redis_client.get("y" + self.username), encoding='utf-8')
            }
            r = requests.post(url=url, headers=header)
            if r.text.__sizeof__() >= 8888:  # 正确 2020 错误 53642
                return False
            else:
                return True
        else:
            logging.info("无cook" + str(self.username))
            return False

    # 验证图书馆cookie
    def check_lib_cookie(self):
        if redis_client.get("l" + self.username):
            url = 'https://findcumt.libsp.com/find/userInfo/getUserInfo'

            jwt = str(redis_client.get("l" + self.username), encoding='utf-8')
            header = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36",
                "jwtOpacAuth": jwt
            }
            r = requests.get(url=url, headers=header)
            if r.text.__sizeof__() <= 1000:  # 正确2726  错误 181
                return False
            else:
                return True
        else:
            logging.info("无jwt"+str(self.username))
            return False

    # 验证验证码
    def check_captcha(self):
        url = 'http://authserver.cumt.edu.cn/authserver/checkNeedCaptcha.htl?username=' + self.username + '&_=' + str(
            int(time.time()))
        r = requests.get(url=url)
        if 'true' in r.text:
            return True
        else:
            return False

    def get_portal_cookie(self):
        cookie = str(redis_client.get(self.username), encoding='utf-8')
        return cookie

    def get_jwxt_cookie(self):
        cookie = str(redis_client.get("j" + self.username), encoding='utf-8')
        return cookie

    def get_card_cookie(self):
        cookie = str(redis_client.get("y" + self.username), encoding='utf-8')
        return cookie

    def get_lib_cookie(self):
        cookie = str(redis_client.get("l" + self.username), encoding='utf-8')
        return cookie
