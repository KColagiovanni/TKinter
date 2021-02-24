#Import everything from TKinter
from tkinter import *
from PIL import ImageTk, Image

#Create the main window first, the root widget
root = Tk()

#Change the root window title
root.title("Root Window")
root.iconbitmap('C:/Users/kcola/Pictures/Images/Icons/Blue_Target.ico')

#Define a function to open the second window
def open():
    #Need to make my_img a global variable or else the image wont display in the second window
    global my_img
    top = Toplevel()
    #Change the top window title and icon
    top.title("New Window")
    top.iconbitmap('C:/Users/kcola/Pictures/Images/Icons/Blue_Target.ico')

    lbl = Label(top, text = "I'm in a new window").pack()
    my_img = ImageTk.PhotoImage(Image.open("LukeAndFriends5.jpg"))
    my_label = Label(top, image = my_img).pack()

    #top window exit button
    top_button_exit = Button(top, text = "Close", command = top.destroy)
    top_button_exit.pack()


#Use button to open a second window (Use button in this example)
button = Button(root, text = "See Luke and Maggie", command = open).pack()

#Use top instead of root for the new window (use pack in this example)
#top = Toplevel()
#Change the top window title and icon
#top.title("New Window")
#top.iconbitmap('C:/Users/kcola/Pictures/Images/Icons/Blue_Target.ico')

#lbl = Label(top, text = "I'm in a new window").pack()
#my_img = ImageTk.PhotoImage(Image.open("LukeAndFriends5.jpg"))
#my_label = Label(top, image = my_img).pack()

#root window exit button
button_exit = Button(root, text = "Close", command = root.destroy)
button_exit.pack()

root.mainloop()