miDiccionario = {"Alemania": "Berlin", "Francia": "Paris",
                 "Reino Unido": "Londres", "España": "Madrid"}

print(miDiccionario["Francia"])  # accedo a una clave y da el valor

print(miDiccionario)  # esto imprime todo el diccionario

miDiccionario["Colombia"] = "Medellin"  # agrego una clave valor al diccionario

print(miDiccionario)

# sobre escribo la clave que tiene el valor errado y eso me actualiza
miDiccionario["Colombia"] = "Bogota"

print(miDiccionario)

# del elimina del diccionario la clave:alor indicado
del miDiccionario["España"]

print(miDiccionario)

# diccionario con varios tipos

miDiccionario2 = {"Colombia": "Bogota", 23: "Jordan", "Mosqueteros": 3}

print(miDiccionario2)

mitupla = ["Colombia", "Peru", "Venezuela", "Brasil"]

# puedo usar una tupla para asignar claves a un diccionario

miDiccionario3 = {mitupla[0]: "Bogota", mitupla[1]
    : "Lima", mitupla[2]: "Caracas", mitupla[3]: "Brasil"}

print(miDiccionario3)  # imprimo todo el diccionario3

miDiccionario4 = {23: "Jordan", "Nombre": "Michael",
                  "Equipo": "Chicago", "Anillos": [1991, 1992, 1993, 1996, 1997, 1998]}


# creo un dicionario dentro de otro diccionario
miDiccionario5 = {23: "Jordan", "Nombre": "Michael",
                  "Equipo": "Chicago", "Anillos": {"temporadas": [1991, 1992, 1993, 1996, 1997, 1998]}}

print(miDiccionario4)
print(miDiccionario4["Equipo"])

print(miDiccionario4["Anillos"])

print(miDiccionario.keys())  # keys nos devuelve claves del diccionario

# values nos devuelve los valores del diccionario
print(miDiccionario.values())
print(len(miDiccionario))  # len nos da la longitud del diccionario


print(miDiccionario2.keys())
print(miDiccionario2.values())
print(len(miDiccionario2))

print(miDiccionario3.keys())
print(miDiccionario3.values())
print(len(miDiccionario3))

print(miDiccionario4.keys())
print(miDiccionario4.values())
print(len(miDiccionario4))
