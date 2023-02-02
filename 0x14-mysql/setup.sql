CREATE DATABASE IF NOT EXISTS tyrell_corp;
USE tyrell_corp;
CREATE TABLE IF NOT EXISTS nexus6 (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
	name VARCHAR(100) UNIQUE
);
INSERT INTO nexus6 (name) VALUES ("Leon");
GRANT SELECT ON tyrell_corp.nexus6 TO 'holberton_user'@'localhost';
