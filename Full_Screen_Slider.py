from tkinter import *
from tkinter import ttk

main = Tk()
main.title('I\'m the main window')
main.geometry("500x400")

#Create a main frame
main_frame = Frame(main)
main_frame.pack(fill = BOTH, expand = 1)

#Create canvas
my_canvas = Canvas(main_frame)
my_canvas.pack(side = LEFT, fill = BOTH, expand = 1)

#Add a scrollbar to a canvas
my_scrollbar = ttk.Scrollbar(main_frame, orient = VERTICAL, command = my_canvas.yview)
my_scrollbar.pack(side = RIGHT, fill = Y)

#Configure the canvas
my_canvas.configure(yscrollcommand = my_scrollbar.set)
my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion = my_canvas.bbox('all')))

#Create another frame inside of the canvas
second_frame = Frame(my_canvas)

#Add that new frame to a window in the canvas
my_canvas.create_window((0, 0), window = second_frame, anchor = NW)


for btn in range(100):
    Button(second_frame, text = f'Button {btn + 1}').grid(row = btn, column = 0, pady = 10, padx = 10)

#Now we put things in second_frame instead of main
lbl = Label(second_frame, text = "Hi")
lbl.grid(row = 1, column = 3, padx = 5)

main.mainloop()