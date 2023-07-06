def devuelveCiudades(*ciudades):
	for elemento in ciudades:
		yield elemento

ciudadesDevuelve=devuelveCiudades("Monteria","Cerete","Lorica","Sahagun")

print(next(ciudadesDevuelve))

print(next(ciudadesDevuelve))

print("**********************************************************************")

def devuelveCiudades(*ciudades):
	for elemento in ciudades:
		for subElemento in elemento:
			yield subElemento

ciudadesDevuelve=devuelveCiudades("Monteria","Cerete","Lorica","Sahagun")

print(next(ciudadesDevuelve))

print(next(ciudadesDevuelve))

print("**********************************************************************")

def devuelveCiudades(*ciudades):
	for elemento in ciudades:
		yield from elemento

ciudadesDevuelve=devuelveCiudades("Monteria","Cerete","Lorica","Sahagun")

print(next(ciudadesDevuelve))

print(next(ciudadesDevuelve))