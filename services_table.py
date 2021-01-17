import tkinter as tk
from tkinter import font as tkFont
from tkinter import ttk

# Window/Root Setup
window = tk.Tk()
window.title('App')
window.geometry('800x700')
window.config(bg="#283346")

my_tree = ttk.Treeview(window)

# Creating A Table, Columns & Headings
my_tree['columns'] = ("Name", "URL")
# Columns
my_tree.column("#0", width=20)
my_tree.column("Name", width=150)
my_tree.column("URL",  width=80)

# Headings
my_tree.heading("#0",text="ID")
my_tree.heading("Name",text="Name")
my_tree.heading("URL",text="URL")

my_tree.place(relx=.6, rely=.3, anchor="c") # End Of Table

window.mainloop()