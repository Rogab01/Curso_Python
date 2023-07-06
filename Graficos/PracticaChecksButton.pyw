from tkinter import *

home=Tk()

home.title("Ejemplo")

playa=IntVar()

montagna=IntVar()

desierto=IntVar()

def opcionViaje():

	opcioEscogida=""

	if playa.get()==1:

		opcioEscogida+="Playa"

	if montagna.get()==1:

		opcioEscogida+="Montaña"

	if desierto.get()==1:

		opcioEscogida+="Desierto"

	textoFinal.config(text=opcioEscogida)


foto=PhotoImage(file="4.png")

Label(home,image=foto).pack()

frame=Frame(home)

frame.pack()

Label(frame, text="Elige tu destino", width=50).pack()

Checkbutton(frame, text="Playa", variable=playa, onvalue=1, offvalue=0, command=opcionViaje).pack()

Checkbutton(frame, text="Montaña", variable=montagna, onvalue=1, offvalue=0, command=opcionViaje).pack()

Checkbutton(frame, text="Desierto", variable=desierto, onvalue=1, offvalue=0, command=opcionViaje).pack()

textoFinal=Label(frame)

textoFinal.pack()



home.mainloop()