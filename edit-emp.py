from flask import Flask, render_template, request
from flask_mysqldb import MySQL
from var import mysqlconnect

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def edit():
    if request.method == "GET":
        cur = mysql.connection.cursor()
        cur.execute("UPDATE employees SET data WHERE idnumber =  idnum)
        mysql.connection.commit()
        cur.close()
        return 'success'
    return render_template('index.html')


if __name__ == '__main__':
    app.run()