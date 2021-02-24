#Import everything from TKinter
from tkinter import *
from PIL import ImageTk, Image

#Create the main window first, the root widget
root = Tk()

#Change the root window title
root.title("Root Window")
root.iconbitmap('C:/Users/kcola/Pictures/Images/Icons/Blue_Target.ico')
#Define a fixed window size
root.geometry("400x400")

#Create an integer variable and if a box is checked the value is 1 and 0 otherwise
#If using StringVar, when checked and unchecked values can be defined
#var = IntVar()
var = StringVar()

#Create a check box if using "StringVar" above, you can define onvalue and offvalue
c = Checkbutton(root, text = "Check me", variable = var, onvalue = "Checked", offvalue = "Not Checked")
#Use this so the check box is not selected by default
c.deselect()
c.pack()

#Define a function to display the check box value
def check():
    #Label to display check box value

    lbl = Label(root, text = var.get()).pack()

#Create a button to show the check box selection value
checked_btn = Button(root, text = "Select", command = check).pack()

#root window exit button
button_exit = Button(root, text = "Close", command = root.destroy)
button_exit.pack()

root.mainloop()