miLista = ["Rodrigo", "Amada", "Carmen",
           "Vilma", "Diana", "Sofia", 5, True, 78.35]
print(miLista[:])
print(miLista[1])
print(miLista[-2])
print(miLista[0:3])
print(miLista[2:])
miLista.append("sandra")  # append agrega al final
print(miLista[:])
# insert agrega al comienzo pi 2 argumentos el idice donde se va a gregar y el valor
miLista.insert(2, "clara")
print(miLista[:])
miLista.extend(["Ana", "Lucia"])  # extend agrega varios valores a la lista
print(miLista[:])
print(miLista.index("Amada"))  # index nos devuelve el indice
print("Vilma" in miLista)  # in nos devulve true si encuentra el valor indicado

miLista.remove("Ana")  # remove eimina de la lista el valor indicado
print(miLista[:])

miLista.pop()  # pop elimina el ultimo elemento de la lista
print(miLista[:])
miLista2 = ["Sandra", "Pedro"] * 3
miLista3 = miLista + miLista2
print(miLista3[:])
