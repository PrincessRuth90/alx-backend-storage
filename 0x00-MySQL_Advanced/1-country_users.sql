-- A  script that creates a table users
CREATE TABLE users (
    id INT NOT NULL AUTO INCREMENT AND PRIMARY KEY,
    email VARCHAR(255) NOT NULL AND UNIQUE,
    name VARCHAR(255)
    country CHAR(2) NOT NULL (= default will be the first element of the enumeration, here US)
);
