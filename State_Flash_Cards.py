#State images found here: https://gisgeography.com/state-outlines-blank-maps-united-states/
from tkinter import *
from PIL import ImageTk, Image
from random import randint
import random
from State_Info import States

main = Tk()
main.title('Geography Flash Cards')
main.geometry("800x700+556+0")

def random_state():
#    global our_states
    #Define State Objects
    alabama = States("Alabama", "Montgomery", "AL", "Birmingham")
    alaska = States("Alaska", "Juneau", "AK", "Anchorage")
    arizona = States("Arizona", "Phoenix", "AZ", "Phoenix")
    arkansas = States("Arkansas", "Little Rock", "AR", "Little Rock")
    california = States("California", "Sacramento", "CA", "Los Angeles")
    colorado = States("Colorado", "Denver", "CO", "Denver")
    connecticut = States("Connecticut", "Hartford", "CT", "Bridgeport")
    delaware = States("Delaware", "Dover", "DE", "Wilmington")
    florida = States("Florida", "Tallahassee", "FL", "Jacksonville")
    georgia = States("Georgia", "Atlanta", "GA", "Atlanta")
    hawaii = States("Hawaii", "Honolulu", "HI", "Honolulu")
    idaho = States("Idaho", "Boise", "ID", "Boise")
    illinois = States("Illinois", "Springfield", "IL", "Chicago")
    indiana = States("Indiana", "Indianapolis", "IN", "Indianapolis")
    iowa = States("Iowa", "Des Moines", "IA", "Des Moines")
    kansas = States("Kansas", "Topeka", "KS", "Wichita")
    kentucky = States("Kentucky", "Frankfort", "KY", "Louisville")
    louisiana = States("Louisiana", "Baton Rouge", "LA", "New Orleans")
    maine = States("Maine", "Augusta", "ME", "Portland")
    maryland = States("Maryland", "Annapolis", "MD", "Baltimore")
    massachusetts = States("Massachusetts", "Boston", "MA", "Boston")
    michigan = States("Michigan", "Lansing", "MI", "Detroit")
    minnesota = States("Minnesota", "St. Paul", "MN", "Minneapolis")
    mississippi = States("Mississippi", "Jackson", "MS", "Jackson")
    missouri = States("Missouri", "Jefferson City", "MO", "Kansas City")
    montana = States("Montana", "Helena", "MT", "Billings")
    nebraska = States("Nebraska", "Lincoln", "NE", "Omaha")
    nevada = States("Nevada", "Carson City", "NV", "Las Vegas")
    new_hamshire = States("New Hampshire", "Concord", "NH", "Manchester")
    new_jersey = States("New Jersey", "Trenton", "NJ", "Newark")
    new_mexico = States("New Mexico", "Santa Fe", "NM", "Albuquerque")
    new_york = States("New York", "Albany", "NY", "New York")
    north_carolina = States("North Carolina", "Raleigh", "NC", "Charlotte")
    north_dakota = States("North Dakota", "Bismarck", "ND", "Fargo")
    ohio = States("Ohio", "Columbus", "OH", "Columbus")
    oklahoma = States("Oklahoma", "Oklahoma City", "OK", "Oklahoma City")
    oregon = States("Oregon", "Salem", "OR", "Portland")
    pennsylvania = States("Pennsylvania", "Harrisburg", "PA", "Philadelphia")
    rhode_island = States("Rhode Island", "Providence", "RI", "Providence")
    south_carolina = States("South Carolina", "Columbia", "SC", "Charleston")
    south_dakota = States("South Dakota", "Pierre", "SD", "Sioux Falls")
    tennessee = States("Tennessee", "Nashville", "TN", "Nashville")
    texas = States("Texas", "Austin", "TX", "Houston")
    utah = States("Utah", "Salt Lake City", "UT", "Salt Lake City")
    vermont = States("Vermont", "Montpelier", "VT", "Burlington")
    virginia = States("Virginia", "Richmond", "VA", "Virginia Beach")
    washington = States("Washington", "Olympia", "WA", "Seattle")
    west_virginia = States("West Virginia", "Charleston", "WV", "Charleston")
    wisconsin = States("Wisconsin", "Madison", "WI", "Milwaukee")
    wyoming = States("Wyoming", "Cheyenne", "WY", "Cheyenne")

    #Create a state list
    global state_list
    state_list = [alabama, alaska, arizona, arkansas, california,
    colorado, connecticut, delaware, florida, georgia, hawaii,
    idaho, illinois, indiana, iowa, kansas, kentucky, louisiana,
    maine, maryland, massachusetts, michigan, minnesota,
    mississippi, missouri, montana, nebraska, nevada, new_hamshire,
    new_jersey, new_mexico, new_york, north_carolina, north_dakota,
    ohio, oklahoma, oregon, pennsylvania, rhode_island,
    south_carolina, south_dakota, tennessee, texas, utah, vermont,
    virginia, washington, west_virginia, wisconsin, wyoming
    ]

