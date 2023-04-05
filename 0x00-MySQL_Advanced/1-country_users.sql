# A  script that creates a table users
CREATE TABLE users (
	id int, never null, auto increment and primary key,
	email varchar(255) never null and unique,
	name varchar(255)
	country char(2) never null (= default will be the first element of the enumeration, here US)
);
