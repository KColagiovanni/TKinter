from tkinter import *
from tkinter import colorchooser

main = Tk()
main.title('I\'m the main window')
main.geometry("400x400")

#color = "white"

my_menu = Menu(main)
main.config(menu = my_menu)

def our_command():
    lbl = Label(main, text = "You clicked a menu!!")
    lbl.pack()

def bg_color():
    hide_all_frames()
    global color
    global window_frame
    window_frame = Frame(main)
    color = colorchooser.askcolor()
    window_frame.grid_forget()
    window_frame = Frame(main, width = 400, height = 400, bg = color[1])
    window_frame.pack(fill = BOTH, expand = 1)
    color_lbl = Label(window_frame, text = "The hex code of the color you chose is " + color[1])
    color_lbl.pack()

def file_new():
    hide_all_frames()
    file_new_frame.pack(fill = BOTH, expand = 1)
    file_new_lbl = Label(file_new_frame, text = "You clicked the File -> New menu option")
    file_new_lbl.pack()

def edit_cut():
    hide_all_frames()
    edit_cut_frame.pack(fill = BOTH, expand = 1)
    edit_cut_lbl = Label(edit_cut_frame, text = "You clicked the Edit -> Cut menu option")
    edit_cut_lbl.pack()

def hide_all_frames():
    #Loop through the children and destroy old ones
    for widget in file_new_frame.winfo_children():
        widget.destroy()
    file_new_frame.pack_forget()
    for widget in edit_cut_frame.winfo_children():
        widget.destroy()
    edit_cut_frame.pack_forget()
    for widget in window_frame.winfo_children():
        widget.destroy()
    window_frame.pack_forget()

#Define the File Button
file_menu = Menu(my_menu)
my_menu.add_cascade(label = "File", menu = file_menu)
file_menu.add_command(label = "New", command = file_new)
file_menu.add_separator()
file_menu.add_command(label = "Exit", command = main.quit)

#Define the Edit Button
edit_menu = Menu(my_menu)
my_menu.add_cascade(label = "Edit", menu = edit_menu)
edit_menu.add_command(label = "Copy", command = our_command)
edit_menu.add_command(label = "Cut", command = edit_cut)

#Define the Options Button
option_menu = Menu(my_menu)
my_menu.add_cascade(label = "Options", menu = option_menu)
option_menu.add_command(label = "Find", command = our_command)
option_menu.add_command(label = "Next", command = our_command)
option_menu.add_command(label = "Change Background Color", command = bg_color)

#Create some frames
file_new_frame = Frame(main, width = 400, height = 400, bg = "red")
edit_cut_frame = Frame(main, width = 400, height = 400, bg = "blue")
window_frame = Frame(main, width = 400, height = 400)

main.mainloop()