#    our_states = ['alabama', 'alaska', 'arizona', 'arkansas',
#    'california', 'colorado', 'connecticut', 'delaware',
#    'florida', 'georgia', 'hawaii', 'idaho', 'illinois',
#    'indiana', 'iowa', 'kansas', 'kentucky', 'louisiana', 'maine',
#    'maryland', 'massachusetts', 'michigan', 'minnesota',
#    'mississippi', 'missouri', 'montana', 'nebraska', 'nevada',
#    'new_hampshire', 'new_jersey', 'new_mexico', 'new_york',
#    'north_carolina', 'north_dakota', 'ohio', 'oklahoma',
#    'oregon', 'pennsylvania', 'rhode_island', 'south_carolina',
#    'south_dakota', 'tennessee', 'texas', 'utah', 'vermont',
#    'virginia', 'washington', 'west_virginia', 'wisconsin',
#    'wyoming'
#    ]

    #Generate state images
    global rando
    rando = randint(0, len(state_list) - 1)
    print("rando is " + str(rando))
    global state_name
    #Select a random state from the list
    state_name = state_list[rando].show_name()
    state_name = state_name.replace(" ", "_")
    #Load the selected state picture
    state = "c:/Users/kcola/Documents/Programing Fun/Python/GUI/images/States/" + state_name + ".jpg"
    #Create state images
    global state_img
    state_img = ImageTk.PhotoImage(Image.open(state))
    #Set the background of the window to match the backround of the state image
    show_state.config(image = state_img, bg = "white")

    #Create an empty global answer list and counter
    global capitol_answer_list
    capitol_answer_list = []
    count = 1

    #While counter to pick the right answer and two other random capitols
    while count < 4:
#        global cap_rando
#        cap_rando = randint(0, len(state_list) - 1)
        #The first capitol_answer is the correct one, so append it to the answer list
        if count == 1:
            global capitol_answer
            capitol_answer = state_list[rando].show_capitol()
#        if count == 3:
#            rando -= 1
#        print("rando is from while is " + str(rando))
        #Then pick two other random capitols then remove them from the list so they dont get picked again and shuffle them
        capitol_answer_list.append(state_list[rando].show_capitol())
        state_list.remove(state_list[rando])
        random.shuffle(state_list)
        #increase counter
        if rando == 48 or rando == 49:
            rando -= 2
        count += 1

    #shuffle the list again
    random.shuffle(capitol_answer_list)
    print("The capitol is " + capitol_answer)
    print("state_list len is " + str(len(state_list)))
    print("The capitol list is", capitol_answer_list)
    print("capitol_answer_list len is " + str(len(capitol_answer_list)))

def check_state_answer():
    #Getting the text in the entry box
    state_answer = state_answer_input.get()
    #Replacing white space from the entry box to an underscore to match the answers in the list
    state_answer = state_answer.replace(" ", "_")

    right_state_answer = state_name
    #Determine if our answer is right or wrong
#    print("right_state_answer.lower() is " + right_state_answer.lower())
#    print("state_answer.lower() is " + state_answer.lower())
    if state_answer.lower() == right_state_answer.lower():
        right_state_answer = right_state_answer.replace("_", " ")
        response = 'Correct!! ' + right_state_answer.title()
    else:
        right_state_answer = right_state_answer.replace("_", " ")
        response = 'Incorrect!! ' + right_state_answer.title()

    state_answer_lbl.config(text = response)

    state_answer_input.delete(0, END)
    random_state()

