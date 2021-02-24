from tkinter import *
from PIL import ImageTk, Image
from random import randint
import pygame
from tkinter import filedialog
import time
from mutagen.mp3 import MP3
import tkinter.ttk as ttk

main = Tk()
main.title('MP3 Player')
main.iconbitmap('C:/Users/kcola/Pictures/Images/Icons/Blue_Target.ico')
main.geometry("500x450")

pt = None

pygame.mixer.init()

#Define adding a song function
def add_song():
    song = filedialog.askopenfilename(initialdir = 'GUI/Audio/Music/', title = 'Choose a Song', filetypes = (('mp3 Files', '*.mp3'), ('All Files', '*.*')))
    #Striping off the directory and file type
    song = song.replace('C:/Users/kcola/Documents/Programing Fun/Python/GUI/Audio/Music/', '')
    song = song.replace('.mp3', '')
    song_box.insert(END, song)

def add_many_songs():
    songs = filedialog.askopenfilenames(initialdir = 'GUI/Audio/Music/', title = 'Choose a Song', filetypes = (('mp3 Files', '*.mp3'), ('All Files', '*.*')))

    #Loop through the list and replace directory info and filetype
    for song in songs:
        song = song.replace('C:/Users/kcola/Documents/Programing Fun/Python/GUI/Audio/Music/', '')
        song = song.replace('.mp3', '')
        song_box.insert(END, song)

#Definei the function to start playing the song that is currently selected
def play():
    #set the stopped variable to stopped so the song can play and slider works
    global stopped
    stopped = False
    song = song_box.get(ACTIVE)
    song = f'C:/Users/kcola/Documents/Programing Fun/Python/GUI/Audio/Music/{song}.mp3'
    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops = 0)
#    lbl.config(text = 'Play', bg = '#ffffff')
    paused = False
    #Call the play time function to get song time
    play_time()
    current_volume = pygame.mixer.music.get_volume()
    slider_lbl.config(text = int(current_volume * 100))
#    party_time()
#    slider_position = int(song_length)
#    slider.config(to = slider_position, value = 0)

global stopped
stopped = False
#Define the function that stops playing the song thatis currently playing
def stop():
    #Reset slider and status bar
    music_pos_slider.config(value = 0)
    status_bar.config(text = '')
#    main.after_cancel
    #Stop the music using the pygame library function
    pygame.mixer.music.stop()
    song_box.selection_clear(ACTIVE)
    #Clear the status bar
    status_bar.config(text = '')
    #Set stop to true
    global stopped
    stopped = True
#    main.config(bg = 'white')
#    lbl.config(text = 'Stop', bg = '#ffffff')
#    main.config(bg = '#ffffff')
#    main.after(100, stop)
    
#global paused
paused = False 

#Define the function that pauses or unpauses the song that is currently playing
def pause(is_paused):
    global paused
    paused = is_paused
    if paused:
        #Unpaused
        pygame.mixer.music.unpause()
        paused = False
#        main.config(bg = 'white')
#        lbl.config(text = 'Unpause', bg = '#ffffff')
    else:
        #Pause
        pygame.mixer.music.pause()
        paused = True
#        main.config(bg = 'white')
#        lbl.config(text = 'Pause', bg = '#ffffff')

def back():
    #Reset slider and status bar
    music_pos_slider.config(value = 0)
    status_bar.config(text = '')
#    lbl.config(text = 'Beginning of List', bg = '#ffffff')
    next_one = song_box.curselection()
    print(next_one)
    print(next_one[0])
    next_one = next_one[0] - 1
    song = song_box.get(next_one)
    #Add directory structure back to song title
    song = f'C:/Users/kcola/Documents/Programing Fun/Python/GUI/Audio/Music/{song}.mp3'
    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops = 0)
    #Clear selection bar from selected song
    song_box.selection_clear(0, END)
    #Activate new song selection bar
    song_box.activate(next_one)
    song_box.selection_set(next_one, last = None)
#    lbl.config(text = 'Back', bg = '#ffffff')

def next():
    #Reset slider and status bar
    music_pos_slider.config(value = 0)
    status_bar.config(text = '')
