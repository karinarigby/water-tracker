# config.py

# Enable Flask's debugging features. Should be False in production


class Config(object):
    """
    Common configurations across all environments
    """

    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False

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
