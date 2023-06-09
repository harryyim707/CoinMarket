from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
import os

db = SQLAlchemy()
migrate = Migrate()


def create_app(config_filename):
    app = Flask(__name__)
    app.config.from_pyfile(config_filename)
    app.secret_key = os.urandom(24)
    # DB 등록
    db.init_app(app)
    migrate.init_app(app, db)

    # DB 모델 불러오기
    from CoinMarket.models import User, History, Sell

    # blueprint 등록
    from .views.index import bp as bp
    app.register_blueprint(bp)
    from .views.auth import auth as auth
    app.register_blueprint(auth)
    from .views.account import acc as acc
    app.register_blueprint(acc)
    from .views.personal import per as per
    app.register_blueprint(per)
    from .views.trade import tr as tr
    app.register_blueprint(tr)

    # flask-login 적용
    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        return User.User.query.get(user_id)

    @app.errorhandler(404)
    def page_not_found(error):
        return render_template('404.html')

    return app
