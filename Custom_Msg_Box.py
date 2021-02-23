from tkinter import *

main = Tk()
main.title('I\'m the main window')
main.geometry('400x400')

def choice(option):
    if option == 'yes':
        lbl.config(text = 'You Clicked Yes')
        print('yes')
#    if choice == 'no':
    else:
        lbl.config(text = 'You Clicked No')
        print('no')
    pop.destroy()

def click_me():
    global pop
    pop = Toplevel(main)
    pop.title('Popup')
    pop.geometry('250x150')
    pop.config(bg = '#00ff00')

    pop_lbl = Label(pop, text = "Would you like to proceed?")
    pop_lbl.pack(pady = 10)

    pop_frame = Frame(pop, bg = '#00ff00')
    pop_frame.pack(pady = 10)

    yes_btn = Button(pop_frame, text = 'Yes', command = lambda: choice('yes'))
    no_btn = Button(pop_frame, text = 'No', command = lambda: choice('no'))
    yes_btn.grid(row = 0, column = 0, padx = 5)
    no_btn.grid(row = 0, column = 1, padx = 5)


btn = Button(main, text = "Click me", command = click_me)
btn.pack(pady = 50)

lbl = Label(main, text = '')
lbl.pack(pady = 15)

main.mainloop()