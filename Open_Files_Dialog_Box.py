#Import everything from TKinter
from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog

#Create the main window first, the root widget
root = Tk()

#Change the root window title
root.title("Root Window")
root.iconbitmap('C:/Users/kcola/Pictures/Images/Icons/Blue_Target.ico')

#Define a function to handle what happens when the file_button is clicked, in this case it opens the file dialog box so an image can be selected, once selected the image gets packed on the screen
def open_file_dialog_box():
    global my_img
    root.filename = filedialog.askopenfilename(initialdir = "C:/Users/kcola/Documents/Programing Fun/Python/GUI/images", title = "Select a File", filetypes = (("jpg files", "*.jpg"), ("png files", "*.png"), ("All Files", "*.*")))
#    lbl = Label(root, text = root.filename).pack()#Use this line to display the directory where the choosen file is located
    my_img = ImageTk.PhotoImage(Image.open(root.filename))
    my_img_lbl = Label(image = my_img).pack()

#Define a button to open the file dialog box and call the open_file_dialog_box function
file_button = Button(root, text = "Open Images", command = open_file_dialog_box).pack()

#root window exit button
button_exit = Button(root, text = "Close", command = root.destroy)
button_exit.pack()

root.mainloop()
