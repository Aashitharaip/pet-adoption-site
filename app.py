from flask import Flask, render_template, request, redirect, url_for, flash
import sqlite3

app = Flask(__name__)

# SQLite database setup
DATABASE = 'database.db'

def connect_db():
    return sqlite3.connect(DATABASE)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/adoption', methods=['GET', 'POST'])
def adoption():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM pets')
    pets = cursor.fetchall()
    cursor.execute('SELECT * FROM shelter')
    shelters = cursor.fetchall()
    cursor.execute('SELECT * FROM breed')
    breeds = cursor.fetchall()
    conn.close()
    if request.method == 'POST':
        pet_id = request.form['pet_id']
        shelter_id = request.form['shelter_id']
        breed_id = request.form['breed_id']
        return redirect(url_for('cart', pet_id=pet_id, shelter_id=shelter_id, breed_id=breed_id))
    return render_template('adoption.html', pets=pets, shelters=shelters, breeds=breeds)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        name = request.form['name']
        phone_no = request.form['phone_no']
        address = request.form['address']
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute('INSERT INTO customer (cust_name, phone_no, address) VALUES (?, ?, ?)', (name, phone_no, address))
        conn.commit()
        cust_id = cursor.lastrowid
        pet_id = request.args.get('pet_id')
        shelter_id = request.args.get('shelter_id')
        breed_id = request.args.get('breed_id')
        cursor.execute('INSERT INTO adoption_details (cust_id, pet_id, shelter_id, breed_id) VALUES (?, ?, ?, ?)', (cust_id, pet_id, shelter_id, breed_id))
        conn.commit()
        conn.close()
        flash('Pet added to cart successfully!')
        return redirect(url_for('cart', pet_id=pet_id, shelter_id=shelter_id, breed_id=breed_id))
    return render_template('login.html')

@app.route('/cart/<int:pet_id>/<int:shelter_id>/<int:breed_id>')
def cart(pet_id, shelter_id, breed_id):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM pets WHERE pet_id=?', (pet_id,))
    pet = cursor.fetchone()
    cursor.execute('SELECT * FROM shelter WHERE shelter_id=?', (shelter_id,))
    shelter = cursor.fetchone()
    cursor.execute('SELECT * FROM breed WHERE breed_id=?', (breed_id,))
    breed = cursor.fetchone()
    conn.close()
    return render_template('cart.html', pet=pet, shelter=shelter, breed=breed)

def init_db():
    with app.app_context():
        conn = connect_db()
        with app.open_resource('schema.sql', mode='r') as f:
            conn.cursor().executescript(f.read())
        conn.commit()
        conn.close()

        # Insert shelter values
        conn = connect_db()
        conn.cursor().execute('INSERT INTO shelter (shelter_name, location) VALUES (?, ?)', ('Shelter 1', 'Location 1'))
        conn.cursor().execute('INSERT INTO shelter (shelter_name, location) VALUES (?, ?)', ('Shelter 2', 'Location 2'))
        conn.commit()
        conn.close()

        

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
     
