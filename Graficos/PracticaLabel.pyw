from tkinter import *

home=Tk()

miFrame=Frame(home, width=650, height=550)

miFrame.pack()

miImagen=PhotoImage(file="4.png")


Label(miFrame,image=miImagen).place(x=100, y=200)

#Label(miFrame,text="Hola Alumnos de curso Python", fg="red", font=("comic Sans MS",18)).place(x=100, y=200)
















home.mainloop()