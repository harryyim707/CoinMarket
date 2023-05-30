from flask import Blueprint, render_template, session, url_for
from CoinMarket.models.History import History
from CoinMarket.models.Sell import Sell
from flask_login import current_user

bp = Blueprint('index', __name__, url_prefix='/')


@bp.route('/')
def index():
    session['url'] = url_for('index.index')
    last = History.query.order_by(History.id.desc()).first()
    latest_price = 0
    if last is not None:
        sell = Sell.query.filter_by(id = last.sell_id).first()
        latest_price = sell.price
    recent_coin = Sell.query.order_by(Sell.id.desc()).filter_by(sold_out=0).first()
    if not recent_coin:
        recent_coin = Sell(id=0, seller_id=0, coin_nm=0, price=0, sold_out=0)
    recent_price = 0
    if recent_coin is not None:
        recent_coin, recent_price = recent_coin, recent_coin.price
    if current_user.is_authenticated:
        c = "col-xl-3 col-md-6 mb-4"
    else:
        c = "col-xl-6 col-md-6 mb-4"
    history = History.query.join(Sell, History.sell_id == Sell.id).add_columns(Sell.price).order_by(History.id).all()
    label = "Coin Prices"
    xlabels = []
    dataset = []
    for his, price in history:
        xlabels.append(his.datetime.strftime("%d %b %Y %H:%M:%S"))
        dataset.append(price)
    return render_template('index.html', **locals())