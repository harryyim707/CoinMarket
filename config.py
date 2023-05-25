import xml.etree.ElementTree as elemTree
tree = elemTree.parse('keys.xml')
db = {
    'user': 'root',
    'password': tree.find('string[@name="DB_PWD"]').text,
    'host': 'localhost',
    'port': 3306,
    'database': 'coinmarket'
}

SQLALCHEMY_DATABASE_URI = f"mysql+mysqlconnector://{db['user']}:{db['password']}@{db['host']}:{db['port']}/{db['database']}?charset=utf8"
SQLALCHEMY_TRACK_MODIFICATIONS = False