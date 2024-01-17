from flask import Flask , request , render_template
import sqlite3
app = Flask(__name__)


def get_contacts(): 
    with sqlite3.connect("contacts.db") as conn:
        cur = conn.cursor()
        rows = cur.execute("SELECT * from contacts")
        print (rows)
        return rows.fetchall()

@app.route('/')
def home():
    return render_template("home.html" , contacts = get_contacts())

