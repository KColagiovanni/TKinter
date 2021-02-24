#Import everything from TKinter
from tkinter import *
from PIL import ImageTk, Image
import numpy as np
import matplotlib.pyplot as plt

#Create the main window first, the root widget
root = Tk()

#Change the root window title
root.title("Data PLotting")
root.iconbitmap('C:/Users/kcola/Pictures/Images/Icons/Blue_Target.ico')
#Define a fixed window size
root.geometry("350x120")

def graph():
    house_prices = np.random.normal(200000, 25000, 5000)
    plt.hist(house_prices, 500)
    plt.show()

btn = Button(root, text = "Graph", command = graph).pack()

root.mainloop()