from flask import Flask
import sqlite3

app = Flask(__name__)

@app.route("/")
def home():
    try:
        conn = sqlite3.connect('sensorDB.db')
        conn.execute('CREATE TABLE IF NOT EXISTS lot_Master (lot_ID integer PRIMARY KEY,is_available integer NOT NULL,lot_timestamp datetime)')
        conn.close()

    except:
        return "Unsuccesful Connection"

    return "Connection Success"

if __name__  == "__main__":
    app.run(debug=True)


