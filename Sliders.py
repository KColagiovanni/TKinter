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

#Create a variable and define the slider type (vertical or horizontal). Don't pack it on the same line or there may be issues
vertical = Scale(root, from_ = 0, to = 1000)
vertical.pack()
horizontal = Scale(root, from_ = 0, to = 1000, orient = HORIZONTAL)
horizontal.pack()

#Define a function that resizes the window to the selected slider size when clicked
def resize():
    root.geometry(str(horizontal.get()) + "x" + str(vertical.get()))

#Define a function to handle what happens when the "Click me" button is clicked
def slide():
    hrz_x_vrt_lbl = Label(root, text = str(horizontal.get()) + " x " + str(vertical.get())).pack()

#Define a button that resizes the window to the slider value when clicked
resize_btn = Button(root, text = "Resize Window", command = resize).pack()

#Define a button to display the slider value output
output_btn = Button(root, text = "Click me", command = slide).pack()

#root window exit button
button_exit = Button(root, text = "Close", command = root.destroy)
button_exit.pack()

root.mainloop()

