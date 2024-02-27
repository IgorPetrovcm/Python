from tkinter import *
from tkinter import ttk

window = Tk()
window.title("Packer")

frame1 = Frame(window, width=150, height=150, bg="green")
frame2 = Frame(window, width=150, height=150, bg="blue")
frame3 = Frame(window, width=150, height=300, bg="red")

frame1.place(relx=0,rely=0,relwidth=0.5,relheight=0.5)
frame2.place(relx=0,rely=0.5,relwidth=0.5,relheight=0.5)
frame3.place(relx=0.5,rely=0,relwidth=0.5,relheight=1)


window.mainloop()