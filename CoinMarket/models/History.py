from CoinMarket import db
import datetime


class History(db.Model):
    __tablename__ = "history"
    __table_args__ = {'mysql_collate': 'utf8_general_ci'}


    id = db.Column(db.Integer, primary_key=True, unique=True, nullable=False, autoincrement=True)
    sell_id = db.Column(db.Integer, db.ForeignKey('sell.id', ondelete='CASCADE'))
    seller_id = db.Column(db.String(100))
    buyer_id = db.Column(db.String(100))
    datetime = db.Column(db.DateTime(timezone=True), default= datetime.datetime.now())
