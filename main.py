import tkinter
import tkinter as tk
from tkinter import ttk

window = tkinter.Tk()

window.columnconfigure(0, weight=1)
window.columnconfigure(0, weight=3)

label_color = tkinter.Label(window, text="elegir color", bg='blue', fg='white')
label_color.grid(column=0, row=1, sticky=tkinter.W, padx=5, pady=5)

lista = ['rojo', 'verde', 'azul', 'amarillo']
lista_item = tkinter.StringVar(value=lista)
listbox = tkinter.Listbox(window,height=4, listvariable=lista_item)
listbox.grid(column=0, row=2, sticky=tkinter.W, padx=5, pady=5)
window.mainloop()
