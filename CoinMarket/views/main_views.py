from flask import current_app, Blueprint, render_template

bp = Blueprint('index', __name__, url_prefix='/')


@bp.route('/')
def index():
    return render_template('Main.html')


@bp.route('/login')
def login():
    return render_template('Login.html')


@bp.route('/join')
def join():
    return render_template('Join.html')