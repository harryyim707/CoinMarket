# 그래프와 최근 거래된 금액을 보여주는 기능 담당
from flask import render_template, Blueprint
from flask_login import current_user
from CoinMarket.models.Sell import Sell
from CoinMarket.models.History import History

flow = Blueprint('flow', __name__, url_prefix='/')


@flow.route('/charts')
def charts():
    history = History.query.join(Sell, History.sell_id == Sell.id).add_columns(Sell.price).order_by(History.id).all()
    label = "Coin Prices"
    xlabels = []
    dataset = []
    i = 1
    for his, price in history:
        xlabels.append(i)
        dataset.append(price)
        i += 1
    return render_template('charts.html', **locals())
