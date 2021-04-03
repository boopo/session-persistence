from App.apis.session import session_api, test_api


def init_api(app):
    session_api.init_app(app)
    test_api.init_app(app)

