from tkinter import * 
from tkinter import ttk
from tkinter import Text
from db import *
import sched, time
from manager import query_services
from PIL import Image,ImageTk, ImageOps

root = Tk()
root.title('Bermuda Service Manager')
root.geometry('600x500')

notebook = ttk.Notebook(root)
notebook.pack()

imge=Image.open("purple-red.jpg")
photo=ImageTk.PhotoImage(imge.resize((600, 500)))

frame1 = Frame(notebook, width=600, height=500)
frame2 = Frame(notebook, width=600, height=500)

frame1.pack(fill="both", expand=1)
frame2.pack(fill="both", expand=1)

notebook.add(frame1, text="Logs")
notebook.add(frame2, text="Services")

lab1=Label(frame1, image=photo)
lab1.place(x=0,y=0)

lab2=Label(frame2, image=photo)
lab2.place(x=0,y=0)

title_logs = Label(frame1, text="Log Data",width=25,font=("bold", 24), bg = 'purple', fg = 'white', relief = "groove")
title_logs.place(relx=0.114,rely=0.1)

logs = ttk.Treeview(frame1)
#logs.place(relx=)
# Columns
logs['columns'] = ("Id","Name", "URL","Status", "Time")
logs.column("#0", width=0)
logs.column("Id", width=10)
logs.column("Name", anchor=W, width=70)
logs.column("URL", anchor=W, width=140)
logs.column("Status", anchor=CENTER, width=70)
logs.column("Time", anchor=CENTER, width=150)

# headings
logs.heading("#0", text='')  
logs.heading("Id",text="ID", anchor=W)
logs.heading("Name",text="Name", anchor=CENTER)
logs.heading("URL",text="URL", anchor=CENTER)
logs.heading("Status",text="Status", anchor=CENTER)
logs.heading("Time",text="Time", anchor=CENTER)

data = []
dblogs=get_all_logs()
counter=0
for log in dblogs:
    logs.insert(parent='', index='end',iid=counter, text="", values=(counter,log.get('name'), log.get('url'),log.get('status'), log.get('time')))
    counter+=1



# # my_tree.pack(pady=20)
logs.place(relx=0.5,rely=0.5, anchor='c', width=500, height=250)

title_serv = Label(frame2, text="Services",width=25,font=("bold", 24), bg = 'purple', fg = 'white', relief = "groove")
title_serv.place(relx=0.114,rely=0.1)

serv = ttk.Treeview(frame2)

# Creating A Table, Columns & Headings
serv['columns'] = ("Id","Name", "URL")
# Columns
serv.column("#0", width=0)
serv.column("Id",anchor=W, width=10)
serv.column("Name",anchor=W, width=100)
serv.column("URL", anchor=W, width=200)




# Headings
serv.heading("#0", text='')  
serv.heading("Id",text="ID")
serv.heading("Name",text="Name")
serv.heading("URL",text="URL")
dbservices=get_all_services()
count=0
for service in dbservices:
    serv.insert(parent='', index='end',iid=count, text="", values=(count,log.get('name'), log.get('url')))
    count+=1

serv.place(relx=0.5,rely=0.5, anchor='c') # End Of Table

quit = Button(root, text="Quit",relief="raised",width=5,font=("arial", 13), bg = "purple", fg='white',command = root.destroy)
quit.place(x=500,y=400)

root.mainloop()
starttime = time.time()
while True:
    query_services()
    time.sleep(600.0- ((time.time() - starttime) % 600.0))
