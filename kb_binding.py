from tkinter import *

main = Tk()
main.title('I\'m the main window')
main.geometry("100x100")

def clicker(event):
#    lbl = Label(main, text = "You Clicked Me!!!")#To show when the button is clicked
#    lbl = Label(main, text = "You Clicked Me!!!" + str(event.x) + " " + str(event.y))#To show when the button is clicked and (x, y) mouse cordinates
#    lbl = Label(main, text = "You clicked the " + event.char + " key")#To show which key clicked the button when focused on it(Used with .bind("<key>", action))
    lbl = Label(main, text = "You clicked the " + event.keysym + " key")#To show th ename of whichever key is clicked the button when focused on it(Used with .bind("<key>", action))
    lbl.pack()

btn = Button(main, text = "Click me", command = clicker)
#.bind(event, action)
#btn.bind("<Button-1>", clicker)#Left click
#btn.bind("<Button-3>", clicker)#Right click
#btn.bind("<Enter>", clicker)#When you enter the button area
#btn.bind("<Leave>", clicker)#When you leave the button area
#btn.bind("<FocusIn>", clicker)#When you tab onto the button
#btn.bind("<FocusOut>", clicker)#When you tab out of the button
#btn.bind("<Return>", clicker)#When you press the Return/Enter button on the keyboard
btn.bind("<Key>", clicker)#When you press any key on the keyboard
btn.pack(pady = 20)

main.mainloop()