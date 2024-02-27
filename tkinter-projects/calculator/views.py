from tkinter import *
from tkinter import ttk

class View(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        answer_label = Label(self, background="green")
        answer_label.pack()



    