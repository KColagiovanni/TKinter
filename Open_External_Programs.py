from tkinter import *
from tkinter import filedialog
import os

main = Tk()
main.title('Open External Programs')
main.iconbitmap('C:/Users/kcola/Pictures/Images/Icons/Blue_Target.ico')
main.geometry('400x400')

def open_program():
    my_program = filedialog.askopenfilename()
    lbl.config(text = my_program)
    #Open program ('"%"' % variable is needed to open files where there is a space in the filename or path)
    os.system('"%s"' % my_program)

def open_notepad():
    os.system('C:/Windows/System32/Notepad.exe')

btn = Button(main, text = "Open Program", command = open_program)
btn.pack(pady = 20)

notepad_btn = Button(main, text = "Open Notepad", command = open_notepad)
notepad_btn.pack(pady = 20)

lbl = Label(main, text = '')
lbl.pack(pady = 20)

main.mainloop()