from tkinter import *


root = Tk()

root.title("STUDENT REG")
root.geometry('1280x720')
root.resizable(True, True)

def register():
    student_id = idValue.get()
    l_name = lnameValue.get()
    f_name = fnameValue.get()
    b_day = birthValue.get()
    address_loc = addressValue.get()
    stud_phone = phoneValue.get()
    stud_dept = deptValue.get()
    stud_course = courseValue.get()
    stud_year = yearValue.get()

    #saves as txt file

    file = open (l_name + " " + f_name + ".txt", "w")
    file.write(student_id + "\n")
    file.write(l_name + "\n")
    file.write(f_name + "\n")
    file.write(b_day + "\n")
    file.write(address_loc + "\n")
    file.write(stud_phone + "\n")
    file.write(stud_dept + "\n")
    file.write(stud_course + "\n")
    file.write(stud_year + "\n")
    file.close()

    Label(text='Registered Succesfully',font=('Verdana', 15, 'bold')).place(x=430, y=660)


Label(root, text = "ISU STUDENT REGISTRATION FORM", font=('Verdana', 20, 'bold')).pack(pady = 50)

Label(root, text="Student ID: ", font=('Verdana', 15)).place(x=100, y=150)
Label(root, text="Last Name: ", font=('Verdana', 15)).place(x=100, y=200)
Label(root, text="First Name: ", font=('Verdana', 15)).place(x=100, y=250)
Label(root, text="Birthday: ", font=('Verdana', 15)).place(x=100, y=300)
Label(root, text="Address: ", font=('Verdana', 15)).place(x=100, y=350)
Label(root, text="Phone Number: ", font=('Verdana', 15)).place(x=100, y=400)
Label(root, text="Department: ", font=('Verdana', 15)).place(x=100, y=450)
Label(root, text="Course: ", font=('Verdana', 15)).place(x=100, y=500)
Label(root, text="Year: ", font=('Verdana', 15)).place(x=100, y=550)

idValue = StringVar()
lnameValue = StringVar()
fnameValue = StringVar()
birthValue = StringVar()
addressValue = StringVar()
phoneValue = StringVar()
deptValue = StringVar()
courseValue = StringVar()
yearValue = StringVar()

stud_id = Entry(root, textvariable=idValue, width=50, bd=2, font=15)
stud_id.place(x=300, y=150)

lname = Entry(root, textvariable=lnameValue, width=50, bd=2, font=15)
lname.place(x=300, y=200)

fname = Entry(root, textvariable=fnameValue, width=50, bd=2, font=15)
fname.place(x=300, y=250)

birth = Entry(root, textvariable=birthValue, width=50, bd=2, font=15)
birth.place(x=300, y=300)

address = Entry(root, textvariable=addressValue, width=50, bd=2, font=15)
address.place(x=300, y=350)

phone = Entry(root, textvariable=phoneValue, width=50, bd=2, font=15)
phone.place(x=300, y=400)

dept = Entry(root, textvariable=deptValue, width=50, bd=2, font=15)
dept.place(x=300, y=450)

course = Entry(root, textvariable=courseValue, width=50, bd=2, font=15)
course.place(x=300, y=500)

year = Entry(root, textvariable=yearValue, width=50, bd=2, font=15)
year.place(x=300, y=550)


Button(text="Register",font=('Verdana', 20, 'bold'), width=11, height=1, command=register).place(x=450, y=600)



root.mainloop()