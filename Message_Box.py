#Import everything from TKinter
from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox#Use this import for message boxes!!

#Create the main window first, the root widget
root = Tk()

#Change the window title
root.title("Image Viewer")
root.iconbitmap('C:/Users/kcola/Pictures/Images/Icons/Blue_Target.ico')

#Define function to display a showinfo popup box
def popup():
    #Different types of meassages boxes are: showinfo, showwarning, showerror, askquestion, askokcancel, askyesno
    #Use the below line for showinfo, showwarning, and show error
    responce = messagebox.showinfo("This is a pop up window", "I'm a popup!")
    #Use the below line to do something with the user selected option, use with askquestion, askokcancel, and askyesno
#    responce = messagebox.askquestion("This is a pop up window", "I'm a popup!")
    Label(root, text = responce).pack()
#    if responce == 1:
#        Label(root, text = "You clicked yes").pack()
#    else:
#        Label(root, text = "You clicked no").pack()

#Button to call the message box
Button(root, text = "Popup", command = popup).pack()

#Exit button
button_exit = Button(root, text = "Close", command = root.quit)
button_exit.pack()

root.mainloop()

