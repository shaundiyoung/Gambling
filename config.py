
class config(object):
    SECRET_KEY = "81346y5028560834yv08we4yt082480u5y043986y0834y6vhdfugjghszjkdfbi$%^&&HVBFOIUBgiodvubVBKUBVPIOUHBPiouhHIUHHWPhbpipunsipbndgv"

class prodConfig(config):
    DATABASE_URI = 'To be decided'

class devConfig(config):
    SQLALCHEMY_DATABASE_URI = "sqlite:///api/data.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    HOST = "0.0.0.0"
    DEBUG = True

class testingConfig(config):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'