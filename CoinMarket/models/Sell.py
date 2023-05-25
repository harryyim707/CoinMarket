from CoinMarket import db


class Sell(db.Model):
    __tablename__ = "sell"
    __table_args__ = {'mysql_collate': 'utf8_general_ci'}

    id = db.Column(db.Integer, primary_key=True, unique=True, nullable=False, autoincrement=True)
    seller_id = db.Column(db.Integer, db.ForeignKey('user.id', ondelete='CASCADE'))
    coin_nm = db.Column(db.Integer)
    price = db.Column(db.Integer)
