from tkinter import *
from PIL import ImageTk, Image

main = Tk()
main.title('I\'m the main window')
main.iconbitmap('C:/Users/kcola/Pictures/Images/Icons/Blue_Target.ico')
main.geometry("800x600")

def small():
    #Open image
    img = Image.open("GUI/images/LukeAndFriends5.jpg")
    #Resize the image
    resized = img.resize((100, 80), Image.ANTIALIAS)
    global new_img
    new_img = ImageTk.PhotoImage(resized)
    lbl.config(image = new_img)

small_btn = Button(main, text = "Small", command = small)
small_btn.grid(row = 0, column = 2, pady = 20)

img = ImageTk.PhotoImage(Image.open("GUI/images/LukeAndFriends5.jpg"))

global lbl
lbl = Label(main, image = img)
lbl.grid(row = 1, column = 0, columnspan = 4, pady = 20)

main.mainloop()