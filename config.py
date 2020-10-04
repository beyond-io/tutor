class Config(object):
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:tutor@localhost:5432/tutor'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'secretkey'


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class TestingConfig(Config):
    TESTING = True
    WTF_CSRF_ENABLED = False
