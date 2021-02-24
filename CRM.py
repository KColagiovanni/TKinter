#Import everything from TKinter
from tkinter import *
from tkinter import ttk
import mysql.connector
from PIL import ImageTk, Image
import csv

#Create the main window first, the root widget
root = Tk()
#Change the root window title
root.title("Customer Relation Management")
#Provide the path to the icon image
root.iconbitmap('C:/Users/kcola/Pictures/Images/Icons/Blue_Target.ico')
#Define a fixed window size
root.geometry("400x600")

mydb = mysql.connector.connect(
    host = "192.168.0.55",
    user = "kevin",
    passwd = "cz4167kc",
    database = "Kevin_TKinter_Stuff"
)

#print(mydb)
my_cursor = mydb.cursor()

#Create a database (If this is run everytime, the same database will be created everytime)
#my_cursor.execute("CREATE DATABASE Kevin_TKinter_Stuff")

#Show databases
#my_cursor.execute("SHOW DATABASES")
#for db in my_cursor:
#    print(db)

#To create a new table (If this is ran everytime, the same table will be created everytime without the if statement)
my_cursor.execute("CREATE TABLE IF NOT EXISTS customers ( \
    first_name VARCHAR(255), \
    last_name VARCHAR(255), \
    zipcode INT(10), \
    price_paid DECIMAL(10, 2), \
    user_id INT AUTO_INCREMENT PRIMARY KEY)")

#Alter a table
"""
my_cursor.execute("ALTER TABLE customers ADD( \
    email VARCHAR(255), \
    address_1 VARCHAR(255), \
    address_2 VARCHAR(255), \
    city VARCHAR(50), \
    state VARCHAR(50), \
    country VARCHAR(255), \
    phone VARCHAR(255), \
    payment_method VARCHAR(50), \
    discount_code VARCHAR(255))")
"""
#my_cursor.execute("SELECT * FROM customers")
#print(my_cursor.description)

#for item in my_cursor.description:
#    print(item)

#Clear all of the fields
def clear_fields():
    first_name_box.delete(0, END)
    last_name_box.delete(0, END)
    address1_box.delete(0, END)
    address2_box.delete(0, END)
    city_box.delete(0, END)
    state_box.delete(0, END)
    zipcode_box.delete(0, END)
    country_box.delete(0, END)
    phone_box.delete(0, END)
    email_box.delete(0, END)
    payment_method_box.delete(0, END)
    discount_code_box.delete(0, END)
    price_paid_box.delete(0, END)

def write_to_csv(result):
    with open('C:/Users/kcola/Documents/Programing Fun/Python/GUI/TKinter GUI Practice/customers.csv', 'a') as f:
        w = csv.writer(f, dialect = 'excel')
        for record in result:
            w.writerow(result)

