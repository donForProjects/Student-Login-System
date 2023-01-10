from tkinter import *
from PIL import ImageTk, Image
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import pymysql


root = Tk()

root.title("STUDENT REG")
root.geometry('1417x720')
root.resizable(False, False)
my_tree = ttk.Treeview(root)

bg = PhotoImage(file="./banner.png")

bg_label = Label(root, image=bg)
bg_label.place(x=0, y=0)

icon = Image.open("./icon.jpg")

#resize
resized = icon.resize((420,550), Image.ANTIALIAS)

#call
new_icon = ImageTk.PhotoImage(resized)


icon = ImageTk.PhotoImage(Image.open("./icon.jpg"))
icon_label = Label(image=new_icon)
icon_label.place(x=1, y=183)

ph1 = tk.StringVar()
ph2 = tk.StringVar()
ph3 = tk.StringVar()
ph4 = tk.StringVar()
ph5 = tk.StringVar()
ph6 = tk.StringVar()
ph7 = tk.StringVar()
ph8 = tk.StringVar()
ph9 = tk.StringVar()


def setph(word,num):
    if num == 1:
        ph1.set(word)
    if num == 2:
        ph2.set(word)
    if num == 3:
        ph3.set(word)
    if num == 4:
        ph4.set(word)
    if num == 5:
        ph5.set(word)
    if num == 6:
        ph6.set(word)
    if num == 7:
        ph7.set(word)
    if num == 8:
        ph8.set(word)
    if num == 9:
        ph9.set(word)


def connection():
    conn =pymysql.connect(
        host = 'localhost', user = 'root', password ='', db = 'student_info_db')
    return conn

def refreshTable():
    for i in my_tree.get_children():
        my_tree.delete(i)

    for array in read():
        my_tree.insert(parent='', index='end', iid=array,text="", values=(array), tags="orow")
    
    my_tree.tag_configure('orow', background="#EEEEEE", font=('Verdana', 10))
    my_tree.place(x=430, y=400)


def read():
    conn = connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM cs_students")
    results = cursor.fetchall()
    conn.commit()
    conn.close()
    return results


def register():
    stud_num = str(stud_numEntry.get())
    l_name = str(l_nameEntry.get())
    f_name = str(f_nameEntry.get())
    birth = str(birthEntry.get())
    address = str(addressEntry.get())
    phone = str(phoneEntry.get())
    dept = str(deptEntry.get())
    course = str(courseEntry.get())
    year = str(yearEntry.get())

    if(stud_num == "" or stud_num == " ") or (l_name == "" or l_name == " ") or (f_name == "" or f_name == " ") or (birth == "" or birth == " ") or (address == "" or address == " ") or (phone == "" or phone == " ") or (dept == "" or dept == " ") or (course == "" or course == " ") or (year == "" or year == " "):
        messagebox.showinfo("Error", "Please Fill up all the fields")
        return
    else:
        try:
            conn = connection()
            cursor = conn.cursor()
            cursor.execute("INSERT INTO cs_students VALUES('"+stud_num+"','"+l_name+"','"+f_name+"','"+birth+"','"+address+"','"+phone+"','"+dept+"','"+course+"','"+year+"')")
            conn.commit()
            conn.close()
        except:
            messagebox.showinfo("Error", "Student ID already Exists")
            return
    stud_numEntry.delete(0, 'end')
    l_nameEntry.delete(0, 'end')
    f_nameEntry.delete(0, 'end')
    birthEntry.delete(0, 'end')
    addressEntry.delete(0, 'end')
    phoneEntry.delete(0, 'end')
    deptEntry.delete(0, 'end')
    courseEntry.delete(0, 'end')
    yearEntry.delete(0, 'end')
    refreshTable()

def reset():
    desicion = messagebox.askquestion("Warning!", "Reset All Data?")
    if desicion != "yes":
        return
    else:
        try:
            conn = connection()
            cursor = conn.cursor()
            cursor.execute("DELETE FROM cs_students")
            conn.commit()
            conn.close()
        except:
            messagebox.showinfo("Error", "Sorry an Error occured")
            return
    refreshTable()

