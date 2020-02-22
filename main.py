from flask import Flask, render_template, request
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = '172.17.0.2'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'password'
app.config['MYSQL_DB'] = 'atbay'

mysql = MySQL(app)


@app.route('/')
def index():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM employees")
    mysql.connection.commit()
    cur.close()
    return render_template('index.html')


@app.route('/')
def addemp():
    details = request.form
    idnumber = details['idnum']
    firstName = details['fname']
    lastName = details['lname']
    email = details['email']
    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO employees(idnumber, firstName, lastName, email) VALUES (%s, %s, %s, %s)", (idnumber, firstName, lastName, email))
    mysql.connection.commit()
    cur.close()
    return render_template('add-emp.html')


if __name__ == '__main__':
    app.run()

if __name__ == '__main__':
    app.run()