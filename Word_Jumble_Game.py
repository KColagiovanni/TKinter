from tkinter import *
from random import choice, shuffle

main = Tk()
main.title('I\'m the main window')
main.geometry("500x500")

lbl = Label(main, text = '', font = ('arial', 48))
lbl.pack(pady = 20)

def jumble():

    #Cleat answer box

    answer_lbl.config

    states = ['Alabama',
        'Alaska',
        'Arizona',
        'Arkansas',
        'California',
        'Colorado',
        'Connecticut',
        'Delaware',
        'Florida',
        'Georgia',
        'Hawaii',
        'Idaho',
        'Illinois',
        'Indiana',
        'Iowa',
        'Kansas',
        'Kentucky',
        'Lousiana',
        'Maine',
        'Maryland',
        'Massachusetts',
        'Michigan',
        'Minnasota',
        'Mississippi',
        'Missouri',
        'Montana',
        'Nebraska',
        'Nevada',
        'New Hampshire',
        'New Jersey',
        'New Mexico',
        'New York',
        'North Carolina',
        'North Dakota',
        'Ohio',
        'Oklahoma',
        'Oregon',
        'Pennsylvania',
        'Rhode Island',
        'South Carolina',
        'South Dakota',
        'Tennessee',
        'Texas',
        'Utah',
        'Vermont',
        'Virginia',
        'Washington',
        'West Virginia',
        'Wisconsin',
        'Wyoming'
    ]

    #Pick a random state
    global word
    global e
    word = choice(states)
    lbl.config(text = word)
    e = states.index(word)
    print(states[e])
    states.remove(word)
    print(states)

    #Spilt up word
    split_word = list(word)
    shuffle(split_word)

    #Turn shuffled list into a word
    global shuffled_word
    shuffled_word = ''
    for letter in split_word:
        shuffled_word += letter

    lbl.config(text = shuffled_word)    

def answer():
    global correct_count
    global total_count
    total_count += 1

    if word == answer_input.get():
        correct_count += 1
        answer_lbl.config(text = "Correct!!")
        right_amount.config(text = str(correct_count) + "/" + str(total_count) + " right")
        answer_input.delete(0, END)

        jumble()

#        answer_input.destroy()
    else:
        correct_count = correct_count
        answer_lbl.config(text = "Incorrect!!")
        right_amount.config(text = str(correct_count) + "/" + str(total_count) + " right")

correct_count = 0
total_count = 0

global answer_input
answer_input = Entry(main, font = ('arial', 20))
answer_input.pack(pady = 20)

btn_frame = Frame(main)
btn_frame.pack(pady = 20)

next_btn = Button(btn_frame, text = "Next Word", command = jumble)
next_btn.grid(row = 0, column = 1, ipadx = 5, padx = 10, pady = 20)

right_amount = Label(main, text = '', font = ('arial', 10))
right_amount.pack()

answer_btn = Button(btn_frame, text = "Check", command = answer)
answer_btn.grid(row = 0, column = 0, ipadx = 20, padx = 10, pady = 20)

answer_lbl = Label(main, text = '', font = ('airal, 18'))
answer_lbl.pack(pady = 20)

jumble()

main.mainloop()