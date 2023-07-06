import math

def evaluaEdad(edad):
	if edad<0:
		raise TypeError("no se permiten edades negativas")
	if edad<20:
		return "eres muy joven"
	elif edad<40:
		return "eres joven"
	elif edad < 65:
		return "eres maduro"
	elif edad<100:
		return "Cuidate..."

print(evaluaEdad(8))


print("**************************************************************")

def calculaRaiz(num1):

	if num1<0:
		raise ValueError("El numero es negativo")
	else:
		return math.sqrt(num1)

op=int(input("inroduce un numero: "))

try:
	print(calculaRaiz(op))
except ValueError as ErrorDeNumeroNegativo:
	print(ErrorDeNumeroNegativo)


print("Mas lineas del programa")
print("Programa terminado")
