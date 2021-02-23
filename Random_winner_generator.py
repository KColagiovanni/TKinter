from tkinter import *
from random import randint

root = Tk()
root.title("")
root.iconbitmap("")
root.geometry("400x400")

btn_click_count = 0

def delete():
    winner_lbl.destroy()

def pick():
    global winner_lbl
    global btn_click_count
    if btn_click_count > 0:
        delete()
    entries = ["person 1",
    "person 2",
    "person 3",
    "person 4",
    "person 5",
    "person 6",
    "person 7",
    "person 8",
    "person 9",
    "person 10",
    "person 11",
    "person 12",
    "person 13",
    "person 14",
    "person 15",
    "person 16",
    "person 17",
    "person 18",
    "person 19",
    "person 20"
    ]

    #Check for duplicates
    entries_set = set(entries)
    unique_entries = list(entries_set)

    #Create a random number for the amount of entries
    rando = randint(0, len(unique_entries) - 1)

    winner_lbl = Label(root, text = unique_entries[rando], font = ("helvetica", 18))
    winner_lbl.pack(pady = 50)

    btn_click_count += 1

top_lbl = Label(root, text = "Win-o-rama!", font = ("helvetica", 24))
top_lbl.pack(pady = 20)

win_btn = Button(root, text = "Pick a Winner", font = ("helvetica", 24), command = pick)
win_btn.pack(pady = 20)

root.mainloop()