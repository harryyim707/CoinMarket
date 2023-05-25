from flask import Flask
# from sqlalchemy import create_engine, text
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()

def create_app(config_filename):
    app = Flask(__name__)
    app.config.from_pyfile(config_filename)
    # ORM
    db.init_app(app)
    migrate.init_app(app, db)

    from .module import User, History, Sell

    # blueprint
    from .views.main_views import bp as bp
    app.register_blueprint(bp)

    return app
