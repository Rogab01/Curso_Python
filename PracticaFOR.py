""" print("practica I del bucles FOR")
for i in [1, 2, 3]:
    print("Hola")
    print(i)
print("practica I del bucles FOR")


for opcion in ["primavera", "verano", "otoño", "invierno"]:
    print("Hola")
    print(opcion)
print("practica I del bucles FOR")

for i in "sistemas.delfos@outlook.com":
    print("Hola", end=" ")
    print(i)


print("practica I del bucles FOR")

email = False
for i in "juan@pildorasinformaticas.es":
    if (i == "@"):
        email = True
if email == True:
    print("el correo es correcto")
else:
    print("el correo es incorrecto")


print("practica I del bucles FOR")
email = False
miemail = input("Introduce tu correo: ")
for i in miemail:
    if (i == "@"):
        email = True
if email == True:
    print("el correo es correcto")
else:
    print("el correo es incorrecto")


print("practica I del bucles FOR")

contador = 0
miemail = input("Introduce tu correo: ")
for i in miemail:
    if (i == "@" or i == "."):
        contador += 1

if contador == 2:
    print("el correo es correcto")
else:
    print("el correo es incorrecto") """


print("practica I del bucles RANGE")
for i in range(5, 10):
    #  print("hola")
    print(f"Valor de la variable {i}")


valido = False

email = input("Introduce tu correo: ")

for i in range(len(email)):
    if email[i] == "@":
        valido = True

if valido:
    print("correo valido")
else:
    print("correo invalido")