def check_capitol_answer():
    print("Hi from the begining of check_capitol_answer()")
    right_capitol_answer = capitol_answer
    print("right_capitol_answer from chack_capitol_answer() is: " + right_capitol_answer)
    print("capitol_radio.get() from chack_capitol_answer() is: " + capitol_radio.get())
    if capitol_radio.get() == right_capitol_answer:
        response = "Correct!! "
        print(response)
    else:
        response = "Incorrect!!"
        print(response)
    capitol_answer_lbl.config(text = response)
    random_state()
#    capitol()

def states():
    hide_all_frames()
    state_frame.pack(fill = BOTH, expand = 1)
#    lbl = Label(state_frame, text = "Height " + str(main.winfo_height()) + "x Width " + str(main.winfo_width())).pack()

    global show_state
    show_state = Label(state_frame)#, image = state_img)
    show_state.pack(pady = 15)

    random_state()

    global state_answer_input
    state_answer_input = Entry(state_frame, font = ('arial', 18), bd = 3)
    state_answer_input.pack(pady = 15)

    state_answer_btn = Button(state_frame, text = "Submit", command = check_state_answer)
    state_answer_btn.pack(pady = 5)

    #Create a button to randomize images
    state_skip_btn = Button(state_frame, text = "Skip", command = states)
    state_skip_btn.pack(pady = 15)

    #Create a label to tell theh user if they got the answer right or not
    global state_answer_lbl
    state_answer_lbl = Label(state_frame, text = '', font = ('arial', 18), bg = "white")
    state_answer_lbl.pack(pady = 15)

def capitol():
    hide_all_frames()
    capitol_frame.pack(fill = BOTH, expand = 1)
    lbl = Label(capitol_frame, text = "State Capitol Frame")
    lbl.pack()

    global show_state
    show_state = Label(capitol_frame)
    show_state.pack(pady = 15)

    random_state()

    global capitol_radio
    capitol_radio = StringVar()
    capitol_radio.set(capitol_answer_list[randint(0, 2)])

    capitol_btn1 = Radiobutton(capitol_frame, text = capitol_answer_list[0], variable = capitol_radio, value = capitol_answer_list[0])
    capitol_btn1.pack()
    capitol_btn2 = Radiobutton(capitol_frame, text = capitol_answer_list[1], variable = capitol_radio, value = capitol_answer_list[1])
    capitol_btn2.pack()
    capitol_btn3 = Radiobutton(capitol_frame, text = capitol_answer_list[2], variable = capitol_radio, value = capitol_answer_list[2])
    capitol_btn3.pack()

    capitol_answer_btn = Button(capitol_frame, text = "Submit", command = check_capitol_answer)
    capitol_answer_btn.pack(pady = 15)

    #Create a button to randomize images
    state_skip_btn = Button(capitol_frame, text = "Skip", command = capitol)
    state_skip_btn.pack(pady = 15)

    global capitol_answer_lbl
    capitol_answer_lbl = Label(capitol_frame, text = '', font = ('arial', 18))
    capitol_answer_lbl.pack(pady = 15)

def hide_all_frames():
    #Loop through to destroy all children in previous frame
    for widget in state_frame.winfo_children():
        widget.destroy()

    #Loop through to destroy all children in previous frame
    for widget in capitol_frame.winfo_children():
        widget.destroy()

    state_frame.pack_forget()
    capitol_frame.pack_forget()

menu = Menu(main)
main.config(menu = menu)

#Create geography menus
states_menu = Menu(main)
menu.add_cascade(label = "Geography", menu = states_menu)
states_menu.add_command(label = "States", command = states)
states_menu.add_command(label = "State Capitol", command = capitol)
states_menu.add_separator()
states_menu.add_command(label = "Exit", command = main.quit)

#Create Frames
state_frame = Frame(main, width = 500, height = 500, bg = "white")
capitol_frame = Frame(main, width = 500, height = 500)

main.mainloop()