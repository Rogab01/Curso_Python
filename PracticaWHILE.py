import math
i=1
while i<=10:
	print("Se ejecuta " + str(i))
	i=i+1
print("ejecutado")


print("**************************************************************************")
edad=int(input("Introduce tu edad: "))
while edad<5 or edad>100:
	print("Has introducido una edad negatica, vuelve a intentar!!!")
	edad=int(input("Introduce tu edad: "))
print("gracias por colaborar, puedes pasar")
print("La edad del aspirante " + str(edad))


print("**************************************************************************")
print("Programa para calcular Raiz Cuadrada")
numero=int(input("Introduce un numero por favor: "))
intentos=0
while numero<0:
	print("No se puede hallar las raiz por ser numero negativo")
	if intentos==2:
		print("has cosumido demasiados intentos, el programa se cerrara!")
		break
	numero=int(input("Introduce un numero por favor: "))
	if numero<0:
		intentos=intentos+1
if intentos<2:
	solucion=math.sqrt(numero)
	print("La raiz cuadrada del numero " + str(numero) + " es: " + str(solucion))