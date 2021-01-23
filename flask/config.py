# config.py

# Enable Flask's debugging features. Should be False in production


class Config(object):
    """
    Common configurations across all environments
    """

    DEBUG = True
    # set below to true when you are using sqlachemy's event system. otherwise
    # disable because of significant cost
    # SQLALCHEMY_URI = 'mysql://root:GCMNAdb-9995@mysql:3306/gcmna'
    # SQLALCHEMY_DATABASE_URI = 'mysql://root:GCMNAdb-9995@mysql:3306/gcmna' # this should go to the docker container

    SQLALCHEMY_TRACK_MODIFICATIONS = False

# actually maybe I shouldn't add this to version control but whatever I'll fix it one day


class DevelopmentConfig(Config):
    """
    Development configurations
    """

    DEBUG = True
    SQLALCHEMY_ECHO = True
    NETWORK_LOCATION = "localhost:5000"


class ProductionConfig(Config):
    """
    Production configurations
    """

    DEBUG = False
    

class TestingConfig(Config):
    """
    Testing configurations
    """

    TESTING = True
    SQLALCHEMY_ECHO = False

app_config = {
    "development": DevelopmentConfig,
    "production": ProductionConfig,
    "default": DevelopmentConfig,
    "testing": TestingConfig,
}
