from flask_login import LoginManager
from flask_migrate import Migrate
from flask_bootstrap import Bootstrap
from flask_marshmallow import Marshmallow, fields

from config import app_config

db = SQLAlchemy()
ma = Marshmallow()

def create_app(config_name):
    # the "instance_relative_config=True" setting tells the app that config files are relative to the instance folder
    app = Flask(__name__, instance_relative_config=True)

    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')

    Bootstrap(app)
    db.init_app(app)
    ma.init_app(app)
    migrate = Migrate(app, db)

    from app import models
    
    from .admin import admin as admin_blueprint
    app.register_blueprint(admin_blueprint, url_prefix='/admin')
    

    return app