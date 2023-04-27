from flask import Flask
from flask import request
from flask import session
from flask import render_template, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from config import config
#from flask_bootstrap import Bootstrap
from flask_navigation import Navigation
from flask_login import LoginManager, current_user

login_manager = LoginManager()
login_manager.login_view = "main.login"

db = SQLAlchemy()

nav = Navigation()
nav.Bar('top', [
    nav.Item('<i class="bi bi-house-fill" style="font-size: 2rem;"></i>', 'main.home'),
    nav.Item('<i class="bi bi-image" style="font-size: 2rem;"></i>', 'main.photo'),
    nav.Item('<i class="bi bi-brush" style="font-size: 2rem;"></i>', 'main.examples_json'),
    nav.Item('<i class="bi bi-person-circle" style="font-size: 2rem;"></i>', 'main.profile'),
])


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    #Bootstrap(app)

    db.init_app(app)
    login_manager.init_app(app)
    nav.init_app(app)
    
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    
    return app