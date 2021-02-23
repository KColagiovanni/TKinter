from tkinter import *
import sqlite3

root = Tk()
root.title("Health Tracker")
root.geometry("400x400")

global db_name
db_name = 'codemy.db'

conn = sqlite3.connect(db_name)
c = conn.cursor()
c.execute("SHOW DATABASES")
for db in c:
    print(db)
#c.execute("CREATE DATABASE" + db_name)
conn.commit()
conn.close()


root.mainloop()