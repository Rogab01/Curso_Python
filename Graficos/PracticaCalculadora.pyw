from tkinter import *

home=Tk()
home.title("Calculadora")

miFrame=Frame(home)

miFrame.pack()

operacion=""

resultado=0


#------------------- PANTALLA ---------------------------------

numeroPantalla=StringVar()

pantalla=Entry(miFrame, textvariable=numeroPantalla)
pantalla.grid(row=1, column=1, padx=10,pady=10, columnspan=4)
pantalla.config(background="black", fg="#03f943", justify="right")

#------------------- PULSACIONES DEL TECLADO ------------------

def numeroPulsado(num):

	global operacion

	if operacion!="":
		
		numeroPantalla.set(num)

		operacion=""

	else:
		
		numeroPantalla.set(numeroPantalla.get() + num)

#------------------- PFUNCION SUMA-------------------------------

def suma(num):
	global operacion

	global resultado
	
	resultado+=int(num)

	operacion="suma"

	numeroPantalla.set(resultado)

#------------------- FUNCION EL RESULTADO-----------------------

def elResultado():
	
	global resultado
	
	numeroPantalla.set(resultado+int(numeroPantalla.get()))

	resultado=0


#------------------- PRIMERA FILA ------------------------------

boton7=Button(miFrame, text="7", width=3, command=lambda:numeroPulsado("7"))
boton7.grid(row=2, column=1)
boton8=Button(miFrame, text="8", width=3, command=lambda:numeroPulsado("8"))
boton8.grid(row=2, column=2)
boton9=Button(miFrame, text="9", width=3, command=lambda:numeroPulsado("9"))
boton9.grid(row=2, column=3)
botonDiv=Button(miFrame, text="/", width=3)
botonDiv.grid(row=2, column=4)

#------------------- SEGUNDA FILA -------------------------------

boton4=Button(miFrame, text="4", width=3, command=lambda:numeroPulsado("4"))
boton4.grid(row=3, column=1)
boton5=Button(miFrame, text="5", width=3, command=lambda:numeroPulsado("5"))
boton5.grid(row=3, column=2)
boton6=Button(miFrame, text="6", width=3, command=lambda:numeroPulsado("6"))
boton6.grid(row=3, column=3)
botonmULT=Button(miFrame, text="X", width=3)
botonmULT.grid(row=3, column=4)

#------------------- TERCERA FILA ---------------------------------

boton1=Button(miFrame, text="1", width=3, command=lambda:numeroPulsado("1"))
boton1.grid(row=4, column=1)
boton2=Button(miFrame, text="2", width=3, command=lambda:numeroPulsado("2"))
boton2.grid(row=4, column=2)
boton3=Button(miFrame, text="3", width=3, command=lambda:numeroPulsado("3"))
boton3.grid(row=4, column=3)
botonRest=Button(miFrame, text="-", width=3)
botonRest.grid(row=4, column=4)

#------------------- CUARTA FILA ------------------------------------

boton0=Button(miFrame, text="0", width=3, command=lambda:numeroPulsado("0"))
boton0.grid(row=5, column=1)
botonComa=Button(miFrame, text=",", width=3)
botonComa.grid(row=5, column=2)
botonIgual=Button(miFrame, text="=", width=3, command=lambda:elResultado())
botonIgual.grid(row=5, column=3)
botonSum=Button(miFrame, text="+", width=3,  command=lambda: suma(numeroPantalla.get()))
botonSum.grid(row=5, column=4)




home.mainloop()