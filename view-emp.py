from flask import Flask, render_template, request
from flask_mysqldb import MySQL
from var import mysqlconnect

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def viewemp():
    if request.method == "GET":
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM employees")
        mysql.connection.commit()
        cur.close()
        return 'success'
    return render_template('index.html')


if __name__ == '__main__':
    app.run()