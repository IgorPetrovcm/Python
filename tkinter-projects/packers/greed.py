from tkinter import *
from tkinter import ttk

window = Tk()
window.geometry("250x200")
window.title("greed")

'''for i in range(3):
    window.columnconfigure(index=i, weight=1)
for i in range(3):
    window.rowconfigure(index=i, weight=1)

for i in range(3):
    for j in range(3):
        btn = ttk.Button(text=f"{i}.{j}")
        btn.grid(column=i, row=j, padx=5, pady=0, ipady=0, ipadx=0)'''

window.columnconfigure(index=0, weight=1)
window.columnconfigure(index=1, weight=1)

window.rowconfigure(index=0, weight=1)
window.rowconfigure(index=1, weight=1)

btn1 = ttk.Button(text="btn1")
btn1.grid(row=0, column=0, columnspan=2, sticky=NSEW)

btn2 = ttk.Button(text="btn1")
btn2.grid(row=1, column=0, sticky=NSEW)

btn3 = ttk.Button(text="btn1")
btn3.grid(row=1, column=1, sticky=NSEW)

window.mainloop()