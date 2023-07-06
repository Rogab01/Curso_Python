print("verificación de acceso")

edadUsuario = int(input("Introduce tu edad, por favor: "))

if edadUsuario < 18:
    print("No Puedes Pasar")
elif edadUsuario > 100:
    print("Edad Incorrecta")
else:
    print("Puedes Pasar")

print("Programa Finalizado")

nota = int(input("Introduce tu Nota, por favor: "))

if nota < 5:
    print("Insuficiente")
elif nota < 6:
    print("suficiente")
elif nota < 7:
    print("Bien")
elif nota < 9:
    print("Notable")
else:
    print("Sobresaliente")
