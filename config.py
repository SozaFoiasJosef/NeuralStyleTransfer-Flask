import os

basedir = os.path.abspath(os.path.dirname(__file__))

UPLOAD_FOLDER = 'C:/Users/Josef/Desktop/CSC210/Project2/app/static'

ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}
class Config:
    
    @staticmethod
    def init_app(app):
        app.config["SESSION_PERMANENT"] = False
        app.config["DEBUG"] = True
        app.config["SESSION_TYPE"] = "filesystem"
        app.config["SECRET_KEY"] = "hard to guess string"
        app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(basedir, "data.sqlite")
        app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

        
class DevelopmentConfig(Config):
    #development initialization
    DEBUG = True

class TestingConfig(Config):
    #testing initialization
    TESTING = True
    
class ProductionConfig(Config):
    #production initialization
    DEBUG = False
    
config = {
    "development": DevelopmentConfig,
    "testing": TestingConfig,
    "production": ProductionConfig,
    "default": ProductionConfig
}