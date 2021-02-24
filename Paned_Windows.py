#Make some menus that go at the top of the window
from tkinter import *

main = Tk()
main.title('Paned Windows')
main.iconbitmap('C:/Users/kcola/Pictures/Images/Icons/Blue_Target.ico')
main.geometry('400x400')

#Panels
panel1 = PanedWindow(bd = 4, relief = "raised", bg = "red")
panel1.pack(fill = BOTH, expand = 1)

left_label = Label(panel1, text = "Left Panel")
panel1.add(left_label)

panel2 = PanedWindow(panel1, orient = VERTICAL, bd = 4, relief = "raised", bg = "blue")
panel1.add(panel2)

top = Label(panel2, text = "Top Panel")
panel2.add(top)

bottom = Label(panel2, text = "Bottom Panel")
panel2.add(bottom)

main.mainloop()