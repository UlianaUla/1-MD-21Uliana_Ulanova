from tkinter import *

window=Tk()
window.title("Мороженое-кафе")

name=Label(window,text="Ванильное мороженое",font=('Arial Bold',14))
name1=Label(window,text="Шоколадное мороженое",font=('Arial Bold',14))
name2=Label(window,text="Клубничное мороженое",font=('Arial Bold',14))
name.grid(column=0,row=0)
name1.grid(column=1,row=0)
name2.grid(column=2,row=0)

window.mainloop()
