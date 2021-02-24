#Have a dropdown box and combo box make a selection when the item is selected
from tkinter import *
from tkinter import ttk

main = Tk()
main.title('Binding Dropdown Menus and Combo Boxes')
main.iconbitmap('C:/Users/kcola/Pictures/Images/Icons/Blue_Target.ico')
main.geometry('400x400')

#Function for the dropdown box
def select(event):
    lbl = Label(main, text = clicked.get()).pack()

#Function for the combo box
def combo_click(event):
    lbl = Label(main, text = myCombo.get()).pack()

options = [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday"
]

#Dropdown
clicked = StringVar()
clicked.set(options[0])
drop = OptionMenu(main, clicked, *options, command = select)
drop.pack(pady = 20)

#Combo Box
myCombo = ttk.Combobox(main, value = options)
myCombo.current(0)
myCombo.bind("<<ComboboxSelected>>", combo_click)
myCombo.pack()

main.mainloop()