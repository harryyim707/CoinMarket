from flask import Blueprint, render_template
from CoinMarket.models.History import History
from CoinMarket.models.Sell import Sell
from flask_login import current_user

bp = Blueprint('index', __name__, url_prefix='/')


@bp.route('/')
def index():
    last = History.query.order_by(History.id.desc()).first()
    latest = 0
    if last is not None:
        sell = Sell.query.filter(id == last.sell_id)
        latest = sell.price
    recent = Sell.query.order_by(Sell.id.desc()).first()
    recent_coin, recent_price = 0, 0
    if recent is not None:
        recent_coin, recent_price = recent.coin_nm, recent.price
    if current_user.is_authenticated:
        c = "col-xl-3 col-md-6 mb-4"
    else:
        c = "col-xl-6 col-md-6 mb-4"
    return render_template('index.html', latest_price=latest, recent_coin=recent_coin, recent_price=recent_price, c=c)