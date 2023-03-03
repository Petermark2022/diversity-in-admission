import sqlite3
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    con = sqlite3.connect('diversity_report_data.db')
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    cur.execute('select * from schools')
    rows = cur.fetchall()
    con.close()
    return render_template('index.html', rows=rows)

@app.route("/show/<school_id>")
def show(school_id):
    con = sqlite3.connect("diversity_report_data.db")
    con.row_factory = sqlite3.row
    cur = con.cursor()

    cur.execute("select * from enrollments WHERE dbn=?", (school_id,))
    rows = cur.fetchall()
    cur.execute("select * from schools WHERE school_id=?", (school_id,))
    diversity = cur.fetchall()
    con.close()
    return render_template("show.html", rows=rows, diversity=diversity)