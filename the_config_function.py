from tkinter import *

main = Tk()
main.title('I\'m the main window')
main.geometry("500x500")

def something():
    #To update the text
    lbl.config(text = "This is new small text", font = ("arial", 8))
    #to update the main window
    main.config(bg = "blue")
    #To update the button
    btn.config(text = "Can't click me!", state = DISABLED, pady = 30)

#global lbl
lbl = Label(main, text = "This is text", font = ("arial", 16))
lbl.pack(pady = 10)

#global btn
btn = Button(main, text = "Click me", command = something)
btn.pack(pady = 10)

main.mainloop()