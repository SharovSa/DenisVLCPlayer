from tkinter import filedialog
from tkinter import Tk
from tkinter import Menu
from tkinter import END
from tkinter import Listbox
from tkinter import PhotoImage
from tkinter import Button
from tkinter import Frame
import pygame
import os


root = Tk()
root.title('DenisPlayer')
root.geometry("500x300")

try:
    pygame.mixer.init()
except:
    print("Аудиовыход не найден")

menubar = Menu(root)
root.config(menu=menubar)

songs = []

class Constants:
    current_song = ""
    paused = False

def load_music():
    root.directory = "songs/"

    for song in os.listdir(root.directory):
        name, ext = os.path.splitext(song)
        if ext == '.mp3':
            songs.append(song)

    for song in songs:
        songlist.insert("end", song)

    songlist.selection_set(0)
    songlist.itemconfig(1, bg='green')
    Constants.current_song = songs[songlist.curselection()[0]]
    a = 1


def play_pause_music():

    if not Constants.paused:
        pygame.mixer.music.load(os.path.join(root.directory, Constants.current_song))
        pygame.mixer.music.play()
        play_pause_btn.config(image=pause_btn_image)
        Constants.paused = True
    else:
        pygame.mixer.music.pause()
        Constants.paused = False
        play_pause_btn.config(image=play_btn_image)


def next_music():

    try:
        songlist.selection_clear(0, END)
        songlist.selection_set(songs.index(Constants.current_song) + 1)
        Constants.current_song = songs[songlist.curselection()[0]]
        play_pause_music()
    except:
        pass


def back_music():
    try:
        songlist.selection_clear(0, END)
        songlist.selection_set(songs.index(Constants.current_song) - 1)
        Constants.current_song = songs[songlist.curselection()[0]]
        play_pause_music()
    except:
        pass


organise_menu = Menu(menubar, tearoff=False)
songlist = Listbox(root, bg="red", fg="white", width=100, height=15)
songlist.pack()

play_btn_image = PhotoImage(file='play.png')
pause_btn_image = PhotoImage(file='pause.png')
next_btn_image = PhotoImage(file='next.png')
back_btn_image = PhotoImage(file='back.png')
cycle_btn_image = PhotoImage(file='cycle.png')
random_btn_image = PhotoImage(file='random.png')
add_btn_image = PhotoImage(file='add.png')
delete_btn_image = PhotoImage(file='delete.png')

control_frame = Frame(root)
control_frame.pack()

play_pause_btn = Button(control_frame, image=play_btn_image, borderwidth=0, command=play_pause_music)
next_btn = Button(control_frame, image=next_btn_image, borderwidth=0, command=next_music)
back_btn = Button(control_frame, image=back_btn_image, borderwidth=0, command=back_music)
cycle_btn = Button(control_frame, image=cycle_btn_image, borderwidth=0)
random_btn = Button(control_frame, image=random_btn_image, borderwidth=0)
add_btn = Button(control_frame, image=add_btn_image, borderwidth=0)
delete_btn = Button(control_frame, image=delete_btn_image, borderwidth=0)

play_pause_btn.grid(row=0, column=4, padx=7, pady=10)
next_btn.grid(row=0, column=5, padx=7, pady=10)
back_btn.grid(row=0, column=3, padx=7, pady=10)
cycle_btn.grid(row=0, column=2, padx=7, pady=10)
random_btn.grid(row=0, column=0, padx=7, pady=10)
add_btn.grid(row=0, column=6, padx=7, pady=10)
delete_btn.grid(row=0, column=7, padx=7, pady=10)

load_music() # загрузка треков при запуске

root.mainloop()