def search_customers():
    search_customers = Tk()
    search_customers.title("Search Customers")
    search_customers.iconbitmap('C:/Users/kcola/Pictures/Images/Icons/Blue_Target.ico')
    search_customers.geometry("1300x800")

    def update():
        sql_command = """UPDATE customers SET first_name = %s,
        last_name = %s,
        zipcode = %s,
        price_paid = %s,
        email = %s,
        address_1 = %s,
        address_2 = %s,
        city = %s,
        state = %s,
        country = %s,
        phone = %s,
        payment_method = %s,
        discount_code = %s WHERE user_id = %s
         """

        first_name = first_name_box2.get()
        last_name = last_name_box2.get()
        zipcode = zipcode_box2.get()
        price_paid = price_paid_box2.get()
        email = email_box2.get()
        address_1 = address1_box2.get()
        address_2 = address2_box2.get()
        city = city_box2.get()
        state = state_box2.get()
        country = country_box2.get()
        phone = phone_box2.get()
        payment_method = payment_method_box2.get()
        discount_code = discount_code_box2.get()

        id_value = id_box2.get()
        inputs = (first_name,
        last_name,
        zipcode,
        price_paid,
        email,
        address_1,
        address_2,
        city,
        state,
        country,
        phone,
        payment_method,
        discount_code,
        id_value)

        my_cursor.execute(sql_command, inputs)
        mydb.commit()
        search_customers.destroy()

    def edit_now(id, index):
        sql2 = "SELECT * FROM customers WHERE user_id = %s"
        name2 = (id, )
        result2 = my_cursor.execute(sql2, name2)
        result2 = my_cursor.fetchall()
        print(result2)

        first_name_lbl = Label(search_customers, text = "First Name:").grid(row = index + 3, column = 0, padx = 10, pady = 10, sticky = W)
        last_name_lbl = Label(search_customers, text = "Last Name:").grid(row = index + 4, column = 0, padx = 10, sticky = W)
        address1_lbl = Label(search_customers, text = "Address 1:").grid(row = index + 5, column = 0, padx = 10, sticky = W)
        address2_lbl = Label(search_customers, text = "Address 2:").grid(row = index + 6, column = 0, padx = 10, sticky = W)
        city_lbl = Label(search_customers, text = "City:").grid(row = index + 7, column = 0, padx = 10, sticky = W)
        state_lbl = Label(search_customers, text = "State:").grid(row = index + 8, column = 0, padx = 10, sticky = W)
        zipcode_lbl = Label(search_customers, text = "Zipcode:").grid(row = index + 9, column = 0, padx = 10, sticky = W)
        country_lbl = Label(search_customers, text = "Country:").grid(row = index + 10, column = 0, padx = 10, sticky = W)
        phone_lbl = Label(search_customers, text = "Phone Number:").grid(row = index + 11, column = 0, padx = 10, sticky = W)
        email_lbl = Label(search_customers, text = "Email Address:").grid(row = index + 12, column = 0, padx = 10, sticky = W)
        payment_method_lbl = Label(search_customers, text = "Payment Method:").grid(row = index + 13, column = 0, padx = 10, sticky = W)
        discount_code_lbl = Label(search_customers, text = "Discount Code:").grid(row = index + 14, column = 0, padx = 10, sticky = W)
        price_paid_lbl = Label(search_customers, text = "Price Paid:").grid(row = index + 15, column = 0, padx = 10, sticky = W)
        id_lbl = Label(search_customers, text = "User ID").grid(row = index + 16, column = 0, padx = 10, sticky = W)

        global first_name_box2
        first_name_box2 = Entry(search_customers)
        first_name_box2.grid(row = index + 3, column = 1, pady = 10)
        first_name_box2.insert(0, result2[0][0])

        global last_name_box2
        last_name_box2 = Entry(search_customers)
        last_name_box2.grid(row = index + 4, column = 1, pady = 5)
        last_name_box2.insert(0, result2[0][1])

        global address1_box2
        address1_box2 = Entry(search_customers)
        address1_box2.grid(row = index + 5, column = 1, pady = 5)
        address1_box2.insert(0, result2[0][6])

        global address2_box2
        address2_box2 = Entry(search_customers)
        address2_box2.grid(row = index + 6, column = 1, pady = 5)
        address2_box2.insert(0, result2[0][7])

        global city_box2
        city_box2 = Entry(search_customers)
        city_box2.grid(row = index + 7, column = 1, pady = 5)
        city_box2.insert(0, result2[0][8])

        global state_box2
        state_box2 = Entry(search_customers)
        state_box2.grid(row = index + 8, column = 1, pady = 5)
        state_box2.insert(0, result2[0][9])

        global zipcode_box2
        zipcode_box2 = Entry(search_customers)
        zipcode_box2.grid(row = index + 9, column = 1, pady = 5)
        zipcode_box2.insert(0, result2[0][2])

        global country_box2
        country_box2 = Entry(search_customers)
        country_box2.grid(row = index + 10, column = 1, pady = 5)
        country_box2.insert(0, result2[0][10])

        global phone_box2
        phone_box2 = Entry(search_customers)
        phone_box2.grid(row = index + 11, column = 1, pady = 5)
        phone_box2.insert(0, result2[0][11])

        global email_box2
        email_box2 = Entry(search_customers)
        email_box2.grid(row = index + 12, column = 1, pady = 5)
        email_box2.insert(0, result2[0][5])

        global payment_method_box2
        payment_method_box2 = Entry(search_customers)
        payment_method_box2.grid(row = index + 13, column = 1, pady = 5)
        payment_method_box2.insert(0, result2[0][12])

        global discount_code_box2
        discount_code_box2 = Entry(search_customers)
        discount_code_box2.grid(row = index + 14, column = 1, pady = 5)
        discount_code_box2.insert(0, result2[0][13])

        global price_paid_box2
        price_paid_box2 = Entry(search_customers)
        price_paid_box2.grid(row = index + 15, column = 1, pady = 5)
        price_paid_box2.insert(0, result2[0][3])

        global id_box2
        id_box2 = Entry(search_customers)
        id_box2.grid(row = index + 16, column = 1, pady = 5)
        id_box2.insert(0, result2[0][4])

        save_record_btn = Button(search_customers, text = "Update", command = update)
        save_record_btn.grid(row = index + 17, column = 0, padx = 10)

    def search_now():
        selected = drop.get()
        if selected == "Search by...":
            test = Label(search_customers, text = "You forgot to pick a drop down option")
            test.grid(row = 2, column = 0)
        if selected == "Last Name":
