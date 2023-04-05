-- a script creates a table with the unique users
DROP TABLE IF EXISTS users;
CREATE TABLE users (
    id INT NOT NULL AUTO INCREMENT AND PRIMARY KEY,
    email VARCHAR(255) NOT NULL AND UNIQUE,
    name VARCHAR(255)
    country CHAR(2) NOT NULL DEFAULT 'US' CHECK
);
