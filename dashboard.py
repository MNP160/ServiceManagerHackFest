import tkinter as tk
from tkinter import font as tkFont
from tkinter import ttk

# Window/Root Setup
window = tk.Tk()
window.title('App')
window.geometry('800x700')
window.config(bg="#283346")

my_tree = ttk.Treeview(window)

# style = tk.Style()

# Button
# style.configure('W.TButton', font =('calibri', 14, 'bold', 'underline'),foreground = 'green', background='green')
# button = Button(root, text="Add New", style="W.TButton")
# button.pack()

# dashboardLabel = Label(root,  text="Services",  font=('Helvetica', 22))
# dashboardLabel.pack(pady=20)

#-----Fonts & Styles-------
helv = tkFont.Font(family='Helvetica', size=12, weight='bold')
dashboard_Font = tkFont.Font(family="Sans-Serif", size=20, weight='bold')

#-----LABEL------
label1 = tk.Label(text="DashBoard", bg='#283346', fg="#fff")
label1['font'] = dashboard_Font
label1.place(anchor="center", x=100, y=50)

#------BUTTONS------
button_1 = tk.Button(text="Log Tables")
button_1['font'] = helv
button_1.place(relx=.1, rely=.21, anchor="c")

button_2 = tk.Button(text="Services")
button_2['font'] = helv
button_2.place(relx=.1, rely=.3, anchor="c")

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