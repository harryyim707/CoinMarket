from CoinMarket import db


class History(db.Model):
    __tablename__ = "history"
    __table_args__ = {'mysql_collate': 'utf8_general_ci'}

    id = db.Column(db.Integer, primary_key=True, unique=True, nullable=False, autoincrement=True)
    sell_id = db.Column(db.Integer, db.ForeignKey('sell.id'))
    seller_id = db.Column(db.Integer)
    buyer_id = db.Column(db.Integer)
