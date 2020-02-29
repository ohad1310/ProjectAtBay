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
    data = cur.fetchall()
    cur.close()
    return render_template('index.html', employees=data )


@app.route('/add-emp/', methods=['GET', 'POST'])
def addemp():
    if request.method == "POST":
        details = request.form
        idnum = details['idnum']
        firstName = details['fname']
        lastName = details['lname']
        email = details['email']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO employees(idnumber, firstName, lastName, email) VALUES (%s, %s, %s, %s)", (idnum, firstName, lastName, email))
        mysql.connection.commit()
    return render_template('add-emp.html')


@app.route('/edit-emp/<idnumber>', methods=['POST','GET'])
def update(idnumber):
        idnumber = request.form['idnumber']
        firstName = request.form['firstName']
        lastName = request.form['lastName']
        email = request.form['email']
        cur = mysql.connection.cursor()
        cur.execute("""
               UPDATE employees
               SET firstName=%s, lastName=%s, email=%s
               WHERE id=%s
            """, (idnumber, firstName, lastName, email))
        mysql.connection.commit()
        return render_template('edit-emp.html')


@app.route('/delete/<id_data>', methods=['GET', 'DELETE'])
def delete(id_data):
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM employees WHERE idnumber=%s", (id_data,))
    mysql.connection.commit()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)