def delete():
    desicion = messagebox.askquestion("Deleting Data!", "Delete the data?")
    if desicion != "yes":
        return
    else:
        selected_item = my_tree.selection()[0]
        deleteData = str(my_tree.item(selected_item)['values'][0])
        try:
            conn = connection()
            cursor = conn.cursor()
            cursor.execute("DELETE FROM cs_students WHERE stud_num= '"+str(deleteData)+"'")
            conn.commit()
            conn.close()
        except:
            messagebox.showinfo("Error", "Sorry an Error occured")
            return
            
    refreshTable()

def update():
    selectedStudid = ""
    try:
        selected_item = my_tree.selection()[0]
        stud_num = str(my_tree.item(selected_item)['values'][0])
        l_name = str(my_tree.item(selected_item)['values'][1])
        f_name = str(my_tree.item(selected_item)['values'][2])
        birth = str(my_tree.item(selected_item)['values'][3])
        address = str(my_tree.item(selected_item)['values'][4])
        phone = str(my_tree.item(selected_item)['values'][5])
        dept = str(my_tree.item(selected_item)['values'][6])
        course = str(my_tree.item(selected_item)['values'][7])
        year = str(my_tree.item(selected_item)['values'][8])

        setph(stud_num, 1)
        setph(l_name, 2)
        setph(f_name, 3)
        setph(birth, 4)
        setph(address, 5)
        setph(phone, 6)
        setph(dept, 7)
        setph(course, 8)
        setph(year, 9)

    except:
        messagebox.showinfo("Error", "Sorry an Error occured")

    stud_num = str(stud_numEntry.get())
    l_name = str(l_nameEntry.get())
    f_name = str(f_nameEntry.get())
    birth = str(birthEntry.get())
    address = str(addressEntry.get())
    phone = str(phoneEntry.get())
    dept = str(deptEntry.get())
    course = str(courseEntry.get())
    year = str(yearEntry.get())

    if(stud_num == "" or stud_num == " ") or (l_name == "" or l_name == " ") or (f_name == "" or f_name == " ") or (birth == "" or birth == " ") or (address == "" or address == " ") or (phone == "" or phone == " ") or (dept == "" or dept == " ") or (course == "" or course == " ") or (year == "" or year == " "):
        messagebox.showinfo("Error", "Please Fill up all the fields")
        return
    else:
        try:
            conn = connection()
            cursor = conn.cursor()
            cursor.execute("UPDATE cs_students SET STUDID ='"+stud_num+"',LNAME = '"+l_name+"',FNAME = '"+f_name+"',BIRTH = '"+birth+"',ADDRESS = '"+address+"',PHONE = '"+phone+"',DEPT = '"+dept+"',COURSE = '"+course+"',YEAR = '"+year+"' WHERE STUDID = '"+selectedStudid+ "' '")
            stud_numEntry.delete(0, 'end')
            l_nameEntry.delete(0, 'end')
            f_nameEntry.delete(0, 'end')
            birthEntry.delete(0, 'end')
            addressEntry.delete(0, 'end')
            phoneEntry.delete(0, 'end')
            deptEntry.delete(0, 'end')
            courseEntry.delete(0, 'end')
            yearEntry.delete(0, 'end')
            conn.commit()
            conn.close()
        except:
            messagebox.showinfo("Error", "Please Select a Data Row")
            return
    refreshTable()


label2 = tk.Label(root, text="ISU Student Registration", font=('Verdana', 20, 'bold'))
label2.place(x=750,y=190)

Label(root, text="Student ID: ", font=('Verdana', 13)).place(x=430, y=250)

stud_numEntry = Entry(root, width=15, bd=2, font=('Verdana', 13), textvariable=ph1)
stud_numEntry.place(x=550, y=252, height = 25)

Label(root, text="Last Name: ", font=('Verdana', 13)).place(x=730, y=250)

l_nameEntry = Entry(root, width=20, bd=2, font=('Verdana', 13), textvariable=ph2)
l_nameEntry.place(x=850, y=252, height = 25)

Label(root, text="First Name: ", font=('Verdana', 13)).place(x=1080, y=250)

f_nameEntry = Entry(root, width=17, bd=2, font=('Verdana', 13), textvariable=ph3)
f_nameEntry.place(x=1200, y=252, height = 25)

Label(root, text="Birthday: ", font=('Verdana', 13)).place(x=430, y=300)

