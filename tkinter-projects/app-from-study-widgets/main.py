from tkinter import *
from tkinter import ttk

clicks = 0
button_width = 10

def button1_click():
    global clicks 
    clicks += 1
    button1["text"] = f"Clicks {clicks}"
    button1["width"] += button_width
    if clicks == 10:
        button1["state"] = DISABLED
        return
    

window = Tk()
window.geometry("500x300")
window.title("Widgets")

button1 = ttk.Button(text="Click me", command=button1_click, width=button_width)

button1.pack()

window.mainloop()