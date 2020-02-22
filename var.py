from flask_mysqldb import MySQL


def mysqlconnect:
    app.config['MYSQL_HOST'] = '172.17.0.2'
    app.config['MYSQL_USER'] = 'root'
    app.config['MYSQL_PASSWORD'] = 'password'
    app.config['MYSQL_DB'] = 'atbay'
    mysql = MySQL(app)

