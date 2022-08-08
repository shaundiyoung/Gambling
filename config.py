
class config(object):
    SECRET_KEY = "81346y5028560834yv08we4yt082480u5y043986y0834y6vhdfugjghszjkdfbi$%^&&HVBFOIUBgiodvubVBKUBVPIOUHBPiouhHIUHHWPhbpipunsipbndgv"

class prodConfig(config):
    DATABASE_URI = 'To be decided'

class devConfig(config):
    DATABASE_URI = "sqlite:///temp/data.db"

class testingConfig(config):
    DATABASE_URI = 'sqlite:///:memory:'