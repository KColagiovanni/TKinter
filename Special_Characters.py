from tkinter import *

main = Tk()
main.title('I\'m the main window')
main.geometry("400x400")

#Creating the unicode charater (Ex. u'\u00b0' is a degree symbol)
#Find more unicode symbols by googling "unicode characters" (https://en.wikipedia.org/wiki/List_of_Unicode_characters)
lbl = Label(main, text = "41" + u'\u264f', font = ("arial", 32), pady = 10)
lbl.pack()

main.mainloop()