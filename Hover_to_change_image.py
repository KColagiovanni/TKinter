from tkinter import *
from PIL import ImageTk, Image

main = Tk()
main.title('I\'m the main window')
main.iconbitmap('C:/Users/kcola/Pictures/Images/Icons/Blue_Target.ico')
main.geometry("800x600")

def change(e):
    pic1 = ImageTk.PhotoImage(Image.open("GUI/images/LukeAndFriends6.jpg"))
    lbl.config(image = pic1)
    lbl.image = pic1

def change_back(e):
    pic1 = ImageTk.PhotoImage(Image.open("GUI/images/LukeAndFriends5.jpg"))
    lbl.config(image = pic1)
    lbl.image = pic1

pic1 = ImageTk.PhotoImage(Image.open("GUI/images/LukeAndFriends5.jpg"))
lbl = Label(main, image = pic1)
lbl.pack(pady = 20)

lbl.bind("<Enter>", change)
lbl.bind("<Leave>", change_back)

main.mainloop()