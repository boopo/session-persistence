from flask_redis import FlaskRedis

redis_client = FlaskRedis()
def init_ext(app):
    redis_client.init_app(app)
