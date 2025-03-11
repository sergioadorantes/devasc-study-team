# \. C:\Users\sergi\Documents\Universidad\5to Semestre\Administración de Base de Datos\practica06_23270095.sql

DROP DATABASE IF EXISTS dbtaller;
CREATE DATABASE dbtaller;
USE dbtaller;

CREATE TABLE lineainv(clavein CHAR(10) PRIMARY KEY, nombre VARCHAR(250));

CREATE TABLE profesor(idprofesor INT AUTO_INCREMENT PRIMARY KEY, nombreProf VARCHAR(200));

CREATE TABLE tipoproyecto(tipo CHAR(10) PRIMARY KEY, nombre VARCHAR(150));

CREATE TABLE proyecto(clave CHAR(10) PRIMARY KEY, nombre VARCHAR(250), clavein CHAR(10), tipo CHAR(10),
CONSTRAINT corresponde FOREIGN KEY (clavein) REFERENCES lineainv(clavein),
CONSTRAINT asignado FOREIGN KEY (tipo) REFERENCES tipoproyecto(tipo));

CREATE TABLE alumno(nocontrol CHAR(10) PRIMARY KEY, nombre VARCHAR(150), clave CHAR(10),
CONSTRAINT elige FOREIGN KEY (clave) REFERENCES proyecto(clave));

CREATE TABLE profesorproy(idprofesor INT, clave CHAR(10), calificacion FLOAT, rol VARCHAR(45),
CONSTRAINT asesora FOREIGN KEY (idprofesor) REFERENCES profesor(idprofesor),
CONSTRAINT dirige FOREIGN KEY (clave) REFERENCES proyecto(clave));

CREATE TABLE rol (id_rol INT AUTO_INCREMENT PRIMARY KEY, nombre VARCHAR(50) UNIQUE NOT NULL);

CREATE TABLE permiso (id_permiso INT AUTO_INCREMENT PRIMARY KEY, nombre VARCHAR(50) UNIQUE NOT NULL);

CREATE TABLE rol_permiso (id_rol INT, id_permiso INT, PRIMARY KEY (id_rol, id_permiso),
FOREIGN KEY (id_rol) REFERENCES rol(id_rol),
FOREIGN KEY (id_permiso) REFERENCES permiso(id_permiso));

CREATE TABLE usuario (id_usuario INT AUTO_INCREMENT PRIMARY KEY, nombre VARCHAR(100) NOT NULL, id_rol INT,
FOREIGN KEY (id_rol) REFERENCES rol(id_rol));

CREATE TABLE rubrica (id_rubrica INT AUTO_INCREMENT PRIMARY KEY, nombre VARCHAR(255) NOT NULL, descripcion TEXT, ponderacion_total INT NOT NULL);

CREATE TABLE criterio_rubrica (id_criterio INT AUTO_INCREMENT PRIMARY KEY, id_rubrica INT, nombre_criterio VARCHAR(255) NOT NULL, ponderacion INT NOT NULL,
FOREIGN KEY (id_rubrica) REFERENCES rubrica(id_rubrica) ON DELETE CASCADE);

CREATE TABLE proyecto_rubrica (id_proyecto_rubrica INT AUTO_INCREMENT PRIMARY KEY, clave_proyecto CHAR(10), id_rubrica INT,
FOREIGN KEY (clave_proyecto) REFERENCES proyecto(clave) ON DELETE CASCADE,
FOREIGN KEY (id_rubrica) REFERENCES rubrica(id_rubrica) ON DELETE CASCADE);