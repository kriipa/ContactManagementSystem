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
    global fname, lname, gender, address, contact
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
    LeftViewForm = Frame(display_screen, width=500, bg="#72938c")
    LeftViewForm.pack(side=LEFT, fill=Y)
    # mid frame for displaying lnames record
    MidViewForm = Frame(display_screen, width=600)
    MidViewForm.pack(side=RIGHT)
    # label for heading
    lbl_text = Label(TopViewForm, text="Contact Management System", font=('verdana', 18), width=600, bg="#72938c",
                     fg="white")
    lbl_text.pack(fill=X)
    # creating registration form in first left frame
    Label(rForm, text="First Name  ", font=("Arial", 12), bg="#72938c", fg="white").pack(side=TOP)
    Entry(rForm, font=("Arial", 10, "bold"), textvariable=fname).pack(side=TOP, padx=10, fill=X)
    Label(rForm, text="Last Name ", font=("Arial", 12), bg="#72938c", fg="white").pack(side=TOP)
    Entry(rForm, font=("Arial", 10, "bold"), textvariable=lname).pack(side=TOP, padx=10, fill=X)
    Label(rForm, text="Gender ", font=("Arial", 12), bg="#72938c", fg="white").pack(side=TOP)
    # Entry(LFrom, font=("Arial", 10, "bold"),textvariable=gender).pack(side=TOP, padx=10, fill=X)
    gender.set("Select Gender")
    content = {'Male', 'Female'}
    OptionMenu(rForm, gender, *content).pack(side=TOP, padx=10, fill=X)


    Label(rForm, text="Address ", font=("Arial", 12), bg="#15244C", fg="white").pack(side=TOP)
    Entry(rForm, font=("Arial", 10, "bold"), textvariable=address).pack(side=TOP, padx=10, fill=X)
    Label(rForm, text="Contact ", font=("Arial", 12), bg="#15244C", fg="white").pack(side=TOP)
    Entry(rForm, font=("Arial", 10, "bold"), textvariable=contact).pack(side=TOP, padx=10, fill=X)
    Button(rForm, text="Submit", font=("Arial", 10, "bold"), command=register, bg="#15244C",
           fg="white").pack(side=TOP, padx=10, pady=5, fill=X  )


    # creating search label and entry in second frame

    lbl_txtsearch = Label(LeftViewForm, text="Enter Name to Search", font=('BlackChancery', 10), bg="#eed5d2")
    lbl_txtsearch.pack()
    # creating search entry
    search = Entry(LeftViewForm, textvariable=SEARCH, font=('verdana', 15), width=10)
    search.pack(side=TOP, padx=10, fill=X)
    # creating search button
    btn_search = Button(LeftViewForm, text="Search", command=SearchRecord, bg="cyan")
    btn_search.pack(side=TOP, padx=10, pady=10, fill=X)
    # creating view button
    btn_view = Button(LeftViewForm, text="View All", command=DisplayData, bg="cyan")
    btn_view.pack(side=TOP, padx=10, pady=10, fill=X)
    # creating reset button
    btn_reset = Button(LeftViewForm, text="Reset", command=Reset, bg="cyan")
    btn_reset.pack(side=TOP, padx=10, pady=10, fill=X)
    # creating delete button
    btn_delete = Button(LeftViewForm, text="Delete", command=Delete, bg="cyan")
    btn_delete.pack(side=TOP, padx=10, pady=10, fill=X)
    # create update button
    btn_delete = Button(LeftViewForm, text="Update", command=Update, bg="cyan")
    btn_delete.pack(side=TOP, padx=10, pady=10, fill=X)
    # setting scrollbar
    scrollbarx = Scrollbar(MidViewForm, orient=HORIZONTAL)
    scrollbary = Scrollbar(MidViewForm, orient=VERTICAL)
    tree = ttk.Treeview(MidViewForm, columns=("Student Id", "Name", "Contact", "Email", "Rollno", "Branch"),
                        selectmode="extended", height=100, yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
    scrollbary.config(command=tree.yview)
    scrollbary.pack(side=RIGHT, fill=Y)
    scrollbarx.config(command=tree.xview)
    scrollbarx.pack(side=BOTTOM, fill=X)
    # setting headings for the columns
    tree.heading('Student Id', text="Id", anchor=W)
    tree.heading('Name', text="FirstName", anchor=W)
    tree.heading('Contact', text="LastName", anchor=W)
    tree.heading('Email', text="Gender", anchor=W)
    tree.heading('Rollno', text="Address", anchor=W)
    tree.heading('Branch', text="Contact", anchor=W)
    # setting width of the columns
    tree.column('#0', stretch=NO, minwidth=0, width=0)
    tree.column('#1', stretch=NO, minwidth=0, width=100)
    tree.column('#2', stretch=NO, minwidth=0, width=150)
    tree.column('#3', stretch=NO, minwidth=0, width=80)
    tree.column('#4', stretch=NO, minwidth=0, width=120)
    tree.pack()
    DisplayData()


# calling function
displayForm()
mainloop()
