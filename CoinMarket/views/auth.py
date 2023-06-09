from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from CoinMarket.models.User import User
from CoinMarket import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, logout_user, current_user

# 회원 가입, 로그인, 로그아웃을 담당하는 기능들의 모음


auth = Blueprint('auth', __name__, url_prefix='/')


@auth.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        if 'url' in session:
            return redirect(session['url'])
        else:
            return redirect(url_for('index.index'))
    if request.method == 'POST' and "usr_id" in request.form and "usr_nm" in request.form and "usr_email" in request.form and "usr_pwd" in request.form and "repeat_pwd" in request.form:
        usr_id = request.form.get("usr_id")
        usr_nm = request.form.get("usr_nm")
        usr_email = request.form.get("usr_email")
        usr_pwd = request.form.get("usr_pwd")
        repeat_pwd = request.form.get("repeat_pwd")
        if usr_pwd != repeat_pwd:
            flash('Password does not match', category="Error")
        user = User.query.filter_by(usr_id=usr_id).first()
        if not user:
            user = User(usr_id=usr_id, usr_nm=usr_nm, usr_pwd=generate_password_hash(usr_pwd), usr_email=usr_email)
            db.session.add(user)
            db.session.commit()
            flash('Signed Up Successfully', category="Success")
            if 'url' in session:
                return redirect(session['url'])
            else:
                return redirect(url_for('index.index'))
        else:
            flash('Existing user', category="Error")
    return render_template('register.html')


@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST' and 'usr_id' in request.form and 'usr_pwd' in request.form:
        usr_id = request.form.get('usr_id')
        usr_pwd = request.form.get('usr_pwd')
        user = User.query.filter_by(usr_id=usr_id).first()
        if user:
            if check_password_hash(user.usr_pwd, usr_pwd):
                login_user(user, remember=True)
                flash('Logged in Succesfully', category='Success')
                if 'url' in session:
                    return redirect(session['url'])
                return redirect(url_for('index.index'))
            else:
                flash('Incorrect Password', category='Error')
        else:
            flash('Incorrect ID/Password', category='Error')
    return render_template('login.html')


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index.index'))
