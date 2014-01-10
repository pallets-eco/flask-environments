from flask.ext.environments import BaseConfig as Config

class Development(Config):
    DEBUG = True
    DATABASE = 'development_db'


class Staging(Config):
    DATABASE = 'staging_db'


class Production(Config):
    DATABASE = 'production_db'


class Testing(Config):
    TESTING = True
    DATABASE = 'testing_db'
