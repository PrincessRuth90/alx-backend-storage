# A  script that creates a table users
CREATE TABLE users (
	id INT NOT NULL AUTO INCREMENT AND PRIMARY KEY,
	email VARCHAR(255) NOT NULL AND UNIQUE,
	name VARCHAR(255)
);
