from flask import Flask, render_template, request
from flask_mysqldb import MySQL
from var import mysqlconnect

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def addemp():
    if request.method == "POST":
        details = request.form
        idnumber = details['idnum']
        firstName = details['fname']
        lastName = details['lname']
        email = details['email']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO employees(idnumber, firstName, lastName, email) VALUES (%s, %s, %s, %s)", (idnumber, firstName, lastName, email))
        mysql.connection.commit()
        cur.close()
        return 'success'
    return render_template('add-emp.html')


if __name__ == '__main__':
    app.run()