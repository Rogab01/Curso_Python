nombreUsuario = input("Introduce el nombre: ")

print("Mi nombre es: ", nombreUsuario.upper())

print("Mi nombre es: ", nombreUsuario.lower())

print("Mi nombre es: ", nombreUsuario.capitalize())


edad = input("introduce tu edad: ")

while (edad.isdigit() == False):
    print("Por favor introduce un valor numerico")
    edad = input("introduce tu edad: ")

if (int(edad) < 18):
    print("No Puedes PASAR")
else:
    print("Podes PASAR")

print(edad.isdigit())
