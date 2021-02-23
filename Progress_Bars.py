from tkinter import *
from tkinter import ttk

main = Tk()
main.title('I\'m the main window')
main.geometry("600x400")

def start():
    progress['value'] += 20
    lbl.config(text = progress['value'])

def stop():
    progress.stop()

#Create a progress bar (determinate is for a progress bar to fill, indetermiate is for a moving small square, no fill)
progress = ttk.Progressbar(main, orient = HORIZONTAL,
length = 300, mode = 'indeterminate')
progress.grid(row = 0, column = 0, columnspan = 2, padx = 150, pady = 20)

start_btn = Button(main, text = 'Start', command = start)
start_btn.grid(row = 1, column = 0, ipadx = 20, pady = 20)

stop_btn = Button(main, text = 'Stop', command = stop)
stop_btn.grid(row = 1, column = 1, ipadx = 20, pady = 20)

lbl = Label(main, text = '')
lbl.grid(row = 2, column = 0, columnspan = 2, pady = 20)
main.mainloop()