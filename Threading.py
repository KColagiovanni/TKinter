#Threading allows a process that freezes the program until its done to run and allow other processes to run simultaniously
from tkinter import *
import time
from random import randint
import threading

main = Tk()
main.title('I\'m the main window')
main.geometry("400x300")


def five_seconds():
    count = 5
    while count > 0:
        lbl.config(text = f'Countdown: {count}')
        count -= 1
        time.sleep(1)
    lbl.config(text = "Blastoff!!!")
lbl = Label(main, text = "Prepairing for launch")
lbl.pack(pady = 20)

def rando():
    random_lbl.config(text = f'Random number is {randint(1, 100)}')

#Using threading
btn1 = Button(main, text = "Launch", command = threading.Thread(target = five_seconds).start)
btn1.pack(pady = 20)

#Not sing threading
#btn1 = Button(main, text = "5 Seconds", command = five_seconds
#btn1.pack(pady = 20)

btn2 = Button(main, text = "Pick a random number", command = rando)
btn2.pack(pady = 20)

random_lbl = Label(main, text = '')
random_lbl.pack(pady = 20)

main.mainloop()