from decouple import config


class Config:
    SECRET_KEY = 'llaveprovisional'


class DelevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///temporizador.sqlite3'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


config = {
    'development': DelevelopmentConfig,
    'default': DelevelopmentConfig
}
