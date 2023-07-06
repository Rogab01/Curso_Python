from tkinter import *

home=Tk()

varOpcion=IntVar()

def imprimir():
	print(varOpcion.get())

Label(home, text="Genero:").pack()

Radiobutton(home, text="Masculino", variable=varOpcion, value=1, command=imprimir()).pack()

Radiobutton(home, text="Femenino", variable=varOpcion, value=2, command=imprimir()).pack()


home.mainloop()