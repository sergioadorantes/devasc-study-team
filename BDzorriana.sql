# \. C:\Users\sergi\Documents\Universidad\5to Semestre\Administración de Base de Datos\BDzorriana.sql

DROP DATABASE IF EXISTS zorriana;
CREATE DATABASE zorriana;
USE zorriana;

CREATE TABLE categoria (
    idcat INT AUTO_INCREMENT PRIMARY KEY,
    nombre_categoria VARCHAR(30)
);

CREATE TABLE productos (
    idproducto INT AUTO_INCREMENT PRIMARY KEY,
    nombre_producto VARCHAR(30),
    descripcion VARCHAR(80),
    stock INT DEFAULT 0,
    idcat INT,
    preciounit DECIMAL(10,2) NOT NULL,
    FOREIGN KEY (idcat) REFERENCES categoria(idcat)
);

CREATE TABLE empleados (
    idemp INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(30) NOT NULL,
    puesto VARCHAR(30),
    sexo ENUM('M', 'F'),
    telefono VARCHAR(15)
);

CREATE TABLE clientes (
    idcliente INT AUTO_INCREMENT PRIMARY KEY,
    usuario VARCHAR(20),
    nivel VARCHAR(10),
    telefono VARCHAR(15),
    descuento DECIMAL(5,2) DEFAULT 0,
    idemp INT, 
    FOREIGN KEY (idemp) REFERENCES empleados(idemp) 
);

CREATE TABLE pedidos (
    idpedido INT AUTO_INCREMENT PRIMARY KEY,
    idcliente INT,
    idemp INT, 
    fecha DATE NOT NULL,
    total DECIMAL(10,2) NOT NULL,
    estpedido VARCHAR(15) DEFAULT 'Pendiente',
    FOREIGN KEY (idcliente) REFERENCES clientes(idcliente),
    FOREIGN KEY (idemp) REFERENCES empleados(idemp)
);

CREATE TABLE detalles_pedido (
    idpedido INT,
    idproducto INT,
    cantidad INT NOT NULL,
    descuento DECIMAL(5,2) DEFAULT 0,
    preciounit DECIMAL(10,2) NOT NULL,
    PRIMARY KEY (idpedido, idproducto),
    FOREIGN KEY (idpedido) REFERENCES pedidos(idpedido),
    FOREIGN KEY (idproducto) REFERENCES productos(idproducto)
);