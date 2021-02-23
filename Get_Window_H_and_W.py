from tkinter import *

main = Tk()
main.title('I\'m the main window')
main.geometry("500x500")

def info():
    dim_lbl = Label(main, text = main.winfo_geometry())
    dim_lbl.pack(pady = 20)

    height_lbl = Label(main, text = "Height " + str(main.winfo_height()))
    height_lbl.pack(pady = 5)
    width_lbl = Label(main, text = "Width " + str(main.winfo_width()))
    width_lbl.pack(pady = 5)

    x_lbl = Label(main, text = "X " + str(main.winfo_x()))
    x_lbl.pack(pady = 5)
    y_lbl = Label(main, text = "Y " + str(main.winfo_y()))
    y_lbl.pack(pady = 5)

btn = Button(main, text = "Click me", command = info)
btn.pack(pady = 20)

main.mainloop()