birthEntry = Entry(root, width=15, bd=2, font=('Verdana', 13), textvariable=ph4)
birthEntry.place(x=550, y=300, height = 25)
#birthEntry.insert(0, "MM/DD/YY")

Label(root, text="Address: ", font=('Verdana', 13)).place(x=730, y=300)

addressEntry = Entry(root, width=20, bd=2, font=('Verdana', 13), textvariable=ph5)
addressEntry.place(x=850, y=302, height = 25)

Label(root, text="Phone: ", font=('Verdana', 13)).place(x=1100, y=300)

phoneEntry = Entry(root, width=17, bd=2, font=('Verdana', 13), textvariable=ph6)
phoneEntry.place(x=1200, y=302, height = 25)

Label(root, text="Department: ", font=('Verdana', 13)).place(x=430, y=350)

#label3 = Label(root, text="Department", font=('Verdana', 13)).place(x=430, y=350)
#stud_dep = ttk.Combobox(root,font=('Verdana', 8), state='readonly', value=["CCSICT", "EDUCATION", "CBM", "CJE", "SAS"])
#stud_dep.set(" ---Select Department---")
#stud_dep.place(x=550, y=350, height = 27, width=169)

#Label(root, text="Department: ", font=('Verdana', 13)).place(x=430, y=350)

deptEntry = Entry(root, width=15, bd=2, font=('Verdana', 13), textvariable=ph7)
deptEntry.place(x=550, y=350, height = 25)

Label(root, text="Course: ", font=('Verdana', 13)).place(x=730, y=350)

courseEntry = Entry(root, width=20, bd=2, font=('Verdana', 13), textvariable=ph8)

#course = ttk.Combobox(root,font=('Verdana', 10), state='readonly', value=["1", "2", "3", "4", "5"])
#course.set("    ---Select Course/Major--")
courseEntry.place(x=850, y=350, height = 25, width=230)

Label(root, text="Year: ", font=('Verdana', 13)).place(x=1100, y=350)

yearEntry = Entry(root, width=17, bd=2, font=('Verdana', 13), textvariable=ph9)
yearEntry.place(x=1200, y=350, height = 27)


Button(text="Register", command=register, font=('Verdana', 20, 'bold'), width=10, height=1, bg='SpringGreen4').place(x=450, y=650)

Button(text="Update", command=update, font=('Verdana', 20, 'bold'), width=10, height=1, bg='SpringGreen4').place(x=700, y=650)

Button(text="Delete",command=delete, font=('Verdana', 20, 'bold'), width=10, height=1, bg='firebrick3').place(x=950, y=650)

Button(text="Reset", command=reset, font=('Verdana', 20, 'bold'), width=10, height=1, bg='firebrick3').place(x=1190, y=650)



style = ttk.Style()
style.configure("Treeview.Heading", font=('Verdana', 9, 'bold'))

my_tree['columns'] = ("Student ID", "Last Name", "First Name", "Birthday", "Address", "Phone", "Department", "Course", "Year")

my_tree.column("#0", width=0, stretch=NO)
my_tree.column("Student ID", anchor=CENTER, width=85)
my_tree.column("Last Name", anchor=CENTER, width=110)
my_tree.column("First Name", anchor=CENTER, width=120)
my_tree.column("Birthday", anchor=CENTER, width=100)
my_tree.column("Address", anchor=CENTER, width=120)
my_tree.column("Phone", anchor=CENTER, width=110)
my_tree.column("Department", anchor=CENTER, width=120)
my_tree.column("Course", anchor=CENTER, width=130)
my_tree.column("Year", anchor=CENTER, width=70)

my_tree.heading("Student ID", text="Student ID", anchor=CENTER)
my_tree.heading("Last Name", text="Last Name", anchor=CENTER)
my_tree.heading("First Name", text="First Name", anchor=CENTER)
my_tree.heading("Birthday", text="Birthday", anchor=CENTER)
my_tree.heading("Address", text="Address", anchor=CENTER)
my_tree.heading("Phone", text="Phone Number", anchor=CENTER)
my_tree.heading("Department", text="Department", anchor=CENTER)
my_tree.heading("Course", text="Course", anchor=CENTER)
my_tree.heading("Year", text="Year", anchor=CENTER)





root.bind('<Return>', register)
root.bind('<Delete>', delete)
refreshTable()
root.mainloop()