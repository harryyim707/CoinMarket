from flask import Blueprint, render_template, request, session, redirect, url_for, flash
from CoinMarket.models.User import User
from CoinMarket import db
from werkzeug.security import generate_password_hash

auth = Blueprint('auth', __name__, url_prefix='/')


@auth.route('/register', methods=['GET', 'POST'])
def register():
    if 'loggedin' in session:
        return redirect(url_for('index'))
    if request.method == 'POST' and "usr_id" in request.form and "usr_nm" in request.form and "usr_email" in request.form and "usr_pwd" in request.form and "repeat_pwd" in request.form:
        usr_id = request.form.get("usr_id")
        usr_nm = request.form.get("usr_nm")
        usr_email = request.form.get("usr_email")
        usr_pwd = request.form.get("usr_pwd")
        repeat_pwd = request.form.get("repeat_pwd")
        if usr_pwd != repeat_pwd:
            flash('Password does not match')
        user = User.query.filter_by(usr_id=usr_id).first()
        if not user:
            user = User(usr_id=usr_id, usr_nm=usr_nm, usr_pwd=generate_password_hash(usr_pwd), usr_email=usr_email)
            db.session.add(user)
            db.session.commit()
            return redirect('/login')
        else:
            flash('Existing user')
    return render_template('register.html')


@auth.route('/login', methods=['GET', 'POST'])
def login():
    # if request.method == 'POST':

    return render_template('login.html')