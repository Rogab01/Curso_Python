print("************************* Continue ****************************************")
for letra in "Python":
    if letra == "h":
        continue
    print("Viendo la letra: " + letra)


print("***************************************************************************")
nombre = "Pildoras Informaticas"
print(len(nombre))


print("************************* Continue ****************************************")
nombre = "Pildoras Informaticas"
contador = 0
for i in nombre:
    if i == " ":
        continue
    contador += 1

print(contador)


print("************************* Continue ****************************************")
email = input("introduzca su correo: ")

for i in email:
    if i == "@":
        arroba = True
        break
else:
    arroba = False

print(arroba)
