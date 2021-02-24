#Import everything from TKinter
from tkinter import *
from PIL import ImageTk, Image
import sqlite3
from tkinter import messagebox

global db_name
global table_name
db_name = "address_book.db"
table_name = "addresses"

#Create the main window first, the root widget
root = Tk()

#Change the root window title
root.title("Root Window")
root.iconbitmap('C:/Users/kcola/Pictures/Images/Icons/Blue_Target.ico')
#Define a fixed window size
root.geometry("365x250")

#Create a db or connect to one that already exists
db = sqlite3.connect(db_name)

#Create cursor
cursor = db.cursor()

#Create a table (the table gets added to the same directory that this program is in)
#ONLY USE THE BELOW COMMAND IF THE DB HASN'T BEEN CREATED YET

#cursor.execute("""CREATE TABLE table_name (
#        first_name text,
#        last_name text,
#        address text,
#        city text,
#        state text,
#        zipcode integer)
#""")

#Create a function to deete a record
def delete():
    #Create a db or connect to one that already exists
    db = sqlite3.connect(db_name)
    #Create cursor
    cursor = db.cursor()

    #If the field is empty show a warning
    if not key.get():
        messagebox.showwarning("Missing Data", "You need to specify a value in the 'Record ID:' field")
        return

    cursor.execute("DELETE from " + table_name + " WHERE oid = " + key.get())

    #Commit db changes
    db.commit()
    #Close the db connection
    db.close()
    key.delete(0, END)

#Define the function to handle what happens when the submit button is clicked
def submit():
    #Create a db or connect to one that already exists
    db = sqlite3.connect(db_name)
    #Create cursor
    cursor = db.cursor()

    #Insert into table
    cursor.execute("INSERT INTO " + table_name + " VALUES(:f_name, :l_name, :address, :city, :state, :zip)",
        {
            'f_name': f_name.get(),
            'l_name': l_name.get(),
            'address': address.get(),
            'city' : city.get(),
            'state': state.get(),
            'zip':zip.get()
        })

    #Commit db changes
    db.commit()
    #Close the db connection
    db.close()
    #Clear the text boxes
    f_name.delete(0, END)
    l_name.delete(0, END)
    address.delete(0, END)
    city.delete(0, END)
    state.delete(0, END)
    zip.delete(0, END)

#Define a function to save the updated changes
def save_update():
    #Create a db or connect to one that already exists
    db = sqlite3.connect(db_name)
    #Create cursor
    cursor = db.cursor()

    record_id = key.get()
    
    cursor.execute("""UPDATE """ + table_name + """ SET
        first_name = :first,
        last_name = :last,
        address = :address,
        city = :city,
        state = :state,
        zipcode = :zip 
        
        WHERE oid = :oid""",
        {
        'first' : f_name_edit.get(),
        'last' : l_name_edit.get(),
        'address' : address_edit.get(),
        'city' : city_edit.get(),
        'state' : state_edit.get(),
        'zip' : zip_edit.get(),
        'oid' : record_id
        })
        
    #Commit db changes
    db.commit()
    #Close the db connection
    db.close()

    #Update window exit button
    update_win.destroy()
    
#Define the update function
def update():
    global update_win

    #If the field is empty show a warning
    if not key.get():
        messagebox.showwarning("Missing Data", "You need to specify a value in the 'Record ID:' field")
        return

    #Open a new window
    update_win = Tk()
    update_win.title("Update a Record")
    update_win.iconbitmap('C:/Users/kcola/Pictures/Images/Icons/Blue_Target.ico')
    update_win.geometry("365x200")

    #Create a db or connect to one that already exists
    db = sqlite3.connect(db_name)
    #Create cursor
    cursor = db.cursor()

    #Insert into table
    record_id = key.get()
    cursor.execute("SELECT * FROM " + table_name + " WHERE oid = " + record_id)
    qry_lbl = cursor.fetchall()

    #Create labels to show the field names
    f_lbl = Label(update_win, text = "First Name:")
    f_lbl.grid(row = 0, column = 0, pady = (10, 0))

    l_lbl = Label(update_win, text = "Last Name:")
    l_lbl.grid(row = 1, column = 0)

    address_lbl = Label(update_win, text = "Address:")
    address_lbl.grid(row = 2, column = 0)

    city_lbl = Label(update_win, text = "City:")
    city_lbl.grid(row = 3, column = 0)

    state_lbl = Label(update_win, text = "State:")
    state_lbl.grid(row = 4, column = 0)

    zip_lbl = Label(update_win, text = "Zipcode:")
    zip_lbl.grid(row = 5, column = 0)

