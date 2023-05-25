from flask import Flask
# from sqlalchemy import create_engine, text
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os

db = SQLAlchemy()
migrate = Migrate()


def create_app(config_filename):
    app = Flask(__name__)
    app.config.from_pyfile(config_filename)
    app.secret_key = os.urandom(24)
    # ORM
    db.init_app(app)
    migrate.init_app(app, db)

    from CoinMarket.models import User, History, Sell

    # blueprint
    from .views.index import bp as bp
    app.register_blueprint(bp)
    from .views.auth import auth as auth
    app.register_blueprint(auth)

    return app
