from tkinter import *
from PIL import ImageTk, Image
import tkinter as tk
import pytz
import time
from datetime import datetime

root = Tk()
root.title('Test')
root.geometry('1417x720')
IST = pytz.timezone('Asia/Manila')

def update_clock():
    raw_TS = datetime.now(IST)
    date_now = raw_TS.strftime("%d %b %Y")
    time_now = raw_TS.strftime("%I:%M:%S %p")
    formatted_now = raw_TS.strftime("%d-%m-%Y")
    label_date_now.config(text = date_now)
    # label_date_now.after(500, update_clock)
    label_time_now.config(text = time_now)
    label_time_now.after(1000, update_clock)
    return formatted_now

bg = PhotoImage(file="Student-Login-System/banner.png")

bg_label = Label(root, image=bg)
bg_label.place(x=0, y=0)


icon = Image.open("Student-Login-System/icon.jpg")

#resize
resized = icon.resize((460,550), Image.ANTIALIAS)

#call
new_icon = ImageTk.PhotoImage(resized)


icon = ImageTk.PhotoImage(Image.open("Student-Login-System/icon.jpg"))
icon_label = Label(image=new_icon)
icon_label.place(x=1, y=183)

label2 = tk.Label(root, text="ISU Student Login", font=('Verdana', 20, 'bold'))
label2.place(x=850,y=190)

Label(root, text="Student ID: ", font=('Verdana', 20)).place(x=480, y=250)

stud_id = Entry(root, width=40, bd=2, font=('Verdana', 20))
stud_id.place(x=670, y=250, height = 50)

Label(root, text="Password: ", font=('Verdana', 20)).place(x=480, y=350)

password = Entry(root, show="*", width=40, bd=2, font=('Verdana', 20))
password.place(x=670, y=350, height = 50)

label_date_now = tk.Label(text="Current Date", font = 'Verdana 25 bold',bg="white")
label_date_now.place(x=670, y=420)


label_time_now = tk.Label(text="Current Time", font = 'Verdana 25', bg="white")
label_time_now.place(x=1100, y=420)



def login(self):
    greet = "Welcome Student: " + stud_id.get()
    my_label = Label(root, text=greet, font=('Verdana', 18, 'bold'))
    stud_id.delete(0, 'end')
    password.delete(0,'end')
    my_label.place(x=800, y=520)
    Label(text='Login Successfully',font=('Verdana', 15, 'bold'), fg='green').place(x=670, y=670)






Button(text="Login", command=login, font=('Verdana', 20, 'bold'), width=11, height=1, bg='green').place(x=670, y=600)
Button(text="Cancel",font=('Verdana', 20, 'bold'), width=11, height=1, bg='red').place(x=1100, y=600)

root.bind('<Return>', login)








update_clock()
root.mainloop()
