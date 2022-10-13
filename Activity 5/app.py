import sqlite3
from flask import Flask, render_template

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

app = Flask(__name__)

@app.route('/')
def index():
    conn = get_db_connection()
    posts = conn.execute('SELECT * FROM posts p').fetchall()
    conn.close()
    return render_template('index.html', posts=posts)

@app.route('/base')
def base():
    return render_template('base.html')


if __name__=="__main__":
    app.run(host="localhost", debug=True)