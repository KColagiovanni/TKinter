#Import everything from TKinter
from tkinter import *
from PIL import ImageTk,Image

#Create the main window first, the root widget
root = Tk()

#Change the window title
root.title("Image Viewer")
root.iconbitmap('C:/Users/kcola/Pictures/Images/Icons/Blue_Target.ico')

#Define a TKinter Variable(This example was when using radiobuttons "option1" and "option2"
opt = IntVar()#StringVar instead of IntVarif value is a string
#Set an initial value for myLabel
#opt.set("2")

#Create a list to hold the different radio button options
TOPPINGS = [
    ("Pepperoni", "Pepperoni"),
    ("Cheese", "Cheese"),
    ("Mushroom", "Mushroom"),
    ("Onion", "Onion")
]

#Define a TKinter Variable
pizza = StringVar()
pizza.set("Pepperoni")

#The for loop to loop through the toppings list
for text, topping in TOPPINGS:
    Radiobutton(root, text = text, variable = pizza, value = topping).pack(anchor = W)

#The function that prints the list item selected to the window
def clicked(value):
    myLabel = Label(root, text = value)
    myLabel.pack()


#Define the Radiobutton and pack it onto the window
#Radiobutton(root, text = "Option 1", variable = opt, value = 1, command = lambda: clicked(opt.get())).pack()
#Radiobutton(root, text = "Option 2", variable = opt, value = 2, command = lambda: clicked(opt.get())).pack()

#Create a label to display the result of selecting the radio button
#myLabel = Label(root, text = pizza.get())
#myLabel.pack()

#The button used to select the radiobutton that was ticked
myButton = Button(root, text = "Select", command = lambda: clicked(pizza.get()))
myButton.pack()

#Exit button
button_exit = Button(root, text = "Close", command = root.quit)
button_exit.pack()

root.mainloop()
