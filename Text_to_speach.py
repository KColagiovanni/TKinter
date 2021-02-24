from tkinter import *
import pyttsx3

main = Tk()
main.title('I\'m the main window')
main.iconbitmap('C:/Users/kcola/Pictures/Images/Icons/Blue_Target.ico')
main.geometry("800x600")

def speak():
    #Initialize
    engine = pyttsx3.init()
    engine.say(entry.get())
    engine.runAndWait()
    entry.delete(0, END)

entry = Entry(main, font = ('arial', 28))
entry.pack(pady = 20)

btn = Button(main, text = "Speak", command = speak)
btn.pack(pady = 20)

main.mainloop()