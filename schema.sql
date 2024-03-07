CREATE TABLE IF NOT EXISTS shelter (
    shelter_id INTEGER PRIMARY KEY AUTOINCREMENT,
    shelter_name VARCHAR(20),
    location VARCHAR(20)
);

CREATE TABLE IF NOT EXISTS customer (
    cust_id INTEGER PRIMARY KEY,
    cust_name VARCHAR(30),
    email VARCHAR(30),
    phone_no INTEGER,
    address VARCHAR(50),
    shelter_id INTEGER,
    FOREIGN KEY(shelter_id) REFERENCES shelter(shelter_id)
);

CREATE TABLE IF NOT EXISTS breed (
    breed_id INTEGER PRIMARY KEY,
    breed_name VARCHAR(20)
);

CREATE TABLE IF NOT EXISTS pets (
    pet_id INTEGER PRIMARY KEY,
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
    adop_id INTEGER PRIMARY KEY,
    cust_id INTEGER,
    pet_id INTEGER,
    adop_date DATE,
    FOREIGN KEY(cust_id) REFERENCES customer(cust_id),
    FOREIGN KEY(pet_id) REFERENCES pets(pet_id)
);

INSERT INTO shelter (shelter_id, shelter_name, location) VALUES (1, 'Save animals shelter', 'Sai Ram Layout');
INSERT INTO shelter (shelter_id, shelter_name, location) VALUES (2, 'Shesh Naag', 'Magadi Road');
INSERT INTO shelter (shelter_id, shelter_name, location) VALUES (3, 'Cupa Larrc', 'Bangalore');

INSERT INTO breed (breed_id, breed_name) VALUES (1, 'Bulldog');
INSERT INTO breed (breed_id, breed_name) VALUES (2, 'Siamese');
INSERT INTO breed (breed_id, breed_name) VALUES (3, 'Holland Lop');

INSERT INTO pets (name, species, breed_id, gender, age, shelter_id) VALUES ('Buddy', 'Dog', 1, 'Male', 3, 1);
INSERT INTO pets (name, species, breed_id, gender, age, shelter_id) VALUES ('Whiskers', 'Cat', 2, 'Female', 2, 2);
INSERT INTO pets (name, species, breed_id, gender, age, shelter_id) VALUES ('Fluffy', 'Rabbit', 3, 'Male', 1, 3);