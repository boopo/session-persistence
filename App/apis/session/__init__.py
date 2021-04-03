from flask_restful import Api

from App.apis.session.api.session_api import Initialization, Jwxt, Card, Book, Portal, Test

session_api = Api(prefix="/session")

test_api = Api()

session_api.add_resource(Initialization, "/initialize")
session_api.add_resource(Portal, "/portal")
session_api.add_resource(Jwxt, "/jwxt")
session_api.add_resource(Card, "/card")
session_api.add_resource(Book, "/book")
test_api.add_resource(Test,"/test")