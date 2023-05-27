# 마이 페이지와 나의 거래내역 확인 기능 담당
from flask import Blueprint, render_template
from flask_login import current_user, login_required

from CoinMarket.models.History import History
from CoinMarket.models.Sell import Sell

per = Blueprint('personal', __name__, url_prefix='/')


@per.route('/my-page')
@login_required
def my_page():
    history = History.query.join(Sell, History.sell_id==Sell.id).add_columns(Sell.coin_nm, Sell.price).filter((History.seller_id == current_user.usr_id) | (History.buyer_id == current_user.usr_id)).all()
    return render_template('mypage.html', history_list=history)