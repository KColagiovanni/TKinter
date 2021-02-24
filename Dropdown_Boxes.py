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

#Define the variable for the OptionMenu
selection = StringVar()
selection.set("Default")

#Define a function to handle the button click
def show_selection():
    lbl = Label(root, text = selection.get()).pack()

#A list can be used instead of manually typing all of the options into the OptionMenu call
options = ["Option 1", 
           "Option 2", 
           "Option 3", 
           "Option 4", 
           "Option 5"]

#Create a variable and define the dropdown box options or use a list
#drop = OptionMenu(root, selection, "Option 1", "Option 2", "Option 3", "Option 4", "Option 5").pack()
drop = OptionMenu(root, selection, *options).pack()

#Define a button to display the selection
btn = Button(root, text = "Select", command = show_selection).pack()

#root window exit button
button_exit = Button(root, text = "Close", command = root.destroy)
button_exit.pack()

root.mainloop()