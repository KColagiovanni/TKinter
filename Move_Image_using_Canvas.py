from tkinter import *

main = Tk()
main.title('I\'m the main window')
main.geometry("700x500")

w = 600
h = 400
x = w/2
y = h/2

#Create a canvas
my_canvas = Canvas(main, width = w, height  = h, bg = 'white')
my_canvas.pack(pady = 50)

img = PhotoImage(file = "c:/Users/KColagiovanni/Downloads")
my_img = my_canvas.create_image(0, 0, anchor = NW, image = img)

main.mainloop()