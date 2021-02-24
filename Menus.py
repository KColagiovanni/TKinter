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
    lbl = Label(main, text = "You clicked a dropdown menu").pack()

#Create a menu item
file_menu = Menu(my_menu)
my_menu.add_cascade(label = "File", menu = file_menu)
file_menu.add_command(label = "New", command = our_command)
#Make a sepertor between two options
file_menu.add_separator()
file_menu.add_command(label = "Exit", command = main.quit)

#Create an edit menu
edit_menu = Menu(my_menu)
my_menu.add_cascade(label = "Edit", menu = edit_menu)
edit_menu.add_command(label = "Cut", command = our_command)
edit_menu.add_command(label = "Copy", command = our_command)

#Create an options menu
option_menu = Menu(my_menu)
my_menu.add_cascade(label = "Options", menu = option_menu)
option_menu.add_command(label = "Find", command = our_command)
option_menu.add_command(label = "FInd Next", command = our_command)

main.mainloop()