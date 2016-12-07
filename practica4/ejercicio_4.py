# -*- coding: utf-8 -*-
#!/usr/bin/env python


import sqlite3
conn = sqlite3.connect('Libreria.db')
conn.text_factory = str
c = conn.cursor()


# Creamos la tabla para 
c.execute("CREATE TABLE Compradores(registro INT(4) PRIMARY KEY UNIQUE NOT NULL , nombre VARCHAR(35) UNIQUE NOT NULL DEFAULT ' ', fecha_nacim DATE NOT NULL DEFAULT '0000-00-00', telefono VARCHAR NULL DEFAULT NULL, domicilio VARCHAR NULL DEFAULT NULL, poblacion VARCHAR NULL DEFAULT NULL, anotaciones TEXT)")
conn.commit()
c.execute("CREATE TABLE Libros(registro INT(4) PRIMARY KEY UNIQUE NOT NULL, titulo VARCHAR(35) NOT NULL DEFAULT ' ' UNIQUE, escritor VARCHAR(35) NOT NULL DEFAULT ' ', editorial VARCHAR(35) NOT NULL DEFAULT ' ', soporte VARCHAR(35) NOT NULL DEFAULT 'LIBRO', fecha_entrada DATE NOT NULL DEFAULT '0000-00-00' UNIQUE, pais VARCHAR(20) NOT NULL DEFAULT NULL , importe DECIMAL(8,2) NOT NULL DEFAULT '0.0', anotaciones BLOB)")
conn.commit()
c.execute("CREATE TABLE Compras(registro INT(4) PRIMARY KEY UNIQUE NOT NULL UNIQUE, id_comprador INT(4) NOT NULL DEFAULT ' ', id_libro INT(4) NOT NULL DEFAULT ' ')")
conn.commit()
print ("Tabla creada con exito")


compradores = [
    (1,'Juan Miedo', 1955-10-23, 608900890, 'La isla del tesoro,33', 'Getafe', 'Buen Comprador'),
    (2, 'Pepe Pepino', 1961-12-13, 607899005, 'Plaza mayor,56', 'Pozuelo', ''),
    (3,'Pepe Mur', 1976-04-02, 917895679, 'Esparteros,5', 'Getafe', ''),
    (4,'Mohamed Alí', 1976-04-02, 609440567, 'Juan sin miedo,4', 'Pozuelo', 'Le gusta la ciencia ficción'),
    #(5,'Alfredo Mesa', 1986-08-17, 690890456, 'Gran via,56', 'Getafe', 'Le gustan los ensayos'),
    #(6,'Pedro Reyes', 1957-08-25, 917890056, 'Plaza de España,34', 'Pozuelo', 'Le gusta la historia'),
    (7,'Isabel Olvido', 1977-07-20, 915678900, 'Principal,3', 'Getafe', 'Le gusta la novela de terror'),
    #(8,'Mariano Calcetines', 1996-11-09, 634567876, 'Aviación,34', 'Getafe', ''),
    #(9,'María Calero', 1984-11-08, 645666900, 'Río Ebro,4', 'Las Rozas', '')    
]
for t in compradores:
    conn.execute('INSERT INTO Compradores (registro,nombre,fecha_nacim,telefono,domicilio,poblacion,anotaciones) VALUES (?,?,?,?,?,?,?)', t)
conn.commit()
libros=[
    (1,'El quijote', 'Mieguel de Cevantes', 'Alianza', 'LIBRO', 1988-06-11, 'España', 12,''),
    (2,'Marina', 'Calos Ruíz Zafón', 'Edebé', 'CD', 2003-05-10, 'España', 18.95,''),
    #(3,'La hoguera de las vanidades', 'Tom Wolfe', 'Edebé', 'CD', 2005-11-09, 'USA', 22.25,''),
    (4,'Los pilares de la tierra', 'Kenfollet', 'Faber', 'LIBRO', 2014-12-01, 'USA', 12.95,''),
    (5,'Otelo', 'Wiliam Shakespeare', 'Anaya', 'LIBRO', 2013-04-11, 'Inglaterra', 14.95,''),
    #(6,'Rimas y leyendas', 'Gustavo Adolfo Becquer', 'Roca', 'LIBRO', 2008-01-08, 'España', 25.95,''),
    (7,'Poesia', 'Juan Ramon Jimenez', 'P&J', 'LIBRO', 2002-04-07, 'España', 10.95,	''),
]
for t in libros:
    conn.execute('INSERT INTO Libros (registro,titulo,escritor,editorial,soporte,fecha_entrada,pais,importe,anotaciones) VALUES (?,?,?,?,?,?,?,?,?)', t)
conn.commit()
compras =[	(1,9,7),(2,9,3),(3,8,2),(4,7,1),(5,8,1),(6,1,1),(7,7,1),(8,6,2),(9,3,5),(10,3,1),(11,3,2)
]
for t in compras:
    conn.execute('INSERT INTO Compras(registro,id_comprador,id_libro) VALUES (?,?,?)', t)
conn.commit()  
#Obtener los países y el número de libros vendidos agrupados por país y ordenados de 
#manera descendente respecto al total de ventas.
conn.execute("CREATE VIEW aux AS SELECT pais, count(*) FROM libros NATURAL JOIN compras GROUP BY pais ORDER BY pais desc")
conn.commit()
consulta = "SELECT * FROM aux;"
for fila in conn.execute(consulta):
    print(fila)
    
#Obtener la media de los importes gastados por los compradores, agrupados por población y 
#ordenados decrecientemente por el importe medio.
conn.execute("CREATE VIEW aux1 AS SELECT compardores, Avg(count(*)) FROM  NATURAL JOIN compras GROUP BY poblacion ORDER BY  desc")
conn.commit()
consulta = "SELECT * FROM aux1;"
for fila in conn.execute(consulta):
    print(fila)
    
#Actualizar la tabla Compras, cambiando los registros 10 y 11 de forma que las filas tengan los 
#valores(3,3) y (3,7) respectivamente.
conn.execute("UPDATE compras SET id_libro = 3 where registro = 10")
conn.commit

#Obtener la media del precio de los libros agrupadas por soporte

#Borrar los compradores que no han comprado nunca ningún libro.









