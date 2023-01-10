from tkinter import *
from PIL import ImageTk, Image
import tkinter as tk
import pytz
import time
from datetime import datetime
import tkinter.messagebox as MessageBox
import mysql.connector as mysql
import pymysql
from tkinter import messagebox

root = Tk()
root.title('Test')
root.geometry('1417x720')
root.resizable(False, False)
IST = pytz.timezone('Asia/Manila')

def connection():
    conn =pymysql.connect(
        host = 'localhost', user = 'root', password ='', db = 'student_info_db')
    return conn


def login(self):
    global f_name
    conn = connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM cs_students")
    results = cursor.fetchall()
    conn.commit()
    conn.close()
    f_name = str(f_name.get())
    greet = "Welcome Student: " + f_name.get()
    my_label = Label(root, text=greet, font=('Verdana', 18, 'bold'))
    my_label.place(x=800, y=520)
    if(f_name == "" or f_name == " "):
        messagebox.showinfo("Error", "Please Fill up all the fields")
        return
    else:
        try:
            conn = connection()
            cursor = conn.cursor()
            cursor.execute("SELECT f_name FROM cs_students")
            conn.commit() 
            conn.close()
        except:
            messagebox.showinfo("Error", "Student ID already Exists")
            return
        
    stud_numEntry.delete(0, 'end')
    #password.delete(0,'end')
    return results

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

bg = PhotoImage(file="./banner.png")

bg_label = Label(root, image=bg)
bg_label.place(x=0, y=0)


icon = Image.open("./icon.jpg")

#resize
resized = icon.resize((460,550), Image.ANTIALIAS)

#call
new_icon = ImageTk.PhotoImage(resized)


icon = ImageTk.PhotoImage(Image.open("./icon.jpg"))
icon_label = Label(image=new_icon)
icon_label.place(x=1, y=183)

label2 = tk.Label(root, text="ISU Student Login", font=('Verdana', 20, 'bold'))
label2.place(x=850,y=190)

Label(root, text="Student ID: ", font=('Verdana', 20)).place(x=480, y=300)

stud_numEntry = Entry(root, width=40, bd=2, font=('Verdana', 20))
stud_numEntry.place(x=670, y=300, height = 50)

#Label(root, text="Password: ", font=('Verdana', 20)).place(x=480, y=350)

#password = Entry(root, show="*", width=40, bd=2, font=('Verdana', 20))
#password.place(x=670, y=350, height = 50)

label_date_now = tk.Label(text="Current Date", font = 'Verdana 25 bold',bg="white")
label_date_now.place(x=670, y=390)


label_time_now = tk.Label(text="Current Time", font = 'Verdana 25', bg="white")
label_time_now.place(x=1100, y=390)




Button(text="Login", command=login, font=('Verdana', 20, 'bold'), width=11, height=1, bg='SpringGreen4').place(x=690, y=580, width=650)
#Button(text="Cancel",font=('Verdana', 20, 'bold'), width=11, height=1, bg='red').place(x=1100, y=500)

root.bind('<Return>', login)








update_clock()
root.mainloop()
