from tkinter import *
from tkinter import ttk

window = Tk()
window.title("First App")
window.geometry("500x600+700+250")
window.minsize(400,450)
window.maxsize(550,600)

icon = PhotoImage(file="source/calculator-icon.png")
window.iconphoto(True, icon)

label1 = ttk.Label(text="Hello World")
label1.pack()

button1 = ttk.Button()
button1["text"] = "Click"
button1.pack()

def get_all_info(widget):
    w_class = widget.winfo_class()
    w_width = widget.winfo_width()
    w_height = widget.winfo_height()
    w_x = widget.winfo_x()
    w_y = widget.winfo_y()
    
    print(f"{w_class} width={w_width} height={w_height} x={w_x} y={w_y}")

    for child in widget.winfo_children():
        get_all_info(child)

window.update()

get_all_info(window)

window.mainloop()