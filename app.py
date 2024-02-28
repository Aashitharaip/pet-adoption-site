from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

# SQLite database setup
DATABASE = 'database.db'

def connect_db():
    return sqlite3.connect(DATABASE)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/adoption')
def adoption():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM pets')
    pets = cursor.fetchall()
    conn.close()
    return render_template('adoption.html', pets=pets)

def init_db():
    with app.app_context():
        conn = connect_db()
        with app.open_resource('schema.sql', mode='r') as f:
            conn.cursor().executescript(f.read())
        conn.commit()
        conn.close()


init_db()

if __name__ == '__main__':
    app.run(debug=True)