#    lbl.config(text = 'End of List', bg = '#ffffff')
    next_one = song_box.curselection()
    next_one = next_one[0] + 1
    song = song_box.get(next_one)
    #Add directory structure back to song title
    song = f'C:/Users/kcola/Documents/Programing Fun/Python/GUI/Audio/Music/{song}.mp3'
    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops = 0)
    #Clear selection bar from selected song
    song_box.selection_clear(0, END)
    #Activate new song selection bar
    song_box.activate(next_one)
    song_box.selection_set(next_one, last = None)
#    lbl.config(text = 'Play', bg = '#ffffff')
#    pygame.mixer.music.fadeout()
#    main.config(bg = 'white')
#    lbl.config(text = '', bg = '#ffffff')

#Delete a song
def delete_song():
    stop()
    #Delete curently selected song
    song_box.delete(ANCHOR)
    #Stop music playing
#    pygame.mixer.music.stop()

#Delete a song
def delete_all_songs():
    #Call the sotp function because it stops the song and resets the slider bar
    stop()
    #Delete curently selected song
    song_box.delete(0, END)
    #Stop music playing
#    pygame.mixer.music.stop()

#Get song length time info
def play_time():
    if stopped:
        return
    #convert milliseconds to time
    current_time = pygame.mixer.music.get_pos() / 1000

#    music_pos_slider_lbl.config(text = f'Slider: {int(music_pos_slider.get())} and Song Pos {int(current_time)}')

    #Get current song
    current_song = song_box.curselection()
    song = song_box.get(current_song)
#    song = song_box.get(ACTIVE)
    #Add directory structure back to song title
    song = f'C:/Users/kcola/Documents/Programing Fun/Python/GUI/Audio/Music/{song}.mp3'

    #Load song into mutagen
    song_mut = MP3(song)
    #Get length
    global song_length
    song_length = song_mut.info.length
    #Convert to time format
    converted_song_length = time.strftime('%M:%S', time.gmtime(song_length))

    #Increase time by 1 second
    current_time += 1
    if int(music_pos_slider.get()) == int(song_length):
        status_bar.config(text = f'Time Elapsed: {converted_song_length} of {converted_song_length} ')
    elif paused:
        pass
    #Update time
    elif int(music_pos_slider.get()) == int(current_time):
        #Update slider position
        music_pos_slider_position = int(song_length)
        music_pos_slider.config(to = music_pos_slider_position, value = int(current_time))
    else:
        #Update slider position
        music_pos_slider_position = int(song_length)
        music_pos_slider.config(to = music_pos_slider_position, value = int(music_pos_slider.get()))
        #Conver to time format
        convert_ms_to_time = time.strftime('%H:%M:%S', time.gmtime(int(music_pos_slider.get())))
        status_bar.config(text = f'Time Elapsed: {convert_ms_to_time} of {converted_song_length} ')
        #Move slider along by 1 second
        next_time = int(music_pos_slider.get()) + 1
        music_pos_slider.config(value = next_time)
    #Display time to status bar
#    music_pos_slider.config(value = int(current_time))


    #Update time
    status_bar.after(1000, play_time)

def slide(x):
    song = song_box.get(ACTIVE)
    song = f'C:/Users/kcola/Documents/Programing Fun/Python/GUI/Audio/Music/{song}.mp3'
    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops = 0, start = int(music_pos_slider.get()))
#    music_pos_slider_lbl.config(text = f'{int(music_pos_slider.get())} of {int(song_length)}')

#create volume function
def volume(x):
    pygame.mixer.music.set_volume(vol_slider.get())
    current_volume = pygame.mixer.music.get_volume()
    slider_lbl.config(text = int(current_volume * 100))

def party_time():
    r = randint(0, 254)
    hex_r = hex(r)
    if r < 16:
        hex_r = str(hex_r)
        hex_r = "0" + hex_r[2:]
    else:
        hex_r = hex_r[2:]

    g = randint(0, 254)
    hex_g = hex(g)
    if g < 16:
        hex_g = str(hex_g)
        hex_g = "0" + hex_g[2:]
    else:
        hex_g = hex_g[2:]

    b = randint(0, 254)
    hex_b = hex(b)
    if b < 16:
        hex_b = str(hex_b)
        hex_b = "0" + hex_b[2:]
    else:
        hex_b = hex_b[2:]

    hex_color_code = "#" + hex_r + hex_g + hex_b
    main.config(bg = hex_color_code)
