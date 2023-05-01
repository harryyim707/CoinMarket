import xml.etree.ElementTree as elemTree
tree = elemTree.parse('keys.xml')
db = {
    'user': 'root',
    'password': tree.find('string[@name="DB_PWD"]').text,
    'host': 'localhost',
    'port': 3306,
    'database': 'coinmarket'
}

DB_URL = f"mysql+mysqlconnector://{db['user']}:{db['password']}@{db['host']}:{db['port']}/{db['database']}?charset=utf8"