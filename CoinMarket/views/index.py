from flask import Blueprint, render_template
from flask_login import current_user

bp = Blueprint('index', __name__, url_prefix='/')


@bp.route('/')
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