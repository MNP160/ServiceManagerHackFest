from tkinter import *
from tkinter import Text

from PIL import Image,ImageTk, ImageOps

root = Tk()
root.geometry('600x500')
root.title("Bermuda Login")

imge=Image.open("purple-red.jpg")
photo=ImageTk.PhotoImage(imge.resize((600, 500)))

lab=Label(image=photo)
lab.place(x=0,y=0)

icon = Image.open("icon.jpg")
icon = ImageOps.fit(icon, (90, 90))
icon = ImageTk.PhotoImage(icon)
mylabel = Label(root, image=icon)

mylabel.place(x=265,y=100,height=90,width=90)

email=StringVar()
password=StringVar()

label_1 = Label(root, text="Email ",width=10,font=("bold", 15), bg = 'purple', fg = 'white', relief = "groove")
label_1.place(x=120,y=240)

entry_1 = Entry(root,textvar=email, font=("arial", 14))
entry_1.place(x=240,y=241)


label_2 = Label(root, text="Password ",width=10,font=("bold", 15), bg = 'purple', fg = 'white', relief = "groove")
label_2.place(x=120,y=280)

entry_2 = Entry(root,textvar=password, font=("arial", 14))
entry_2.place(x=240,y=281)

vld_label = Label(root, text = "Invalid email address or password",width=27,font=("ariel", 10), bg = '#ede7a0', fg = 'black', relief = "solid", borderwidth = 1)

# Validate User
def validate():
    
    email_v = email.get()
    pass_v = password.get()
    
    if email_v == 'test' and pass_v == 'test':
         root.destroy() # To Change
    else:
        vld_label.place(x=242,y=315)

login = Button(root, text="Login",relief="raised",width=5,font=("arial", 13), bg = "purple", fg='white',command = validate)
login.place(x=430,y=340)

print

root.mainloop()