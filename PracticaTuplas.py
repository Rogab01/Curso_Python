miTupla = ("Rodrigo", "Amada", 7, 28, 1977)

miLista = list(miTupla)  # list convierte una tupla en lista

print(miTupla[2])

print(miLista)

milista2 = ["Pedro", "Luis", 2, 14, 2007, 10, 10]

miTupla2 = tuple(milista2)  # tuple convierte una lista en tupla

print(miTupla2)
print("Pedro" in miTupla2)  # in busca el valor pedido en la tupla

# count nos devuelve la cantidad de veces se repite el elemento pedido
print("hay ", miTupla2.count(10))

print(len(milista2))  # len devuelve la longitud de la tupla

miTupla3 = ("Amada",)  # tupla unitaria lleva una como al final

print(miTupla3)
# desempaquetado de tupla asigna los valores de la tupla a cada variable
nombre, apellido, dia, mes, agno = miTupla
print(nombre)
print(agno)
print(dia)
print(apellido)
print(mes)
