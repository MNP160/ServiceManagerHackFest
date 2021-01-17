from tkinter import * 
from tkinter import ttk
from tkinter import Text

from PIL import Image,ImageTk, ImageOps

root = Tk()

# myLabel = Label(root, text="Dashboard")

root.geometry('600x500')

imge=Image.open("purple-red.jpg")
photo=ImageTk.PhotoImage(imge.resize((600, 500)))

lab=Label(image=photo)
lab.place(x=0,y=0)

title = Label(root, text="Log Data",width=25,font=("bold", 24), bg = 'purple', fg = 'white', relief = "groove")
title.place(relx=0.114,rely=0.2135)

my_tree = ttk.Treeview(root)

# Columns
my_tree['columns'] = ("Name", "URL","Status", "Time")

my_tree.column("#0", width=10)
my_tree.column("Name", anchor=W, width=200)
my_tree.column("URL", anchor=W, width=150)
my_tree.column("Status", anchor=CENTER, width=40)
my_tree.column("Time", anchor=CENTER, width=70)

# headings
my_tree.heading("#0",text="ID", anchor=W)
my_tree.heading("Name",text="Name", anchor=CENTER)
my_tree.heading("URL",text="URL", anchor=CENTER)
my_tree.heading("Status",text="Status", anchor=CENTER)
my_tree.heading("Time",text="Time", anchor=CENTER)

data = []

my_tree.insert(parent='', index='end',iid=0, text="", values=("Dobri", "localhost", 200,"2021"))

# my_tree.pack(pady=20)
my_tree.place(relx=0.12,rely=0.3)

login = Button(root, text="Back",relief="raised",width=5,font=("arial", 13), bg = "purple", fg='white',command = root.destroy)
login.place(x=500,y=400)

# Entry Boxes
# add_frame = Frame(root)
# add_frame.pack(pady=20)

# nl = Label(add_frame, text="Name")
# nl.grid(row=0, column=0)

# il = Label(add_frame,text="URL")
# il.grid(row=0, column=1)

# name_box = Entry(add_frame)
# name_box.grid(row=1, column=0)

# url_box = Entry(add_frame)
# url_box.grid(row=1, column=1)

# Add Record
# def add_record():
#     my_tree.insert(parent='', index='end',iid=0, text="", values=(name_box.get(), url_box.get(), 200,"2021"))

# Buttons
# add_records = Button(root, text="Add Service")
# add_records.pack(pady=20)


root.mainloop()