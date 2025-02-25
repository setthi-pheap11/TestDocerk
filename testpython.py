import tkinter as tk
from tkinter import messagebox

def show_entry_fields():
    messagebox.showinfo('Message', 'Hello %s, you are %s years old' % (e1.get(), e2.get()))
master = tk.Tk()
tk.Label(master, text='Name').grid(row=0)
tk.Label(master, text='Age').grid(row=1)
e1 = tk.Entry(master)
e2 = tk.Entry(master)
e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
tk.Button(master, text='Quit', command=master.quit).grid(row=3, column=0, sticky=tk.W, pady=4)
tk.Button(master, text='Show', command=show_entry_fields).grid(row=3, column=1, sticky=tk.W, pady=4)
tk.mainloop()
