from tkinter import * 

raiz=Tk()

raiz.title("Ventana de pruebas")

#raiz.resizable(0,0)

raiz.iconbitmap("favicon.ico")

#raiz.geometry("650x350")

raiz.config(bg="blue")

miFrame=Frame()

miFrame.pack(fill="both", expand="True")

miFrame.config(bg="red")

miFrame.config(width="650",height="350")

raiz.mainloop()