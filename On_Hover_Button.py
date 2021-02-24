from tkinter import *

main = Tk()
main.title('I\'m the main window')
main.iconbitmap('C:/Users/kcola/Pictures/Images/Icons/Blue_Target.ico')
main.geometry("300x200")

def btn_hover(e):
    btn['bg'] = 'red'
    status_lbl.config(text = "Button is being hovered over")

def btn_leave(e):
    btn['bg'] = 'SystemButtonFace'
    status_lbl.config(text = "Button is not being hovered over")

btn = Button(main, text = "Click Me", font = (('arial'), 28))
btn.pack(pady = 50)

status_lbl = Label(main, text = '', bd = 1, relief = SUNKEN, anchor = E)
status_lbl.pack(fill = X, side = BOTTOM, ipady = 2)

btn.bind("<Enter>", btn_hover)
btn.bind("<Leave>", btn_leave)

main.mainloop()