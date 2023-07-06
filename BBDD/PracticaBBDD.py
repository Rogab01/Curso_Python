import sqlite3

miConexion=sqlite3.connect("PrimeraBase")

miCursor=miConexion.cursor()
#miCursor.execute("CREATE TALE PRODUCTOS(Nom_Articulo VARCHAR(50), Precio INTEGER, Seccion VARCHAR(20))")
#miCursor.execute("INSERT INTO PRODUCTOS VALUES('BALON',150,'DEPORTE')")
#variosProductos=[
#	("CAMISETA", 10, "DEPORTE"),
#	("JARRON", 90, "CERAMICA"),
#	("CAMION", 10, "JUGUEERIA")
#]
#miCursor.executemany("INSERT INTO PRODUCTOS VALUES(?,?,?)", variosProductos)


miCursor.execute("SELECT * FROM PRODUCTOS")

variosProductos=miCursor.fetchall()

for producto in variosProductos:
	print("Nombre Articulo: ",producto[0], "Seccion: ", producto[2])



miConexion.commit()





miConexion.close()