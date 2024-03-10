import os

class Config:
    DEBUG = False
    TESTING = False
    MONGO_URI = os.getenv('MONGO_URI', 'mongodb+srv://belindaxo:ORspxgwlgUOxeTWx@lumiplan.bpe9jda.mongodb.net/db')

class DevelopmentConfig(Config):
    DEBUG = True
    pass

class TestingConfig(Config):
    TESTING = True
    MONGO_URI = os.getenv('TEST_MONGO_URI', 'mongodb+srv://belindaxo:ORspxgwlgUOxeTWx@lumiplan.bpe9jda.mongodb.net/db')

class ProductionConfig(Config):
    pass
