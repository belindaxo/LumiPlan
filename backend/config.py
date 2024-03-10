import os

class Config:
    DEBUG = False
    TESTING = False
    MONGO_URI = os.getenv('MONGO_URI', 'mongodb+srv://belindaxo:v2jaVeyap7zF@lumiplan.bpe9jda.mongodb.net/')

class DevelopmentConfig(Config):
    DEBUG = True
    pass

class TestingConfig(Config):
    TESTING = True
    MONGO_URI = os.getenv('TEST_MONGO_URI', 'mongodb+srv://bmdebruyn:F5owwjaBxehm5KNc@testing.prybgh5.mongodb.net/')

class ProductionConfig(Config):
    pass
