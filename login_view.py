from tkinter import *
from tkinter import Text


from PIL import Image,ImageTk

root = Tk()
root.geometry('600x500')
root.title("Bermuda Login")

imge=Image.open("purple-red.jpg")
photo=ImageTk.PhotoImage(imge.resize((600, 500)))

lab=Label(image=photo)
lab.pack()



email=StringVar()
password=StringVar()
    

login = Button(root, text="Login",relief="raised",width=5,font=("arial", 13), bg = "purple", fg='white')
login.place(x=430,y=330)


label_1 = Label(root, text="Email ",width=10,font=("bold", 15), bg = 'purple', fg = 'white', relief = "groove")
label_1.place(x=120,y=240)

entry_1 = Entry(root,textvar=email, font=("arial", 14))
entry_1.place(x=240,y=241)


label_2 = Label(root, text="Password ",width=10,font=("bold", 15), bg = 'purple', fg = 'white', relief = "groove")
label_2.place(x=120,y=280)

entry_2 = Entry(root,textvar=password, font=("arial", 14))
entry_2.place(x=240,y=281)

root.mainloop()