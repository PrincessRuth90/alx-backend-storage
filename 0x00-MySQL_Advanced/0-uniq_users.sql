-- a script creates a table with the unique users
CREATE TABLE IF NOT EXISTS users (
    id INT NOT NULL AUTO_INCREMENT AND PRIMARY KEY,
    email VARCHAR(255) NOT NULL UNIQUE,
    name VARCHAR(255)
);
