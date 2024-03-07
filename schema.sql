CREATE TABLE IF NOT EXISTS shelter (
    shelter_id INTEGER PRIMARY KEY AUTOINCREMENT,
    shelter_name TEXT,
    location TEXT
);

CREATE TABLE IF NOT EXISTS customer (
    cust_id INTEGER PRIMARY KEY AUTOINCREMENT,
    cust_name TEXT,
    email TEXT,
    phone_no TEXT,
    local_address TEXT,
    password TEXT
);

CREATE TABLE IF NOT EXISTS breed (
    breed_id INTEGER PRIMARY KEY AUTOINCREMENT,
    breed_name TEXT
);

CREATE TABLE IF NOT EXISTS pets (
    pet_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    species TEXT NOT NULL,
    breed_id INTEGER,
    gender TEXT NOT NULL,
    age INTEGER,
    shelter_id INTEGER,
    FOREIGN KEY(breed_id) REFERENCES breed(breed_id),
    FOREIGN KEY(shelter_id) REFERENCES shelter(shelter_id)
);

CREATE TABLE IF NOT EXISTS adoption_details (
    adop_id INTEGER PRIMARY KEY AUTOINCREMENT,
    cust_id INTEGER,
    pet_id INTEGER,
    adop_date DATE,
    FOREIGN KEY(cust_id) REFERENCES customer(cust_id),
    FOREIGN KEY(pet_id) REFERENCES pets(pet_id)
);




INSERT INTO SHELTER VALUES(1, "Animal Hive", "KR Puram, Bengaluru");
INSERT INTO SHELTER VALUES(2, "Pet Park", "Rajaji Nagar, Bengaluru");
INSERT INTO SHELTER VALUES(3, "Platinum Pets", "Magestic, Bengaluru");

INSERT INTO BREED VALUES (1, "German Shephard");
INSERT INTO BREED VALUES (2, "Great Dane");
INSERT INTO BREED VALUES (3, "Rottweiler");
INSERT INTO BREED VALUES (4, "Bull Dog");

INSERT INTO BREED VALUES (5, "Siamese");
INSERT INTO BREED VALUES (6, "Persian");
INSERT INTO BREED VALUES (7, "Shpynx");
INSERT INTO BREED VALUES (8, "British Shorthair");

INSERT INTO PETS ('name', 'species', 'breed_id',  'gender',  'age', 'shelter_id') VALUES 
                ('Bobby', 'Dog', 1, 'Male', 2, 1),
                ('Bella', 'Dog', 2, 'Female', 1, 2),
                ('Tyson', 'Dog', 3, 'Male', 2, 3),
                ('Liana', 'Dog', 4, 'Female', 1, 2),

                ('Jack', 'Cat', 5, 'Male', 1, 1),
                ('Lilly', 'Cat', 7, 'Female', 2, 2),
                ('Luke', 'Cat', 6, 'Male', 2, 3),
                ('Birdie', 'Cat', 8, 'Female', 1, 2);