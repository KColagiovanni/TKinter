#Import everything from TKinter
from tkinter import *
from PIL import ImageTk,Image

#Create the main window first, the root widget
root = Tk()

#Change the window title
root.title("Image Viewer")
root.iconbitmap('C:/Users/kcola/Pictures/Images/Icons/Blue_Target.ico')

#Define the location of the images:
my_img1 = ImageTk.PhotoImage(Image.open("images/LukeAndFriends1.jpg"))
my_img2 = ImageTk.PhotoImage(Image.open("images/LukeAndFriends2.jpg"))
my_img3 = ImageTk.PhotoImage(Image.open("images/LukeAndFriends3.jpg"))
my_img4 = ImageTk.PhotoImage(Image.open("images/LukeAndFriends4.jpg"))
my_img5 = ImageTk.PhotoImage(Image.open("images/LukeAndFriends5.jpg"))
my_img6 = ImageTk.PhotoImage(Image.open("images/LukeAndFriends6.jpg"))

#Create a list for the images
image_list = [my_img1, my_img2, my_img3, my_img4, my_img5, my_img6]

#Define the status bar (bd = 1 is the boarder size)(relief = SUNKEN makes the label look sunken)(anchor = E means the text is anchored to the east side of the window)
status = Label(root, text = "Image 1 of " + str(len(image_list)), bd = 1, relief = SUNKEN, anchor = E)

#Define where the image will be placed 
my_label = Label(image = my_img1)
my_label.grid(row = 0, column = 0, columnspan = 3)

#Define the forward button function and pass in the image number
def forward(image_num):
    #Define global variables to be shared between functions
    global my_label
    global button_forward
    global button_back
    #Remove the previous image displayed
    my_label.grid_forget()
    #Pull up the next image and display it and define the forward and back button function
    my_label = Label(image = image_list[image_num - 1])
    button_forward = Button(root, text = ">>", command = lambda: forward(image_num + 1))
    button_back = Button(root, text = "<<", command = lambda: back(image_num - 1))
    #If the image displayed is the last one, disable the forward button
    if image_num == 6:
        button_forward = Button(root, text = ">>", state = DISABLED)
    #Where to display the image and buttons
    my_label.grid(row = 0, column = 0, columnspan = 3)
    button_back.grid(row = 1, column = 0)
    button_forward.grid(row = 1, column = 2)
    #Update the status bar
    status = Label(root, text = "Image " + str(image_num) + " of " + str(len(image_list)), bd = 1, relief = SUNKEN, anchor = E)
    status.grid(row = 2, column = 0, columnspan = 3, sticky = W+E)

#Define the back button function and pass in the image number
def back(image_num):
    #Define global variables to be shared between functions
    global my_label
    global button_forward
    global button_back
    #Remove the previous image displayed
    my_label.grid_forget()
    #Pull up the previous image and display it and define the forward and back button function
    my_label = Label(image = image_list[image_num - 1])
    button_forward = Button(root, text = ">>", command = lambda: forward(image_num + 1))
    button_back = Button(root, text = "<<", command = lambda: back(image_num - 1))
    #If the image displayed is the first one, disable the forward button
    if image_num == 1:
        button_back = Button(root, text = "<<", command = back, state = DISABLED)
    #Where to display the image and buttons
    my_label.grid(row = 0, column = 0, columnspan = 3)
    button_back.grid(row = 1, column = 0)
    button_forward.grid(row = 1, column = 2)
    #Update the status bar
    status = Label(root, text = "Image " + str(image_num) + " of " + str(len(image_list)), bd = 1, relief = SUNKEN, anchor = E)
    status.grid(row = 2, column = 0, columnspan = 3, sticky = W+E)

#Define the back button
button_back = Button(root, text = "<<", command = back, state = DISABLED)
#Define the exit button
button_exit = Button(root, text = "Close", command = root.quit)
#Define the forward button
button_forward = Button(root, text = ">>", command = lambda: forward(2))

#Where to display the image and buttons
button_back.grid(row = 1, column = 0)
button_exit.grid(row = 1, column = 1)
button_forward.grid(row = 1, column = 2, pady = 10)
#Where to display the status(sticky = W + E means the status label will span the entire window from the west to the east)
status.grid(row = 2, column = 0, columnspan = 3, sticky = W + E)

#Create the main loop to let the program keep running
root.mainloop()