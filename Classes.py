from tkinter import *

main = Tk()
main.title('I\'m the main window')
main.geometry("100x100")

#Define the class
class Kevin:

    #Define the initialization funciton
    def __init__(self, master):
        myFrame = Frame(master)
        myFrame.pack()

        self.btn = Button(master, text = "Click Me!", command = self.clicker)
        self.btn.pack(pady = 20)

    #Define what happens when the button is clicked
    def clicker(self):
        print("Thank you! You clicked me!")

#Initializing the class
e = Kevin(main)

main.mainloop()