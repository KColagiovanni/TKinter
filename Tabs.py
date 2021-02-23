from tkinter import *
from tkinter import ttk

main = Tk()
main.title('I\'m the main window')
main.geometry("500x500")

notebook = ttk.Notebook(main)
notebook.pack(pady = 15)

#Hide the 2nd tab
def hide():
    #1 is for the second(onenth) tab (starting at 0)
    notebook.hide(1)

#Show the 2nd tab
def show():
    notebook.add(frame2, text = "Red Tab")

def select():
    #1 is for the second(onenth) tab (starting at 0)
    notebook.select(1)

#Create and define the tabs
frame1 = Frame(notebook, width = 500, height = 500, bg = "blue")
frame2 = Frame(notebook, width = 500, height = 500, bg = "red")

#For adding the color
frame1.pack(fill = BOTH, expand = 1)
frame2.pack(fill = BOTH, expand = 1)

#Adding the tabs to the window
notebook.add(frame1, text = "Blue Tab")
notebook.add(frame2, text = "Red Tab")

#Creating a hide button
btn_hide = Button(frame1, text = "Hide Red Tab", command = hide)
btn_hide.pack(pady = 10)

#Creating a show button
btn_show = Button(frame1, text = "Show Red Tab", command = show)
btn_show.pack(pady = 10)

#Navigate to a tab
sel_btn = Button(frame1, text = "Navigate to the Red tab", command = select)
sel_btn.pack(pady = 10)

main.mainloop()