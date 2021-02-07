#app/__init__.py

from flask import Flask, render_template
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_bootstrap import Bootstrap
from flask_marshmallow import Marshmallow, fields
from flask_sqlalchemy import SQLAlchemy
from config import app_config

db = SQLAlchemy()
ma = Marshmallow()
login_manager = LoginManager()

def create_app(config_name):
    # the "instance_relative_config=True" setting tells the app that config files are relative to the instance folder
    app = Flask(__name__, instance_relative_config=True)

    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')

    Bootstrap(app)
    db.init_app(app)
    ma.init_app(app)

    login_manager.init_app(app)
    login_manager.login_message = "You must be logged in to see this page. "
    login_manager.login_view = "auth.login"


    migrate = Migrate(app, db)

    from app import models
    
    from .admin import admin as admin_blueprint
    app.register_blueprint(admin_blueprint, url_prefix='/admin')
    
    from .home import home as home_blueprint
    app.register_blueprint(home_blueprint)

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    # from .api import api as api_blueprint
    # app.register_blueprint(api_blueprint, url_prefix="/api/v0")
    
    @app.errorhandler(404)
    def not_found(error):
        return render_template('errors/404.html', title='Page Isn\'t Found Dawg')

    # Do some OAuth instead of Flask login manager

    @app.errorhandler(500)
    def internal_server_error(error):
      
        # if wants_json_response():
            #return api_error_response(500)
        return render_template('errors/500.html', title='Internal Server Error')

    return app