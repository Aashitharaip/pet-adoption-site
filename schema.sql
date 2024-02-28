CREATE TABLE IF NOT EXISTS customer (
    cust_id INTEGER PRIMARY KEY,
    cust_name VARCHAR(30),
    email VARCHAR(30),
    phone_no INTEGER,
    address VARCHAR(50)
    
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
    FOREIGN KEY(breed_id) REFERENCES breed(breed_id)
);

CREATE TABLE IF NOT EXISTS shelter (
    shelter_id INTEGER PRIMARY KEY,
    shelter_name VARCHAR(20),
    location VARCHAR(20)
);

CREATE TABLE IF NOT EXISTS adoption_details (
    adop_id INTEGER PRIMARY KEY,
    cust_id INTEGER,
    pet_id INTEGER,
    adop_date DATE,
    FOREIGN KEY(cust_id) REFERENCES customer(cust_id),
    FOREIGN KEY(pet_id) REFERENCES pets(pet_id)
);
