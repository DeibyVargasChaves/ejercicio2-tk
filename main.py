import tkinter as tk

window = tk.Tk()

window.columnconfigure(0, weight=1)
window.columnconfigure(0, weight=3)

label_color = tk.Label(window, text="elegir color", bg='blue', fg='white')
label_color.grid(column=0, row=1, sticky=tk.W, padx=5, pady=5)

Lista = ['rojo', 'verde', 'azul', 'amarillo']
lista_item = tk.StringVar(value=Lista)
listbox = tk.Listbox(window, height=4, listvariable=lista_item)
listbox.grid(column=0, row=2, sticky=tk.W, padx=5, pady=5)
window.mainloop()
