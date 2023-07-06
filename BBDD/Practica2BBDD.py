import sqlite3

miConexion=sqlite3.connect("GestionProductos")

miCursor=miConexion.cursor()

#miCursor.execute('''
#	CREATE TABLE PRODUCTOS (
#	CODIGO_ARTICULO VARCHAR(4) PRIMARY KEY,
#	NOMBRE_ARTICULO VARCHAR(50),
#	PRECIO INTEGER,
#	SECCION VARCHAR(20))
#	''')

#productos=[
#	("AR01","PELOTA", 20,"JUGUETERIA"),
#	("AR02","PANTALON",15,"CONFECCION"),
#	("AR03","DESTORNILLADOR",25,"FERRETERIA"),
#	("AR04","JARRON",45,"CERAMICA")
#]



#miCursor.execute('''
#	CREATE TABLE PRODUCTOS (
#	ID INTEGER PRIMARY KEY AUTOINCREMENT,
#	NOMBRE_ARTICULO VARCHAR(50) UNIQUE,
#	PRECIO INTEGER,
#	SECCION VARCHAR(20))
#	''')

#productos=[
#	("PELOTA", 20,"JUGUETERIA"),
#	("PANTALON",15,"CONFECCION"),
#	("DESTORNILLADOR",25,"FERRETERIA"),
#	("JARRON",45,"CERAMICA"),
#	("PANTALONES",35,"CONFECCION")
#]

#miCursor.executemany("INSERT INTO PRODUCTOS VALUES(NULL,?,?,?)", productos)

#miCursor.execute("SELECT * FROM PRODUCTOS WHERE SECCION='CONFECCION'")

#miCursor.execute("UPDATE PRODUCTOS SET PRECIO=35 WHERE NOMBRE_ARTICULO='PELOTA'")


miCursor.execute("DELETE FROM PRODUCTOS WHERE ID=4")

#productos=miCursor.fetchall()

#print(productos)



miConexion.commit()

miConexion.close()