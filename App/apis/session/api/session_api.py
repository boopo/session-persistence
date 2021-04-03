from flask_restful import Resource, reqparse

from App.apis.session.utils.utils_check import CheckAndUpdate
from App.apis.session.utils.utils_login import newIds

parse_initial = reqparse.RequestParser()
parse_initial.add_argument("username", type=str, help='请输入用户名', required=True, location=['json'])
parse_initial.add_argument("password", type=str, help='请输入密码', required=True, location=['json'])


class Initialization(Resource):
    def post(self):
        args = parse_initial.parse_args()
        username = args.get("username")
        password = args.get("password")
        try:
            user = newIds(username, password)
            user.login()
            return "ok", 200
        except:
            return "null", 400


class Portal(Resource):
    def post(self):
        args = parse_initial.parse_args()
        username = args.get("username")
        password = args.get("password")
        try:
            user_id = CheckAndUpdate(username)
            if not user_id.check_portal_cookie():
                user = newIds(username, password)
                user.login()
            return user_id.get_portal_cookie()
        except:
            return "null", 400


class Jwxt(Resource):
    def post(self):
        args = parse_initial.parse_args()
        username = args.get("username")
        password = args.get("password")
        try:
            user_id = CheckAndUpdate(username)
            if not user_id.check_jwxt_cookie():
                user = newIds(username, password)
                user.login_with_jwxt()
            return user_id.get_jwxt_cookie()
        except:
            return "null", 400


class Card(Resource):
    def post(self):
        args = parse_initial.parse_args()
        username = args.get("username")
        password = args.get("password")
        try:
            user_id = CheckAndUpdate(username)
            if not user_id.check_card_cookie():
                user = newIds(username, password)
                user.login_with_card()
            return user_id.get_card_cookie()
        except:
            return "null", 400


class Book(Resource):
    def post(self):
        args = parse_initial.parse_args()
        username = args.get("username")
        password = args.get("password")
        try:
            user_id = CheckAndUpdate(username)
            if not user_id.check_lib_cookie():
                user = newIds(username, password)
                user.login_with_lib()
            return user_id.get_lib_cookie()
        except:
            return "null", 400
class Test(Resource):
    def get(self):
        return "hello,my son!"