#            test = Label(search_customers, text = "You picked last name")
#            test.grid(row = 2, column = 0)
            sql = "SELECT * FROM customers WHERE last_name = %s"
        if selected == "Email Address":
#            test = Label(search_customers, text = "You picked email")
#            test.grid(row = 2, column = 0)
            sql = "SELECT * FROM customers WHERE email = %s"
        if selected == "Customer ID":
#            test = Label(search_customers, text = "You picked Customer ID")
#            test.grid(row = 2, column = 0)
            sql = "SELECT * FROM customers WHERE user_id = %s"
        searched = search_box.get()
#        sql = "SELECT * FROM customers WHERE last_name = %s"
        name = (searched, )
        result = my_cursor.execute(sql, name)
        result = my_cursor.fetchall()

        if not result:
            test.destroy()
            result = 'Record not found!'
            searched_lbl = Label(search_customers, text = result)
            searched_lbl.grid(row = 2, column = 0)
        else:
            for index, x in enumerate(result):
                num = 0
                index += 2
                id_reference = str(x[4])
                edit_btn = Button(search_customers, text = "Edit", command = lambda: edit_now(id_reference, index))
                edit_btn.grid(row = index + 1, column = num)
                for y in x:
                    searched_lbl = Label(search_customers, text = y)
                    searched_lbl.grid(row = index + 1, column = num + 1)
                    num += 1
            csv_btn = Button(search_customers, text = "Save to CSV", command = lambda: write_to_csv(result))
            csv_btn.grid(row = index + 2, column = 0)

#        searched_lbl = Label(search_customers, text = result)
#        searched_lbl.grid(row = 3, column = 0, padx = 10)

    search_box = Entry(search_customers)
    search_box.grid(row = 0, column = 1, padx = 10, pady = 10)

    search_box_lbl = Label(search_customers, text = "Search")
    search_box_lbl.grid(row = 0, column = 0, padx = 10, pady = 10)
    search_btn = Button(search_customers, text = "Search Customers", command = search_now)
    search_btn.grid(row = 1, column = 0, padx = 10)
    drop = ttk.Combobox(search_customers, value = ["Search by...", "Last Name", "Email Address", "Customer ID"])
    drop.current(0)
    drop.grid(row = 0, column = 2)

def list_customers():
    list_customers_query = Tk()
    list_customers_query.title("List All Customers")
    list_customers_query.iconbitmap('C:/Users/kcola/Pictures/Images/Icons/Blue_Target.ico')
    list_customers_query.geometry("800x600")
    my_cursor.execute("SELECT * FROM customers")
    result = my_cursor.fetchall()
    for index, x in enumerate(result):
        num = 0
        for y in x:
            display_lbl = Label(list_customers_query, text = y)
            display_lbl.grid(row = index + 1, column = num)
            num += 1
    csv_btn = Button(list_customers_query, text = "Save to CSV", command = lambda: write_to_csv(result))
    csv_btn.grid(row = index + 2, column = 0)

