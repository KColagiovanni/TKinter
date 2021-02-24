#Import everything from TKinter
from tkinter import *
from PIL import ImageTk,Image

#Create the main window first, the root widget
root = Tk()

#Change the window title
root.title("Image Viewer")
root.iconbitmap('C:/Users/kcola/Pictures/Images/Icons/Blue_Target.ico')

#Create the frame
frame = LabelFrame(root, text = "This is my Frame", padx = 50, pady = 50)
#Pack the frame onto the screen
frame.pack(padx = 10, pady = 10)

#Create a sample button to put in the frame(Notice that instead of putting it in "root", its in "frame")
button = Button(frame, text = "Don't click here")
button_exit = Button(frame, text = "Close", command = root.quit)
#Pack the button into the frame
#button.pack()

#Can also use grid with pack when using frames
button.grid(row = 0, column = 0)
button_exit.grid(row = 1, column = 1)

root.mainloop()