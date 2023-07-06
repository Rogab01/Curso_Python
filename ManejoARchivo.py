from io import open

archivoTexto = open("archivo.txt", "w")

frase = "Estudiando python hoy miercoles 28 de Octubre del 2020 \nTe deseo suerte!"

archivoTexto.write(frase)

archivoTexto.close()


print("*******************leer texto********************")

archivoTexto = open("archivo.txt", "r")

texto = archivoTexto.read()

archivoTexto.close()

print(texto)

print("*****************leer texto linea a linea**********************")

archivoTexto = open("archivo.txt", "r")

lineasTexto = archivoTexto.readlines()

archivoTexto.close()

print(lineasTexto[0])


print("***************** texto añadiendo**********************")

archivoTexto = open("archivo.txt", "a")

archivoTexto.write("\nSiempre es bueno seguir aprendiendo cada dia")

archivoTexto.close()

print("se añadio texto al archivo")


print("*******************leer texto********************")

archivoTexto = open("archivo.txt", "r")

print(archivoTexto.read())

print("*****")

archivoTexto.seek(0)

print(archivoTexto.read())
print("*****")

archivoTexto.seek(19)

print(archivoTexto.read())
print("*****")


archivoTexto.seek(0)

print(archivoTexto.read(11))
print("*****")


archivoTexto.seek(len(archivoTexto.read())/2)

print(archivoTexto.read())

print("*****")

archivoTexto.close()


print("*******************leer escribir texto********************")

archivoTexto = open("archivo.txt", "r+")

archivoTexto.write("Texto añadido ")

# print(archivoTexto.readlines())

listaTexto = archivoTexto.readlines()

listaTexto[1] = "Esta linea se a adicionado desde el exterior \n"

archivoTexto.seek(0)

archivoTexto.writelines(listaTexto)

archivoTexto.close()
