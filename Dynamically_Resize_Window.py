from tkinter import *

main = Tk()
main.title('I\'m the main window')
main.geometry("800x800")

def resize():
    w = width_entry.get()
    h = height_entry.get()
    main.geometry(str(w) + "x" + str(h))
#    main.geometry(f"{w}x{h}")

width_lbl = Label(main, text = "Width")
width_lbl.pack(pady = 20)
width_entry = Entry(main)
width_entry.pack()

height_lbl = Label(main, text = "Height")
height_lbl.pack(pady = 20)
height_entry = Entry(main)
height_entry.pack()

btn = Button(main, text = "Resize", command = resize)
btn.pack(pady = 20)

main.mainloop()