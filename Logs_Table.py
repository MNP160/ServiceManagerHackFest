from tkinter import * 
from tkinter import ttk
from tkinter.ttk import *

# Root Setup
root = Tk()
root.title('App')
root.geometry('1000x800')
root.config(bg="#283346")
my_tree = ttk.Treeview(root)

# Style Setup
style = ttk.Style()


# my_tree = ttk.Treeview(root)
# style.configure("BW.TButton", fg="#49837c", bg="#000000")
#style.configure("BW.TLabel", foreground="yellow", background="black")

# b = ttk.Button(text="Example button ttk", style = "BW.TButton")
# b.pack()
# label = ttk.Label(root, text="Hello World", style = "BW.TLabel")
# label.pack()

# Dashboard Label & Setting
# style.configure("BW.TLabel")
#dashboardLabel = ttk.Label(root, text="Dashboard", style="BW.TLabel")
dashboardLabel = Label(root,  text="Dashboard",  font=('Helvetica', 22))

dashboardLabel.pack(pady=20)


# Creating A Table + Columns & Headings
my_tree['columns'] = ("Name", "URL","Status", "Time")
# Columns
my_tree.column("#0", width=20)
my_tree.column("Name", anchor=CENTER, width=150)
my_tree.column("URL", anchor=CENTER, width=80)
my_tree.column("Status", anchor=CENTER, width=50)
my_tree.column("Time", anchor=CENTER, width=50)

# Headings
my_tree.heading("#0",text="ID", anchor=W)
my_tree.heading("Name",text="Name", anchor=CENTER)
my_tree.heading("URL",text="URL", anchor=CENTER)
my_tree.heading("Status",text="Status", anchor=CENTER)
my_tree.heading("Time",text="Time", anchor=CENTER)

my_tree.pack() # End Of Table

root.mainloop()