#    key_lbl = Label(root, text = "Record ID:")
#    key_lbl.grid(row = 6, column = 0)

    global f_name_edit
    global l_name_edit
    global address_edit
    global city_edit
    global state_edit
    global zip_edit

    #Create input boxes to get the user input
    f_name_edit = Entry(update_win, width = 30)
    f_name_edit.grid(row = 0, column = 1, columnspan = 2, padx = 20, pady = (10, 0))

    l_name_edit = Entry(update_win, width = 30)
    l_name_edit.grid(row = 1, column = 1, columnspan = 2, padx = 20)

    address_edit = Entry(update_win, width = 30)
    address_edit.grid(row = 2, column = 1, columnspan = 2, padx = 20)

    city_edit = Entry(update_win, width = 30)
    city_edit.grid(row = 3, column = 1, columnspan = 2, padx = 20)

    state_edit = Entry(update_win, width = 30)
    state_edit.grid(row = 4, column = 1, columnspan = 2, padx = 20)

    zip_edit = Entry(update_win, width = 30)
    zip_edit.grid(row = 5, column = 1, columnspan = 2, padx = 20)

#    key_edit = Entry(root, width = 30)
#    key_edit.grid(row = 6, column = 1, columnspan = 2, padx = 20)

    #Loop throught results
    for record in qry_lbl:
        f_name_edit.insert(0, record[0])
        l_name_edit.insert(0, record[1])
        address_edit.insert(0, record[2])
        city_edit.insert(0, record[3])
        state_edit.insert(0, record[4])
        zip_edit.insert(0, record[5])
#    cursor.execute("DELETE  from " + table_name + " WHERE oid = " + key.get())

    #Commit db changes
    db.commit()
    #Close the db connection
    db.close()

    #Create a button to save the record
    save_win_btn = Button(update_win, text = "Update Record", command = save_update)
    save_win_btn.grid(row = 7, column = 1, pady = 10, padx = 10, ipadx = 38)


#Define the query function
def query():
    top = Toplevel()
    top.title("Query Result")

    #Create a db or connect to one that already exists
    db = sqlite3.connect(db_name)
    #Create cursor
    cursor = db.cursor()

    #Insert into table
    cursor.execute("SELECT *, oid FROM " + table_name)
#    cursor.fetchmany(50)#to fetch (x) amount of records
    qry_lbl = cursor.fetchall()
    print_records = ''
    for record in qry_lbl:
        print_records += str(record[6]) + " " + record[0] + " " + record[1] + " " + record[2] + " " + record[3] + " " + record[4] + " " + str(record[5]) + "\n"

    qry_lbl = Label(top, text = print_records)
    qry_lbl.grid(row = 0, column = 0)

    #top window exit button
    top_button_exit = Button(top, text = "Close", command = top.destroy)
    top_button_exit.grid(row = 7, column = 0, pady = 10, padx = 10, ipadx = 15)

    #Commit db changes
    db.commit()
    #Close the db connection
    db.close()


#Create input boxes to get the user input
f_name = Entry(root, width = 30)
f_name.grid(row = 0, column = 1, columnspan = 2, padx = 20, pady = (10, 0))

l_name = Entry(root, width = 30)
l_name.grid(row = 1, column = 1, columnspan = 2, padx = 20)

address = Entry(root, width = 30)
address.grid(row = 2, column = 1, columnspan = 2, padx = 20)

city = Entry(root, width = 30)
city.grid(row = 3, column = 1, columnspan = 2, padx = 20)

state = Entry(root, width = 30)
state.grid(row = 4, column = 1, columnspan = 2, padx = 20)

zip = Entry(root, width = 30)
zip.grid(row = 5, column = 1, columnspan = 2, padx = 20)

#Create an input box to take the primary key of a specific row
key = Entry(root, width = 30)
key.grid(row = 6, column = 1, columnspan = 2, padx = 20)


#Create labels to show the field names
f_lbl = Label(root, text = "First Name:")
f_lbl.grid(row = 0, column = 0, pady = (10, 0))

l_lbl = Label(root, text = "Last Name:")
l_lbl.grid(row = 1, column = 0)

address_lbl = Label(root, text = "Address:")
address_lbl.grid(row = 2, column = 0)

city_lbl = Label(root, text = "City:")
city_lbl.grid(row = 3, column = 0)

state_lbl = Label(root, text = "State:")
state_lbl.grid(row = 4, column = 0)

zip_lbl = Label(root, text = "Zipcode:")
zip_lbl.grid(row = 5, column = 0)

key_lbl = Label(root, text = "Record ID:")
key_lbl.grid(row = 6, column = 0)


#Create a submit button
sub_btn = Button(root, text = "Add Record to datebase", command = submit)
sub_btn.grid(row = 7, column = 1, columnspan = 2, pady = 10, padx = 10, ipadx = 15)

#Create a delete button
delete_btn = Button(root, text = "Delete a Record", command = delete)
delete_btn.grid(row = 8, column = 2, pady = 10, padx = 2, ipadx = 0)

#Create an uodate button
update_btn = Button(root, text = "Update a Record", command = update)
update_btn.grid(row = 8, column = 1, pady = 10, padx = 2, ipadx = 0)

#Create a Query button
qry_btn = Button(root, text = "Show Records", command = query)
qry_btn.grid(row = 7, column = 0, pady = 10, padx = 10, ipadx = 15)

#root window exit button
button_exit = Button(root, text = "Close", command = root.destroy)
button_exit.grid(row = 8, column = 0, pady = 10, padx = 10, ipadx = 38)

#Commit db changes
db.commit()

#Close the db connection
db.close()

root.mainloop()