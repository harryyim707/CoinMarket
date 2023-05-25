from CoinMarket import db


class User(db.Model):
    __tablename__ = "user"
    __table_args__ = {'mysql_collate': 'utf8_general_ci'}

    id = db.Column(db.Integer, primary_key=True, unique=True, nullable=False, autoincrement=True)
    usr_id = db.Column(db.String(100))
    usr_nm = db.Column(db.String(100))
    usr_pwd = db.Column(db.String(500))
    usr_email = db.Column(db.String(100))
    money = db.Column(db.Integer, default=0)
    coin = db.Column(db.Integer, default=0)

    def __init__(self, usr_id, usr_nm, usr_pwd, usr_email, money=0, coin=0):
        self.usr_id = usr_id
        self.usr_nm = usr_nm
        self.usr_pwd = usr_pwd
        self.usr_email = usr_email
        self.money = money
        self.coin = coin