#Insert data into the database
def add_customer():
    sql_command = "INSERT INTO customers (\
        first_name, \
        last_name, \
        zipcode, \
        price_paid, \
        email, \
        address_1, \
        address_2, \
        city, \
        state, \
        country, \
        phone, \
        payment_method, \
        discount_code) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"

    values = (first_name_box.get(),
     last_name_box.get(), 
     zipcode_box.get(),
     price_paid_box.get(),
     email_box.get(),
     address1_box.get(),
     address2_box.get(),
     city_box.get(),
     state_box.get(),
     country_box.get(),
     phone_box.get(),
     payment_method_box.get(),
     discount_code_box.get())

    #Execute the command with the values
    my_cursor.execute(sql_command, values)
    #Commit the changes to the database
    mydb.commit()
    #Clear the fields after the changes have been commited
    clear_fields()

title_lbl = Label(root, text = "Customer Database", font = ("Helvetica", 16))
title_lbl.grid(row = 0, column = 0, columnspan = 2, pady = 10)

first_name_lbl = Label(root, text = "First Name:").grid(row = 1, column = 0, padx = 10, sticky = W)
last_name_lbl = Label(root, text = "Last Name:").grid(row = 2, column = 0, padx = 10, sticky = W)
address1_lbl = Label(root, text = "Address 1:").grid(row = 3, column = 0, padx = 10, sticky = W)
address2_lbl = Label(root, text = "Address 2:").grid(row = 4, column = 0, padx = 10, sticky = W)
city_lbl = Label(root, text = "City:").grid(row = 5, column = 0, padx = 10, sticky = W)
state_lbl = Label(root, text = "State:").grid(row = 6, column = 0, padx = 10, sticky = W)
zipcode_lbl = Label(root, text = "Zipcode:").grid(row = 7, column = 0, padx = 10, sticky = W)
country_lbl = Label(root, text = "Country:").grid(row = 8, column = 0, padx = 10, sticky = W)
phone_lbl = Label(root, text = "Phone Number:").grid(row = 9, column = 0, padx = 10, sticky = W)
email_lbl = Label(root, text = "Email Address:").grid(row = 10, column = 0, padx = 10, sticky = W)
payment_method_lbl = Label(root, text = "Payment Method:").grid(row = 11, padx = 10, sticky = W)
discount_code_lbl = Label(root, text = "Discount Code:").grid(row = 12, padx = 10, sticky = W)
price_paid_lbl = Label(root, text = "Price Paid:").grid(row = 13, padx = 10, sticky = W)

first_name_box = Entry(root)
first_name_box.grid(row = 1, column = 1)
last_name_box = Entry(root)
last_name_box.grid(row = 2, column = 1, pady = 5)
address1_box = Entry(root)
address1_box.grid(row = 3, column = 1, pady = 5)
address2_box = Entry(root)
address2_box.grid(row = 4, column = 1, pady = 5)
city_box = Entry(root)
city_box.grid(row = 5, column = 1, pady = 5)
state_box = Entry(root)
state_box.grid(row = 6, column = 1, pady = 5)
zipcode_box = Entry(root)
zipcode_box.grid(row = 7, column = 1, pady = 5)
country_box = Entry(root)
country_box.grid(row = 8, column = 1, pady = 5)
phone_box = Entry(root)
phone_box.grid(row = 9, column = 1, pady = 5)
email_box = Entry(root)
email_box.grid(row = 10, column = 1, pady = 5)
payment_method_box = Entry(root)
payment_method_box.grid(row = 11, column = 1, pady = 5)
discount_code_box = Entry(root)
discount_code_box.grid(row = 12, column = 1, pady = 5)
price_paid_box = Entry(root)
price_paid_box.grid(row = 13, column = 1, pady = 5)

add_customer_btn = Button(root, text = "Add Customer to Database", command = add_customer)
add_customer_btn.grid(row = 14, column = 0, padx = 10, pady = 10)
clear_fields_button = Button(root, text = "Clear Fields", command = clear_fields)
clear_fields_button.grid(row = 14, column = 1)
list_customers_btn = Button(root, text = "List Customers", command = list_customers)
list_customers_btn.grid(row = 15, column = 0, sticky = W, padx = 10)
search_customers_btn = Button(root, text = "Search/Edit Customers", command = search_customers)
search_customers_btn.grid(row = 15, column = 1, sticky = W, padx = 10)

root.mainloop()