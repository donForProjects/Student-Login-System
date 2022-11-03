import tkinter as tk
import pytz
import time
from datetime import datetime
import sqlite3

root = tk.Tk()

root.geometry('1280x720')
root.title("Student Login")
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



label_date_now = tk.Label(text="Current Date", font = 'Verdana 25 bold',bg="white")
label_date_now.place(x=550, y=400)


label_time_now = tk.Label(text="Current Time", font = 'Verdana 50', bg="white")
label_time_now.place(x=430, y=300)




def display_text():
   global textbox
   string= textbox.get('1.0', 'end')
   label.configure(text=string)
   #label3.configure(text=string) #can put here for text/ displaying text 



def submit():
    textbox.delete('1.0', tk.END) #okayy na Dditoo potaaaa
    label3.delete('1 .0', tk.END) #use get()
    stud_course.delete('1.0', tk.END)
    stud_year.delete('1.0', tk.END)
    label5.delete('1.0', tk.END)




#Try changing to grids instead of packs
label2 = tk.Label(root, text="ISU Student Login", font=('Verdana', 20, 'bold'))
label2.pack(padx=20, pady=20)

stud_num = tk.Label(root, text="Student Number", font=('Verdana', 15, 'bold'))
stud_num.place(x=100, y=480)

label = tk.Label(root, text="", justify="center", font=('Verdana', 15, 'bold'))
label.place(x=100, y=520)

stud_name = tk.Label(root, text="Student Name", font=('Verdana', 15, 'bold'))
stud_name.place(x=350, y=480)

label3 = tk.Label(root, text="", font=('Verdana', 15))
label3.place(x=350, y=520)

stud_course = tk.Label(root, text="Course", font=('Verdana', 15, 'bold'))
stud_course.place(x=600, y=480)

label4 = tk.Label(root, text="", font=('Verdana', 15))
label4.place(x=600, y=520)

stud_year = tk.Label(root, text="Year", font=('Verdana', 15, 'bold' ))
stud_year.place(x=800, y=480)

label5 = tk.Label(root, text="", font=('Verdana', 15))
label5.place(x=850, y=520)

stud_year = tk.Label(root, text="Timed In", font=('Verdana', 15, 'bold' ))
stud_year.place(x=950, y=480)

label5 = tk.Label(root, text="", font=('Verdana', 15))
label5.place(x=950, y=520)



textbox = tk.Text(root, height=2, font=('Verdana', 16))
textbox.pack(padx=10, pady=10, fill='x')
#entry= tk.Entry(root, width=100, font=('Verdana', 25, 'bold'))
#entry.focus_set()
#entry.place(x=10, y =180)



#center the text in textbox potangina mo (FIX THIS)
textbox.tag_configure('center', justify='center')
textbox.insert('1.0', ' ')#space = fills open space
textbox.tag_add('center', '1.0', 'end')



buttonframe = tk.Frame(root)
buttonframe.columnconfigure(0, weight=1)
buttonframe.columnconfigure(1, weight=1)


btn1 = tk.Button(buttonframe, text="Login",command=display_text,  font=('Verdana', 20, 'bold'))
btn1.grid(row=0, column=0, sticky=tk.W+tk.E)


btn2 = tk.Button(buttonframe, text="Register", command=submit, font=('Verdana', 20, 'bold'))
btn2.place(x=700, y=0, width=600)


buttonframe.pack(fill='x') #stretch the buttons







#DATABASE USING SQLITE3

#CREATING DB

#conn = sqlite3.connect('student_info.db')

#cur = conn.cursor()

#res = cur.execute("SELECT name From sqlite_master")
#res.fetchone()

#cur.execute("""CREATE TABLE studentInfo (

#    student_id text,
#    student_name text,
#    student_course text,
#    student_year text,
#    timed_in text)""")







#conn.commit()

#conn.close()




update_clock()
root.mainloop()