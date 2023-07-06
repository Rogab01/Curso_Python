from tkinter import *
from tkinter import messagebox

home=Tk()
home.title("Menu")

def infoAdicional():
	messagebox.showinfo("Procesador de Rodrigo", "procesador de texo Version 2020")

def avisoLicencia():
	messagebox.showwarning("Lincencia", "Licencia bajo GNU")

def salirAplicacion():
	#valor=messagebox.askquestion("Salir","Deseas salir")
	valor=messagebox.askokcancel("Salir","Deseas salir")
	if valor==True:
		home.destroy()

def cerrarDocumento():
	valor=messagebox.askretrycancel("Reintentar","No es posible cerrar documento")
	if valor==True:
		home.destroy()

barraMenu=Menu(home)

home.config(menu=barraMenu, width=300, height=300)

archivoMenu=Menu(barraMenu, tearoff=0)
archivoMenu.add_cascade(label="Nuevo")
archivoMenu.add_cascade(label="Guardar")
archivoMenu.add_cascade(label="Guardar como")
archivoMenu.add_separator()
archivoMenu.add_cascade(label="Cerrar", command=cerrarDocumento)
archivoMenu.add_cascade(label="Salir", command=salirAplicacion)

archivoEdicion=Menu(barraMenu, tearoff=0)
archivoEdicion.add_cascade(label="Copiar")
archivoEdicion.add_cascade(label="Cortar")
archivoEdicion.add_cascade(label="Pegar")
archivoEdicion.add_separator()
archivoEdicion.add_cascade(label="Ajustes")
archivoEdicion.add_cascade(label="Tools")

archivoHerramientas=Menu(barraMenu, tearoff=0)

archivoAyuda=Menu(barraMenu, tearoff=0)
archivoAyuda.add_cascade(label="Licencia", command=avisoLicencia)
archivoAyuda.add_cascade(label="Acerca de...", command=infoAdicional)

barraMenu.add_cascade(label="Archivo", menu=archivoMenu)

barraMenu.add_cascade(label="Edicion", menu=archivoEdicion)

barraMenu.add_cascade(label="Herramientas", menu=archivoHerramientas)

barraMenu.add_cascade(label="Ayuda", menu=archivoAyuda)

home.mainloop()