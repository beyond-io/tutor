class Config(object):
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:tutor@localhost:5432/tutor'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'cec31195da474ae1235388ff67567ddf'


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True
