from functools import wraps
import sqlite3
from flask import flash, redirect, request, session, url_for, Request
from datetime import datetime


def login_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if session.get("user-token"):
            return func(*args, **kwargs)
        else:
            next_url = request.path if request.path != url_for('login') else None
            return redirect(url_for('login', next=next_url))
    return wrapper



class Database:
    def __init__(self):
        self.conn= sqlite3.connect("db.sqlite3")
        self.cur = self.conn.cursor()
        self.cur.execute("PRAGMA foriegn_keys = ON;")

    def init_db(self):
        with open('schema.sql', mode='r') as f:
            self.cur.executescript(f.read())
        self.conn.commit()

class Auth(Database):
    def register (self, request:Request):
        cust_name = request.form.get("name")
        email = request.form.get("email")
        phone_no = request.form.get("phone")
        local_address= request.form.get("address")
        password = request.form.get("password")
        data_tuple = (cust_name, email, phone_no, local_address, password)
        self.cur.execute("INSERT INTO CUSTOMER (cust_name, email, phone_no, local_address, password) VALUES (?, ?, ?, ?, ?);", data_tuple)
        self.conn.commit()

        
    def authenticate(self, request):
        email = request.form.get("email")
        password = request.form.get('password')
        db_password =  self.cur.execute("SELECT PASSWORD FROM CUSTOMER WHERE EMAIL = ?", (email,)).fetchone()
        if db_password:
            if password == db_password[0]:
                return email
            else:
                flash("Your password is Wrong...")
        else:
            flash("User Email Does Not Exist...")
        return None


class PetStore(Database):
    def get_pet(self, pet_id):
        pet = self.cur.execute(
            """SELECT P.PET_ID,  P.NAME, P.SPECIES, B.BREED_NAME, P.AGE, P.GENDER, S.SHELTER_NAME, S.LOCATION 
            FROM PETS P, SHELTER S, BREED B 
            WHERE P.BREED_ID = B.BREED_ID AND S.SHELTER_ID = P.SHELTER_ID AND P.PET_ID = ?;""", (pet_id,)).fetchone()
        return pet

    def get_pets(self):
        return self.cur.execute(
            """SELECT P.PET_ID,  P.NAME, P.SPECIES, B.BREED_NAME, P.AGE, P.GENDER, S.SHELTER_NAME, S.LOCATION 
            FROM PETS P, SHELTER S, BREED B 
            WHERE P.BREED_ID = B.BREED_ID AND S.SHELTER_ID = P.SHELTER_ID;""").fetchall()
    
    def buy_pet(self, pet_id):
        customer = self.cur.execute("SELECT * FROM CUSTOMER WHERE EMAIL = ?", (session.get("user-token"),)).fetchone()
        self.cur.execute("INSERT INTO ADOPTION_DETAILS (cust_id, pet_id, adop_date) VALUES (?, ?, ?)", 
                         (customer[0], pet_id, datetime.now()))
        self.conn.commit()
        return customer





        

       
            