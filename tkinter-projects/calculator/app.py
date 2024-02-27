from tkinter import *
from tkinter import ttk
from views import *

class App(Tk):
    def __init__(self):
        super().__init__()

        self.geometry("300x360")

        self.title("calculator")

        view = View(self)
        view.grid(row=0,column=0, columnspan=4, sticky=NSEW)

