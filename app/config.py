
class Config(object):
    DEBUG = True
    TESTING = False

class DevelopmentConfig(Config):
    SECRET_KEY = "this-is-a-super-secret-key"



config = {
    'development': DevelopmentConfig,
    'testing': DevelopmentConfig,
    'production': DevelopmentConfig
}



API_KEY = 'TmSNZluQ7ETcXbQdI5J0wkVHY'
API_KEY_SECRET = 'hUvGXUkxw1NHvCAK426OzwXRzdExpsgoSZB6OwzE3UQpeK6Fxj'
BEARER_TOKEN = 'AAAAAAAAAAAAAAAAAAAAAPZcXwEAAAAABFm0j0kay9Tbj5U5OTuch%2Bb%2BvTM%3DZUUFHG6IvCOaM5Z1AvtxfY5SnZbWtRLy7ir00RSKLhgyVrVj1c'
ACCESS_TOKEN = '1479118083352530946-xpUbHtz5a7yfYpgFM94DN6cN5jCzUY'
ACCESS_TOKEN_SECRET = 'jlPGMELHMMoIbN4n1bL1p60TtPc4OKmKU7vO4MCzLV0Pi'