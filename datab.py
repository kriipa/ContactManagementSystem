# function to define database
def Database():
    global conn, cursor
    # creating contact database
    conn = sqlite3.connect("contact.db")
    cursor = conn.cursor()
    # creating REGISTRATION table
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS REGISTRATION (RID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, FNAME TEXT, LNAME TEXT, GENDER TEXT, ADDRESS TEXT, CONTACT TEXT)")

def register():
    Database()
    # getting form data
    fname1 = fname.get()
    lname1 = lname.get()
    gender1 = gender.get()
    address1 = address.get()
    contact1 = contact.get()
    # applying empty validation
    if fname1 == '' or lname1 == '' or gender1 == '' or address1 == '' or contact1 == '':
        tkMessageBox.showinfo("Warning", "fill the empty field!!!")
    else:
        # execute query
        conn.execute('INSERT INTO REGISTRATION (FNAME,LNAME,GENDER,ADDRESS,CONTACT) \
              VALUES (?,?,?,?,?)', (fname1, lname1, gender1, address1, contact1))
        conn.commit()
        tkMessageBox.showinfo("Message", "Stored successfully")
        # refresh table data
        DisplayData()
        conn.close()

def Delete():
    # open database
    Database()
    if not tree.selection():
        tkMessageBox.showwarning("Warning", "Select data to delete")
    else:
        result = tkMessageBox.askquestion('Confirm', 'Are you sure you want to delete this record?',
                                          icon="warning")
        if result == 'yes':
            curItem = tree.focus()
            contents = (tree.item(curItem))
            selecteditem = contents['values']
            tree.delete(curItem)
            cursor = conn.execute("DELETE FROM REGISTRATION WHERE RID = %d" % selecteditem[0])
            conn.commit()
            cursor.close()
            conn.close()


# function to search data
def SearchRecord():
    # open database
    Database()
    # checking search text is empty or not
    if SEARCH.get() != "":
        # clearing current display data
        tree.delete(*tree.get_children())
        # select query with where clause
        cursor = conn.execute("SELECT * FROM REGISTRATION WHERE FNAME LIKE ?", ('%' + str(SEARCH.get()) + '%',))
        # fetch all matching records
        fetch = cursor.fetchall()
        # loop for displaying all records into GUI
        for data in fetch:
            tree.insert('', 'end', values=(data))
        cursor.close()
        conn.close()

# defining function to access data from SQLite database
def DisplayData():
    # open database
    Database()
    # clear current data
    tree.delete(*tree.get_children())
    # select query
    cursor = conn.execute("SELECT * FROM REGISTRATION")
    # fetch all data from database
    fetch = cursor.fetchall()
    # loop for displaying all data in GUI
    for data in fetch:
        tree.insert('', 'end', values=data)
        tree.bind("<Double-1>", OnDoubleClick)
    cursor.close()
    conn.close()



# function to update data into database
def Update():
    Database()
    # getting form data
    fname1 = fname.get()
    lname1 = lname.get()
    gender1 = gender.get()
    address1 = address.get()
    contact1 = contact.get()
    # applying empty validation
    if fname1 == '' or lname1 == '' or gender1 == '' or address1 == '' or contact1 == '':
        tkMessageBox.showinfo("Warning", "fill the empty field!!!")
    else:
        # getting selected data
        curItem = tree.focus()
        contents = (tree.item(curItem))
        selecteditem = contents['values']
        # update query
        conn.execute('UPDATE REGISTRATION SET FNAME=?,LNAME=?,GENDER=?,ADDRESS=?,CONTACT=? WHERE RID = ?'
                     , (fname1, lname1, gender1, address1, contact1, selecteditem[0]))
        conn.commit()
        tkMessageBox.showinfo("Message", "Updated successfully")
        # reset form
        Reset()
        # refresh table data
        DisplayData()
        conn.close()

