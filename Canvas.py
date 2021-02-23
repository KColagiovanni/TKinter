from tkinter import *

main = Tk()
main.title('I\'m the main window')
main.geometry("800x700")

#Create a canvas
my_canvas = Canvas(main, width = 300, height  = 200)#, bg = 'white')
my_canvas.pack(pady = 20)

w = 600
h = 400
x = w/2
y = h/2

#Create another canvas
my_canvas2 = Canvas(main, width = w, height  = h, bg = 'white')
my_canvas2.pack(pady = 20)

#Create a rectangle
#my_canvas,create_rectangle(x1, y1, x2, y2, fill = "color")
#x1 and y1 = Top left cordinates - x2 and y2 = Bottom right cordinates
my_canvas.create_rectangle(50, 150, 250, 50, fill = "pink")

#Create an oval
#my_canvas.create_oval(x1, y1, x2, y2, fill = "color")
#x1 and y1 = Top left cordinates - x2 and y2 = Bottom right cordinates
my_canvas.create_oval(100, 150, 200, 50, fill = "blue")

#Create a line
#my_canvas.create_line(x1, y1, x2, y2, fill = "color")
my_canvas.create_line(0, 100, 300, 100, fill = "red")
my_canvas.create_line(150, 200, 150, 0, fill = "red")

circle = my_canvas2.create_oval(x, y, x + 10, y + 10, fill = "red")

#Use left arrow to move the circle
def left(event):
    x = -5#Define the speed that the circle will move left
    y = 0
    my_canvas2.move(circle, x, y)

#Use right arrow to move the circle
def right(event):
    x = 5#Define the speed that the circle will move right
    y = 0
    my_canvas2.move(circle, x, y)

#Use up arrow to move the circle
def up(event):
    x = 0
    y = -5#Define the speed that the circle will move up
    my_canvas2.move(circle, x, y)

#Use dowm arrow to move the circle
def down(event):
    x = 0
    y = 5#Define the speed that the circle will move down
    my_canvas2.move(circle, x, y)

def pressing(event):
    x = 0
    y = 0
    if event.char == "a": x = -10#Define the key and speed that the circle will move left
    if event.char == "d": x = 10#Define the key and speed that the circle will move right
    if event.char == "w": y = -10#Define the key and speed that the circle will move up
    if event.char == "s": y = 10#Define the key and speed that the circle will move down
    my_canvas2.move(circle, x, y)

#Move the circle with the arrow keys
main.bind("<Left>", left)
main.bind("<Right>", right)
main.bind("<Up>", up)
main.bind("<Down>", down)

#Move the circle with the assigned key in the pressing function
main.bind("<Key>", pressing)

main.mainloop()