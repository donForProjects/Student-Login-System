from tkinter import *
import tkinter as tk

root = Tk()

root.geometry("700x700")

L1 = Label(text="enter your name: ", font=('Verdana', 10, 'bold'))
L1.grid(row=0, column=0)

#E1 = Entry(root, bg="white", fg="black", bd=10,font=('Verdana', 10, 'bold'))
#E1.grid(row=0, column=1)

textbox = tk.Text(root, bg="white",fg="black",font=('Verdana', 10, 'bold'))
textbox.grid(row=0, column=1)


def C1():
    L2 = Label(root, text=textbox.get())
    L2.grid(row=3, column=0)
    font = ('Verdane', 15)

B1 = Button(root, text="ok", font=('Verdana', 10, 'bold'), command=C1 )
B1.grid(row=2, column=1)

root.mainloop()