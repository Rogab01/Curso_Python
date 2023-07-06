print(
    "EJERCICIO 1: Crea un programa que pida dos números por teclado. El programa tendrá una función llamada “DevuelveMax” encargada de devolver el número más alto de los dos introducidos"
)

numero1 = int(input("Introduce el Primer numero: "))

numero2 = int(input("Introduce el Segundo numero: "))


def DevuelveMax(n1, n2):
    if n1 > n2:
        print("El ", n1, " es el mayor")
    elif n1 < n2:
        print("El ", n2, " es mayor")
    else:
        print("Los numeros son iguales")


DevuelveMax(numero1, numero2)

print(
    "EJERCICIO 2: Crea un programa que pida por teclado “Nombre”, “Dirección” y “Tfno”. Esos tres datos deberán ser almacenados en una lista y mostrar en consola el mensaje: “Los datos personales son: nombre apellido teléfono” (Se mostrarán los datos introducidos por teclado)."
)

nombre = input("Introduce tu Nombre: ")

direccion = input("Introduce tu Direccion: ")

telefono = input("Introduce tu Telefono: ")

miLista = (nombre, direccion, telefono)

print(
    "Los datos personales son: " + miLista[0] + " - " + miLista[1] + " - " + miLista[2]
)


print(
    "EJERCICIO 3: Crea un programa que pida tres números por teclado. El programa imprime en consola la media aritmética de los números introducidos"
)

numero1 = int(input("Introduce el primer numero: "))

numero2 = int(input("Introduce el segundo numero: "))

numero3 = int(input("Introduce el tercer numero: "))


def media(n1, n2, n3):
    resultado = (n1 + n2 + n3) / 3
    return resultado


print("La media aritmetica es: ", media(numero1, numero2, numero3))
