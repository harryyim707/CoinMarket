# 거래와 관련된 모든 기능을 담당하는 파일
from flask import render_template, Blueprint, session, url_for, request, flash, redirect
from flask_login import current_user, login_required

from CoinMarket import db
from CoinMarket.models.History import History
from CoinMarket.models.Sell import Sell
from CoinMarket.models.User import User

tr = Blueprint('trade', __name__, url_prefix='/')


@tr.route('/marketplace')
def marketplace():
    session['url'] = url_for('trade.marketplace')
    last = History.query.order_by(History.id.desc()).first()
    latest_price = 0
    if last is not None:
        sell = Sell.query.filter_by(id=last.sell_id).first()
        latest_price = sell.price
    if current_user.is_authenticated:
        c = "col-xl-8"
    else:
        c = "col-xl-12"
    admin = User.query.filter_by(usr_id='admin').first()
    left_coin = admin.coin
    on_sale = Sell.query.filter_by(sold_out=0).order_by(Sell.id.desc()).all()
    history = History.query.join(Sell, History.sell_id == Sell.id).add_columns(Sell.price).order_by(
        History.id.asc()).all()
    label = "Coin Prices"
    xlabels = []
    dataset = []
    for his, price in history:
        xlabels.append(his.id)
        dataset.append(price)
    return render_template('marketplace.html', **locals())


@tr.route('/sell', methods=['POST'])
@login_required
def sell():
    if request.method == 'POST' and 'money' in request.form and 'coin' in request.form:
        coin = int(request.form.get('coin'))
        money = int(request.form.get('money'))
        user = User.query.filter_by(id=current_user.id).first()
        sell_col = Sell(seller_id=user.usr_id, coin_nm=coin, price=money, sold_out=0)
        db.session.add(user)
        db.session.add(sell_col)
        db.session.commit()
        flash('Successfully uploaded', category='Success')
    if 'url' in session:
        return redirect(session['url'])
    else:
        return redirect(url_for('index.index'))


@tr.route('/buy/<int:sell_id>', methods=['GET', 'POST'])
@login_required
def buy(sell_id):
    if request.method == 'POST':
        number = int(request.form.get('number'))
        if sell_id == 0 and 'number' in request.form:
            admin = User.query.filter_by(usr_id='admin').first()
            user = User.query.filter_by(usr_id=current_user.usr_id).first()
            if admin.coin < number:
                flash('Insufficient coins', category='Error')
                if 'url' in session:
                    return redirect(session['url'])
                else:
                    return redirect(url_for('index.index'))
            if user.money < number * 100:
                flash('Insufficient money', category='Error')
                if 'url' in session:
                    return redirect(session['url'])
                else:
                    return redirect(url_for('index.index'))
            user.money -= number * 100
            admin.money += number * 100
            admin.coin -= number
            user.coin += number
            db.session.add(user)
            db.session.add(admin)
            db.session.commit()
            flash('Transaction Completed', category='Success')
            if 'url' in session:
                return redirect(session['url'])
            else:
                return redirect(url_for('index.index'))
    elif request.method == 'GET':
        sell_col = Sell.query.filter_by(id=sell_id).first()
        seller = User.query.filter_by(usr_id=sell_col.seller_id).first()
        buyer = User.query.filter_by(usr_id=current_user.usr_id).first()
        if seller.coin < sell_col.coin_nm:
            flash('Insufficient coins', category='Error')
            if 'url' in session:
                return redirect(session['url'])
            else:
                return redirect(url_for('index.index'))
        if buyer.money < sell_col.coin_nm * sell_col.price:
            flash('Insufficient money', category='Error')
            if 'url' in session:
                return redirect(session['url'])
            else:
                return redirect(url_for('index.index'))
        buyer.money -= sell_col.coin_nm * sell_col.price
        seller.money += sell_col.coin_nm * sell_col.price
        seller.coin -= sell_col.coin_nm
        buyer.coin += sell_col.coin_nm
        sell_col.sold_out = 1
        history = History(sell_id=sell_col.id, seller_id=seller.usr_id, buyer_id=buyer.usr_id)
        db.session.add(seller)
        db.session.add(buyer)
        db.session.add(sell_col)
        db.session.add(history)
        db.session.commit()
        flash('Transaction Completed', category='Success')
        if 'url' in session:
            return redirect(session['url'])
        else:
            return redirect(url_for('index.index'))
    if 'url' in session:
        return redirect(session['url'])
    else:
        return redirect(url_for('index.index'))


@tr.route('/delete-coin/<int:sell_id>', methods=['POST'])
@login_required
def delete_coin(sell_id):
    if request.method == 'POST':
        sell_col = Sell.query.filter_by(id=sell_id).first()
        if sell_col.seller_id != current_user.usr_id:
            flash('Invalid access', category='Error')
            if 'url' in session:
                return redirect(session['url'])
            else:
                return redirect(url_for('trade.marketplace'))
        db.session.query(Sell).filter_by(id=sell_id).delete()
        db.session.commit()
        flash("Deleted successfully", category='Success')
        if 'url' in session:
            return redirect(session['url'])
        else:
            return redirect(url_for('trade.marketplace'))
    if 'url' in session:
        return redirect(session['url'])
    else:
        return redirect(url_for('trade.marketplace'))


@tr.route('/update-coin/<int:sell_id>', methods=['POST'])
@login_required
def update_coin(sell_id):
    if request.method == 'POST':
        if not (request.form.get('coin') and request.form.get('money')):
            if 'url' in session:
                return redirect(session['url'])
            else:
                return redirect(url_for('trade.marketplace'))
        sell_col = Sell.query.filter_by(id=sell_id).first()
        coin, money = sell_col.coin_nm, sell_col.price
        if request.form.get('coin'):
            coin = int(request.form.get('coin'))
        if request.form.get('money'):
            money = int(request.form.get('money'))
        db.session.query(Sell).filter_by(id=sell_id).update({'coin_nm': coin, 'price': money})
        db.session.commit()
        flash("Updated successfully", category='Success')
        if 'url' in session:
            return redirect(session['url'])
        else:
            return redirect(url_for('trade.marketplace'))
    if 'url' in session:
        return redirect(session['url'])
    else:
        return redirect(url_for('trade.marketplace'))