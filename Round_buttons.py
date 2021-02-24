from tkinter import *

main = Tk()
main.title('Open External Programs')
main.iconbitmap('C:/Users/kcola/Pictures/Images/Icons/Blue_Target.ico')
main.geometry('400x400')

def thing():
    lbl.config(text = "You clicked the button!!")

upload_btn = PhotoImage(file = "C:/Users/kcola/Documents/Programing Fun/Python/GUI/images/round_upload_button.png")

img_lbl = Label(image = upload_btn)
#img_lbl.pack(pady = 20)

btn = Button(main, image = upload_btn, text = "Click Me", command = thing, borderwidth = 0)
btn.pack(pady = 20)

lbl = Label(main, text = '')
lbl.pack(pady = 20)

main.mainloop()