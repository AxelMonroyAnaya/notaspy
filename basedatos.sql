CREATE TABLE IF NOT EXISTS proyecto;
use proyecto;

CREATE TABLE IF NOT EXISTS usuarios(
    id INTEGER auto_increment NOT NULL,
    nombre VARCHAR(45),
    apellidos VARCHAR(100),
    email VARCHAR(255) NOT NULL,
    password VARCHAR(45),
    fecha DATE NOT NULL,
    CONSTRAINT pkuSUARIOS PRIMARY KEY(id),
    CONSTRAINT uqmail UNIQUE(email)
)ENGINE=InnoDb:

CREATE TABLE notas(
    id INTEGER auto_increment NOT NULL,
    usuario_id INTEGER NOT NULL,
    titulo varchar(45),
    nota TEXT,
    fecha DATE NOT NULL,
    CONSTRAINT Pk_id PRIMARY KEY(id),
    CONSTRAINT fk_usuario_id FOREIGN KEY(usuario_id) REFERENCES usuarios(id)
)