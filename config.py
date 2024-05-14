from decouple import config 

class Config:
    SECRET_KEY = '4^3YcK5rnQg96^Cm'

class DevelopmentConfig(Config):
    DEBUG = True
    MYSQL_HOST = "localhost"
    MYSQL_USER = "root"
    #MYSQL_PASSWORD = "123456" 
    MYSQL_DB = "tienda"
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = 'josuealcantara251@gmail.com'
    MAIL_PASSWORD = config('MAIL_PASSWORD')

config = {
    'development': DevelopmentConfig,
    'default': DevelopmentConfig
}