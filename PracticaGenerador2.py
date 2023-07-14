# el * en los argumentos es para indicar que son un numero indefino de elementos y esos argumentos son en forma de tupla
def devuelveCiudades(*ciudades):
    for elemento in ciudades:
        yield elemento


ciudadesDevuelve = devuelveCiudades("Monteria", "Cerete", "Lorica", "Sahagun")

print(next(ciudadesDevuelve))

print(next(ciudadesDevuelve))

print("**********************************************************************")


def devuelveCiudades1(*ciudades):
    for elemento in ciudades:
        for subElemento in elemento:
            yield subElemento


ciudadesDevuelve = devuelveCiudades1("Monteria", "Cerete", "Lorica", "Sahagun")

print(next(ciudadesDevuelve))

print(next(ciudadesDevuelve))

print("**********************************************************************")

# uso del yeld from simpifica el anidamiento


def devuelveCiudades2(*ciudades):
    for elemento in ciudades:
        yield from elemento


ciudadesDevuelve = devuelveCiudades2("Monteria", "Cerete", "Lorica", "Sahagun")

print(next(ciudadesDevuelve))

print(next(ciudadesDevuelve))
