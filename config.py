import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = 'martinmaina'

class ProductionConfig(Config):
    DEBUG = False

class StagingConfig(COnfig):
    DEVELOPMENT = True
    DEBUG = True



class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class TestingConfig(Config):
    TESTING = True
