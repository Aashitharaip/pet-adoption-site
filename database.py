import sqlite3

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
    def register (self,cust_name, email, phone_no, local_address, password):
        self.cur.execute("INSERT INTO CUSTOMER(cust_name, email, phone_no, local_address, password) values (?, ?, ?, ?, ?) ",
                          (cust_name, email, phone_no, local_address, password))
        self.conn.commit()




        

       
            