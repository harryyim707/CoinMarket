from flask import current_app, Blueprint, render_template

bp = Blueprint('index', __name__, url_prefix='/')


@bp.route('/')
@bp.route('/index')
def index():
    return render_template('index.html')


# @bp.route('/login')
# def login():
#     return render_template('login.html')
#
#
# @bp.route('/register')
# def join():
#     return render_template('register.html')