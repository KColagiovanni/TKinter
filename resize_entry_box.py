from tkinter import *

root = Tk()
root.title("")
root.iconbitmap("")
root.geometry("400x400")

my_label = Label(root)

def my_click():
    global my_label
    my_label.destroy()
    hello = "Hello " + e.get()
    my_label = Label(root, text = hello)
    e.delete(0, END)
    my_label.grid(row = 3, column = 0, pady = 10)

e = Entry(root, width = 20, font = ("helvetica", 14))
e.grid(row = 0, column = 0, padx = 10, pady = 10)

my_btn = Button(root, text = "Enter Your Name", command = my_click)
my_btn.grid(row = 1, column = 0, pady = 10)

root.mainloop()