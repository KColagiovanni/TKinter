from tkinter import *
from PIL import ImageTk, Image

main = Tk()
main.title('I\'m the main window')
main.iconbitmap('C:/Users/kcola/Pictures/Images/Icons/Blue_Target.ico')
main.geometry("800x600")

w = 600
h = 400
x = w/2
y = h/2

#Create a canvas
my_canvas = Canvas(main, width = w, height  = h, bg = 'white')
my_canvas.pack(pady = 20)

img = ImageTk.PhotoImage(Image.open("GUI/images/Luke_Stick_Boy.jpg"))
my_img = my_canvas.create_image(230, 165, anchor = NW, image = img)

def left(event):
    x = -10
    y = 0
    my_canvas.move(my_img, x, y)

def right(event):
    x = 10
    y = 0
    my_canvas.move(my_img, x, y)

def up(event):
    x = 0
    y = -10
    my_canvas.move(my_img, x, y)

def down(event):
    x = 0
    y = 10
    my_canvas.move(my_img, x, y)

main.bind("<Left>", left)
main.bind("<Right>", right)
main.bind("<Up>", up)
main.bind("<Down>", down)

main.mainloop()