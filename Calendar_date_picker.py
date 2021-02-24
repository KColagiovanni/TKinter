from tkinter import *
from tkcalendar import *

main = Tk()
main.title('I\'m the main window')
main.iconbitmap('C:/Users/kcola/Pictures/Images/Icons/Blue_Target.ico')
main.geometry("800x600")

cal = Calendar(main, selectmode = 'day', year = 2020, month = 11, day = 27)
cal.pack(pady = 20, fill = BOTH, expand = True)

def get_date():
    lbl.config(text = cal.get_date())


btn = Button(main, text = "Get Date", command = get_date)
btn.pack(pady = 20)

lbl = Label(main, text = '')
lbl.pack(pady = 20)

main.mainloop()