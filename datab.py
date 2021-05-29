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
