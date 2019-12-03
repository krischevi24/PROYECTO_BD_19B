CREATE DATABASE proyecto;

CREATE TABLE contactos(id INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY, nombre VARCHAR(100) NOT NULL, tel VARCHAR(20) NOT NULL, email VARCHAR(50) NOT NULL, face VARCHAR(50) NOT NULL, twitter VARCHAR(50) NOT NULL, insta VARCHAR(50) NOT NULL);

INSERT INTO contactos(nombre, tel, email, face, twitter, insta) VALUES('Balam Rodriguez Arellano', '3323574811', 'balamr@udg.mx', 'Balam Rodriguez', 'balamr23', 'BalamArellano');

INSERT INTO contactos(nombre, tel, email, face, twitter, insta) VALUES('Francisco Hernandez', '3325573600', 'fhernadezs@udg.mx', 'Francisco Hernandez S.', 'Fherna1', 'Franhernandez');