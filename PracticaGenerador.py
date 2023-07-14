# esto es una funcion tradicional
def generaPar(limite):
    num = 1
    lista = []
    while num < limite:
        lista.append(num*2)
        num += 1
    return lista


print(generaPar(10))


print("----------------------------------------------------------------------------")
# esto es una funcion generador usa la palabra reservada YEILD. esto genera un objeto que se puede iterar


def generaPares(limite):

    num = 1

    while num < limite:

        yield num*2

        num += 1


# almaceno en una variable el objeto iteradao de la funcion generador
devuelvePar = generaPares(10)

for i in devuelvePar:
    print(i)


print("----------------------------------------------------------------------------")


def generaPares2(limite):

    num = 1

    while num < limite:

        yield num*2

        num += 1


devuelvePar = generaPares2(10)

print(next(devuelvePar))  # funcion NEXT

print("Aqui van mas datos del programa")

print(next(devuelvePar))

print("Aqui van mas datos del programa")

print(next(devuelvePar))

print("Aqui van mas datos del programa")
