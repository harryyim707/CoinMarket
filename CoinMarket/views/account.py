# 계좌 충전과 출금 기능 담당
from flask import Blueprint, render_template, redirect, url_for, flash, request
from CoinMarket.models.User import User
from CoinMarket import db
from flask_login import login_required, current_user

acc = Blueprint('account', __name__, url_prefix='/account')


@acc.route('/')
@login_required
def account():
    return render_template('account.html')


@acc.route('/add-money', methods=['POST'])
@login_required
def add_money():
    if request.method == 'POST' and 'money' in request.form:
        user = User.query.filter_by(usr_id=current_user.usr_id).first()
        money = user.money + int(request.form.get('money'))
        user.money = money
        db.session.add(user)
        db.session.commit()
    return redirect(url_for('account.account'))


@acc.route('/withdraw', methods=['POST'])
@login_required
def withdraw():
    if request.method == 'POST' and 'money' in request.form:
        user = User.query.filter_by(usr_id=current_user.usr_id).first()
        if user.money < int(request.form.get('money')):
            flash('Insufficient balance', category='Error')
            return redirect(url_for('account.account'))
        money = user.money - int(request.form.get('money'))
        user.money = money
        db.session.add(user)
        db.session.commit()
    return redirect(url_for('account.account'))
