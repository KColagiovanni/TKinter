from tkinter import *

main = Tk()
main.title('I\'m the main window')
main.geometry("700x500")

entries = []

def something():
    entry_list = ''
    for entry in entries:
        entry_list = entry_list + str(entries) + '\n'
        lbl.config(text = entries + '\ n')

for x in range(5):
#    entry_box = Entry(main)
#    entry_box.grid(row = 0, column = x, pady = 2, padx = 5)
    for y in range(5):
        entry_box = Entry(main)
        entry_box.grid(row = y, column = x, pady = 2, padx = 5)
        entries.append(entry_box)

btn = Button(main, text = "Click Me", command = something)
btn.grid(row = y + 1, column = 0, pady = 20)

lbl = Label(main, text = '')
lbl.grid(row = y + 2, column = 0, pady = 20)

main.mainloop()