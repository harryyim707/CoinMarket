from flask import Flask
from sqlalchemy import create_engine, text


def create_app(config_filename):
    app = Flask(__name__)
    app.config.from_pyfile(config_filename)
    # ORM
    database = create_engine(app.config['DB_URL'], max_overflow=0)
    app.database = database

    # blueprint
    from .views import main_views
    app.register_blueprint(main_views.bp)
    from .views import login
    app.register_blueprint(login.bp)

    return app
