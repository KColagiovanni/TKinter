#Make some menus that go at the top of the window
from tkinter import *

main = Tk()
main.title('Menu Bars')
main.iconbitmap('C:/Users/kcola/Pictures/Images/Icons/Blue_Target.ico')
main.geometry('400x400')

my_menu = Menu(main)
main.config(menu = my_menu)

#our_command function
def our_command():
    lbl = Label(main, text = "You clicked a dropdown menu")
    lbl.pack()

def file_new():
    hide_all_frames()
    file_new_frame.pack(fill = "both", expand = 1)
    lbl = Label(file_new_frame, text = "You clicked the file -> new menu")
    lbl.pack()

def edit_cut():
    hide_all_frames()
    edit_cut_frame.pack(fill = "both", expand = 1)
    lbl = Label(edit_cut_frame, text = "You clicked the edit -> cut menu")
    lbl.pack()

def hide_all_frames():
    file_new_frame.pack_forget()
    edit_cut_frame.pack_forget()

#Create a menu item
file_menu = Menu(my_menu)
my_menu.add_cascade(label = "File", menu = file_menu)
file_menu.add_command(label = "New", command = file_new)

#Make a sepertor between two options
file_menu.add_separator()
file_menu.add_command(label = "Exit", command = main.quit)

#Create an edit menu
edit_menu = Menu(my_menu)
my_menu.add_cascade(label = "Edit", menu = edit_menu)
edit_menu.add_command(label = "Cut", command = edit_cut)
edit_menu.add_command(label = "Copy", command = our_command)

#Create an options menu
option_menu = Menu(my_menu)
my_menu.add_cascade(label = "Options", menu = option_menu)
option_menu.add_command(label = "Find", command = our_command)
option_menu.add_command(label = "FInd Next", command = our_command)

#Create new frames
file_new_frame = Frame(main, width = 400, height = 400, bg = "red")
edit_cut_frame = Frame(main, width = 400, height = 400, bg = "blue")

main.mainloop()