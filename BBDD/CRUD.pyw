from tkinter import * 
from tkinter import messagebox
import sqlite3

raiz=Tk()
raiz.title("practica CRUD")
#----------------- MENU -----------------------
barraMenu=Menu(raiz)
raiz.config(menu=barraMenu, width=300, height=300)

bbddMenu=Menu(barraMenu, tearoff=0)
bbddMenu.add_command(label="Conectar")
bbddMenu.add_command(label="Salir")

borrarMenu=Menu(barraMenu, tearoff=0)
borrarMenu.add_command(label="Borrar campos")

crudMenu=Menu(barraMenu, tearoff=0)
crudMenu.add_command(label="Conectar")
crudMenu.add_command(label="Leer")
crudMenu.add_command(label="Actualizar")
crudMenu.add_command(label="Borrar")

ayudaMenu=Menu(barraMenu, tearoff=0)
ayudaMenu.add_command(label="Licencia")
ayudaMenu.add_command(label="Acerca de...")

barraMenu.add_cascade(label="BBDD", menu=bbddMenu)
barraMenu.add_cascade(label="Borrar", menu=borrarMenu)
barraMenu.add_cascade(label="CRUD", menu=crudMenu)
barraMenu.add_cascade(label="Ayuda", menu=ayudaMenu)

#----------------- CAMPOS -----------------------

miframe=Frame(raiz)
miframe.pack()

cuadroID=Entry(miframe)
cuadroID.grid(row=0, column=1,padx=10,pady=10)

cuadroNombre=Entry(miframe)
cuadroNombre.grid(row=1, column=1,padx=10,pady=10)
cuadroNombre.config(fg="red", justify="right")

cuadroPass=Entry(miframe)
cuadroPass.grid(row=2, column=1,padx=10,pady=10)
cuadroPass.config(show="*")

cuadroApellido=Entry(miframe)
cuadroApellido.grid(row=3, column=1,padx=10,pady=10)

cuadroDireccion=Entry(miframe)
cuadroDireccion.grid(row=4, column=1,padx=10,pady=10)

textoComentario=Text(miframe, width=16, height=5)
textoComentario.grid(row=5, column=1,padx=10,pady=10)
scrollVert=Scrollbar(miframe, command=textoComentario.yview)
scrollVert.grid(row=5,column=2,sticky="nsew")


textoComentario.config(yscrollcommand=scrollVert.set)









raiz.mainloop()