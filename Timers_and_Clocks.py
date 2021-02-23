#See all time options here --> https://docs.python.org/3/library/datetime.html
from tkinter import *
import time

main = Tk()
main.title('I\'m the main window')
main.geometry("1100x200")

#def update():
#    lbl.config(text = "New Text!!")

def clock():
    day = time.strftime("%A")
    date = time.strftime("%d")
    month = time.strftime("%m")
    year = time.strftime("%y")
    hour = time.strftime("%I")
    minute = time.strftime("%M")
    second = time.strftime("%S")
    AMPM = time.strftime("%p")

    lbl.config(text = day + " " + month + "/" + date + "/" + year + " " + hour + ":" + minute + ":" + second + AMPM)
    lbl.after(1000, clock)

lbl = Label(main, text = "", font = ("arial", 50), fg = "red", bg = "black")
lbl.pack(pady = 50)

clock()

main.mainloop()