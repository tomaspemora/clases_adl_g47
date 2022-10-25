-- CREATE DATABASE biblioteca;
DROP TABLE libro CASCADE;
DROP TABLE prestamo;

CREATE TABLE libro(
	id_libro SERIAL,
	-- id_libro INT PRIMARY KEY,
	nombre_libro VARCHAR(100),
	autor VARCHAR(100),
	genero VARCHAR(50),
	PRIMARY KEY (id_libro)
);

INSERT INTO libro (nombre_libro, autor, genero) VALUES 
	('sapo y sepo', 'arnold lobel', 'cuentos'),
	('la metamorfosis', 'franz kafka', 'novela');

CREATE TABLE prestamo(
	id_prestamo SERIAL,
	-- id_libro INT PRIMARY KEY,
	id_libro INT,
	nombre_persona VARCHAR(100),
	fecha_inicio DATE,
	fecha_termino DATE,
	PRIMARY KEY (id_prestamo),
	FOREIGN KEY (id_libro) REFERENCES libro(id_libro)
);

ALTER TABLE libro ADD prestado BOOLEAN;							-- agrega columna prestado a la tabla
ALTER TABLE libro ALTER COLUMN prestado SET DEFAULT FALSE;		-- modifica la columna prestado para que tenga un valor por default
UPDATE libro SET prestado = FALSE;								-- setea el valor de los datos en una columna

INSERT INTO prestamo(id_libro, nombre_persona, fecha_inicio, fecha_termino) VALUES 
(1, 'Braulio', '2022-09-15', '2022-10-15'),
(1, 'Tania', '2022-09-17', '2022-10-25');

INSERT INTO libro (nombre_libro, autor, genero) VALUES 
	('la nausea', 'sartre', 'novela'),
	('tokio blues', 'murakami', 'novela');

UPDATE libro SET prestado = TRUE WHERE id_libro=1;

select * from libro l, prestamo p where l.id_libro = p.id_libro;

select * from libro l, prestamo p where l.id_libro = p.id_libro and nombre_libro = 'sapo y sepo' order by fecha_inicio desc;

-- mysql workbench
-- COPY persons(first_name, last_name, dob, email) FROM 'C:\path\data.csv' DELIMITER ',' CSV HEADER;
