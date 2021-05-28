# import libraries
from tkinter import *
import tkinter.ttk as ttk
import tkinter.messagebox as tkMessageBox
import sqlite3

# defining function for creating GUI Layout
def displayForm():
    # creating window
    display_screen = Tk()
    # setting width and height for window
    display_screen.geometry("900x400")
    # setting title for window
    display_screen.title("python project")
    global tree
    global SEARCH
    global fname,lname,gender,address,contact
    SEARCH = StringVar()
    fname = StringVar()
    lname = StringVar()
    gender = StringVar()
    address = StringVar()
    contact = StringVar()
    # creating frames for layout
    # topview frame for heading
    TopViewForm = Frame(display_screen, width=600, bd=1, relief=SOLID)
    TopViewForm.pack(side=TOP, fill=X)
    # right frame for registration from
    rForm = Frame(display_screen, width="350", bg="#72938c")
    rForm.pack(side=RIGHT, fill=Y)
    # left frame for search form
    LeftViewForm = Frame(display_screen, width=500,bg="#72938c")
    LeftViewForm.pack(side=LEFT, fill=Y)
    #mid frame for displaying lnames record
    MidViewForm = Frame(display_screen, width=600)
    MidViewForm.pack(side=RIGHT)
    #label for heading
    lbl_text = Label(TopViewForm, text="Contact Management System", font=('verdana', 18), width=600,bg="#72938c",fg="white")
    lbl_text.pack(fill=X)
    #creating registration form in first left frame
    Label(rForm, text="First Name  ", font=("Arial", 12),bg="#72938c",fg="white").pack(side=TOP)
    Entry(rForm,font=("Arial",10,"bold"),textvariable=fname).pack(side=TOP, padx=10, fill=X)
    Label(rForm, text="Last Name ", font=("Arial", 12),bg="#72938c",fg="white").pack(side=TOP)
    Entry(rForm, font=("Arial", 10, "bold"),textvariable=lname).pack(side=TOP, padx=10, fill=X)
    Label(rForm, text="Gender ", font=("Arial", 12),bg="#72938c",fg="white").pack(side=TOP)
    #Entry(LFrom, font=("Arial", 10, "bold"),textvariable=gender).pack(side=TOP, padx=10, fill=X)
    gender.set("Select Gender")
    content={'Male','Female'}
    OptionMenu(rForm,gender,*content).pack(side=TOP, padx=10, fill=X)

#calling function
displayForm()
    mainloop()
