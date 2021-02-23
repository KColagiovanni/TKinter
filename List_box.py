from tkinter import *

main = Tk()
main.title('I\'m the main window')
main.geometry("500x500")

frame = Frame(main)
scrollbar = Scrollbar(frame, orient = VERTICAL)

#Create the listbox (selectmode can be changed to SINGLE, BROWSE, MULTIPLE, or EXTENDED)
my_listbox = Listbox(frame, width = 30, yscrollcommand = scrollbar.set, selectmode = MULTIPLE)

scrollbar.config(command = my_listbox.yview)
scrollbar.pack(side = RIGHT, fill = Y)
frame.pack()

my_listbox.pack(pady = 15)

#Use END to append the item to the end of the list and 0 at the begining, or any other number for that position (ex. 2, 3, 4...)
my_listbox.insert(END, "Option 1")
my_listbox.insert(END, "Option 2")
my_listbox.insert(END, "Option 3")
my_listbox.insert(END, "Option 4")
my_listbox.insert(END, "Option 5")

options = [
    "Option 6",
    "Option 7",
    "Option 8",
    "Option 9",
    "Option 10",
    "Option 11",
    "Option 12",
    "Option 13",
    "Option 14",
    "Option 15",
    "Option 16",
    "Option 17",
    "Option 18",
    "Option 19",
    "Option 20"
]

for x in options:
    my_listbox.insert(END, x)

def delete():
    my_listbox.delete(ANCHOR)
    lbl.config(text = '')

def delete_all():
    my_listbox.delete(0, END)

def select():
    lbl.config(text = my_listbox.get(ANCHOR))

def select_all():
    result = ''
    for x in my_listbox.curselection():
        result = result + str(my_listbox.get(x)) + '\n'
    lbl.config(text = result)
#    my_listbox.delete(0, END)

def delete_all_selected():
    for x in reversed(my_listbox.curselection()):
        my_listbox.delete(x)

del_btn = Button(main, text = "Delete", command = delete)
del_btn.pack(pady = 10)

sel_btn = Button(main, text = "Select", command = select)
sel_btn.pack(pady = 10)

global lbl
lbl = Label(main, text = '')
lbl.pack(pady = 10)

del_all_btn = Button(main, text = "Delete All Items", command = delete_all)
del_all_btn.pack(pady = 10)

sel_all_btn = Button(main, text = "Select All Items", command = select_all)
sel_all_btn.pack(pady = 10)

del_all_selected_btn = Button(main, text = "Delete All Selected Items", command = delete_all_selected)
del_all_selected_btn.pack(pady = 10)

main.mainloop()