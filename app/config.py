from instance.config import MUSIC_API_KEY
import os

class Config:
    '''
    General configuration parent class
    '''
    MUSIC_API_BASE_URL ='https://api.spotify.com/v1'



class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL","")
    if SQLALCHEMY_DATABASE_URI.startswith("postgres://"):
        SQLALCHEMY_DATABASE_URI =SQLALCHEMY_DATABASE_URI.replace("postgres://","postgresql://",1)


class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL","")
    DEBUG = True



config_options = {
    'development':DevConfig,
    'production':ProdConfig
    }   