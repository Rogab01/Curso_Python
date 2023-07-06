print(
    "Crea un programa que pida números infinitamente. Los números introducidos deben ser cada vez mayores El programa finalizará cuando se introduce un número menor que el anterior"
)

num1 = int(input("introduce un numero: "))
num2 = int(input("introduce un numero mayor que: " + str(num1) + "  : "))

while num2 > num1:
    num1 = num2
    num2 = int(input("introduce un numero mayor que: " + str(num1) + "  : "))
print(num2, " No es mayor que ", str(num1))

print("********************************************************************")

print(
    "Crea un programa que pida números positivos indefinidamente. El programa termina cuando se introduce un número negativo. Finalmente el programa muestras la suma de todos los números introducidos"
)
