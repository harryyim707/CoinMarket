from flask import current_app, Blueprint, render_template

bp = Blueprint('index', __name__, url_prefix='/')


@bp.route('/hello')
def hello():
    return 'hello'


@bp.route('/')
def index():
    return 'CoinMarket index'
