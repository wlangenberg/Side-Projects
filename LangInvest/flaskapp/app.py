from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy
import db

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/investments')
def investments():
    return render_template('investments.html', trades = getTrades(), totalspent = getTotalSpent())


def getTrades():
    sql = "SELECT * FROM maindb.trades;"
    result = db.cursor('langinvest', sql, ()).connect()
    return result

def getTotalSpent():
    sql = """
    SELECT SUM(
        CASE WHEN "type" = 'sell' then (-1 * shareprice * amount) 
        ELSE shareprice * amount END
        ) as totalspent
    FROM maindb.trades;
    """
    result = db.cursor('langinvest', sql, ()).connect()
    return result



def selectusers():
    sql = "SELECT * FROM users;"
    sqldata = ()
    cursor = db.cursor('langinvest', sql, sqldata)
    result = cursor.connect()
    return result

if __name__ == '__main__':
    app.run(debug=True)