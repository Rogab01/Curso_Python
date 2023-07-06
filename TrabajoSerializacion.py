import pickle

lista_nombres=["Amada","Diana","Rodrigo","Antonella"]

fichero_binario=open("lista_nombres.txt","wb")

pickle.dump(lista_nombres, fichero_binario)

fichero_binario.close()

print ("**********************")

fichero=open("lista_nombres.txt","rb")

lista=pickle.load(fichero)

print(lista)


