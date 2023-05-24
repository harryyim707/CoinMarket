import pymysql
from CoinMarket import create_app
class Database():
    def __init__(self):
        self.db = pymysql.connect()