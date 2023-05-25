from enum import unique

import pymysql
from CoinMarket import db


class User(db.Model):
    __tablename__ = "user"
    __table_args__ = {'mysql_collate': 'utf8_general_ci'}

    id = db.Column(db.Integer, primary_key=True, unique=True, nullable=False, autoincrement=True)
    user_id = db.Column(db.String(100))
    user_nm = db.Column(db.String(100))
    user_pwd = db.Column(db.String(100))
    user_email = db.Column(db.String(100))
    money = db.Column(db.Integer, default=0)
    coin = db.Column(db.Integer, default=0)