#    lbl.config(text = "Party Time!!!!", bg = hex_color_code)
    main.after(100, party_time)

#    print(hex_color_code)

master_frame = Frame(main, bg = 'white')
master_frame.pack(pady = 20)

#Create playlist box
song_box = Listbox(master_frame, bg = '#000000', fg = '#00ff00', width = 60, selectbackground = '#6d6d6d', selectforeground = '#000000')
song_box.grid(row = 0, column = 0)

#Define player control button images
back_btn_img = ImageTk.PhotoImage(Image.open('GUI/images/Buttons/back.jpg'))
next_btn_img = ImageTk.PhotoImage(Image.open('GUI/images/Buttons/next.jpg'))
play_btn_img = ImageTk.PhotoImage(Image.open('GUI/images/Buttons/play.jpg'))
pause_btn_img = ImageTk.PhotoImage(Image.open('GUI/images/Buttons/pause.jpg'))
stop_btn_img = ImageTk.PhotoImage(Image.open('GUI/images/Buttons/stop.jpg'))

#Create a player control frame
controls_frame = Frame(master_frame, bg = '#ffffff')
controls_frame.grid(row = 1, column = 0, pady = 20)

#Create volume lable frame
volume_frame = LabelFrame(master_frame, text = 'Volume', bg = 'white')
volume_frame.grid(row = 0, column = 1, padx = 20)

back_btn = Button(controls_frame, image = back_btn_img, borderwidth = 0, command = back)
next_btn = Button(controls_frame, image = next_btn_img, borderwidth = 0, command = next)
play_btn = Button(controls_frame, image = play_btn_img, borderwidth = 0, command = play)
pause_btn = Button(controls_frame, image = pause_btn_img, borderwidth = 0, command = lambda: pause(paused))
stop_btn = Button(controls_frame, image = stop_btn_img, borderwidth = 0, command = stop)

back_btn.grid(row = 1, column = 0, padx = 10, pady = 10)
next_btn.grid(row = 1, column = 4, padx = 10, pady = 10)
play_btn.grid(row = 1, column = 2, padx = 10, pady = 10)
pause_btn.grid(row = 1, column = 3, padx = 10, pady = 10)
stop_btn.grid(row = 1, column = 1, padx = 10, pady = 10)


#Create a menu
my_menu = Menu(main)
main.config(menu = my_menu, bg = 'white')

#Add song menu
add_song_menu = Menu(my_menu)
my_menu.add_cascade(label = 'Add Songs', menu = add_song_menu)
add_song_menu.add_command(label = 'Add 1 song to playlist', command = add_song)
#Add many songs ot playlist
add_song_menu.add_command(label = 'Add multiple songs to the playlist', command = add_many_songs)

remove_song_menu = Menu(my_menu)
my_menu.add_cascade(label = "Remove Songs", menu = remove_song_menu)
remove_song_menu.add_command(label = "Delete a Song from Playlist", command = delete_song)
remove_song_menu.add_command(label = "Delete All Songs from Playlist", command = delete_all_songs)

status_bar = Label(main, text = '', bd = 1, relief = GROOVE, anchor = E)
status_bar.pack(fill = X, side = BOTTOM, ipady = 2)

#Create a music position slider
music_pos_slider = ttk.Scale(master_frame, from_ = 0, to = 100, orient = HORIZONTAL, value = 0, command = slide, length = 360)
music_pos_slider.grid(row  = 2, column = 0, pady = 10)

#Create a volume slider
vol_slider = ttk.Scale(volume_frame, from_ = 1, to = 0, orient = VERTICAL, value = 1, command = volume, length = 125)
vol_slider.pack(padx = 10)

#Create a temp slider label
slider_lbl = Label(volume_frame, text = 0, bg = 'white')
slider_lbl.pack(pady = 10)

#play_btn = Button(main, text = 'Play Song', font = (('arial'), 32), bg = 'white', command = play)
#play_btn.pack(pady = 20)

#stop_btn = Button(main, text = "Stop =(", font = ('arial', 16), command = stop)
#stop_btn.pack(pady = 10)

#global lbl
#lbl = Label(controls_frame, text = '', font = ('arial', 18))
#lbl.grid(row = 1, column = 5)

main.mainloop()