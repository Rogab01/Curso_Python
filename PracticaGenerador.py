def generaPar(limete):
    num = 1
    lista = []
    while num < limete:
        lista.append(num*2)
        num += 1
    return lista


print(generaPar(10))


print("----------------------------------------------------------------------------")


def generaPares(limete):

    num = 1

    while num < limete:

        yield num*2

        num = num+1


devuelvePar = generaPares(10)

for i in devuelvePar:
    print(i)


print("----------------------------------------------------------------------------")


def generaPares(limete):

    num = 1

    while num < limete:

        yield num*2

        num = num+1


devuelvePar = generaPares(10)

print(next(devuelvePar))

print("Aqui van mas datos del programa")

print(next(devuelvePar))

print("Aqui van mas datos del programa")
