from flask import Flask
from sqlalchemy import create_engine, text


def create_app(test_config=None):
    app = Flask(__name__)

    if test_config is None:
        app.config.from_pyfile("config.py")
    else:
        app.config.update(test_config)

    database = create_engine(app.config['DB_URL'], max_overflow=0)
    app.database = database

    @app.route('/')
    def helloworld():
        return "Hello, world!"
    return app
