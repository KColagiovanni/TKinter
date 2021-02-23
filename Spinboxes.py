from tkinter import *

main = Tk()
main.title('I\'m the main window')
main.geometry("500x400")


def grab():
    lbl.config(text = my_spin.get())
#Create a spinbox with ints(Spinbox(window, range start, range end, incrament amount))
#my_spin = Spinbox(main, from_ = 0, to = 10, increment = 2, font = ('arial', 20))

#Create a spinbox with strings(Spinbox(window, tuple of strings('',''), incrament amount))
my_spin = Spinbox(main, values = ('Kevin', 'Jessica', 'John'), font = ('arial', 20))
my_spin.pack(pady = 20)

btn = Button(main, text = 'submit', command = grab)
btn.pack(pady = 20)

lbl = Label(main, text = '')
lbl.pack(pady = 20)

main.mainloop()