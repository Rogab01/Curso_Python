from tkinter import *
from tkinter import filedialog

home=Tk()

def abreFichero():
	fichero=filedialog.askopenfilename(title="Abrir",initialdir="C:", filetypes=(("Ficheros de Excel","*.xlsx"),("Ficheros de Texto","*.txt"),("Todos los Ficheros","*.*")))
	print(fichero)

Button(home,text="Abrir ficero", command=abreFichero).pack()

home.mainloop()
