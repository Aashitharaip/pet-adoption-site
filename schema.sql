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
    breed_id INTEGER PRIMARY KEY,
    breed_name TEXT
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

