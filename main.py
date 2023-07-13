import tkinter
from tkinter import *
import pygame
import os


root = Tk()
root.title('DenisPlayer')
root.geometry("600x350")

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
    isLoad = False
    isPlaying = False

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


def play_pause_music():
    if not Constants.isLoad:
        pygame.mixer.music.load(os.path.join(root.directory, Constants.current_song))
        Constants.isLoad = True

    if not Constants.paused:
        if Constants.isPlaying:
            pygame.mixer.music.unpause()
        else:
            pygame.mixer.music.play()
        play_pause_btn.config(image=pause_btn_image)
        Constants.paused = True
    else:
        if pygame.mixer.music.get_busy():
            Constants.isPlaying = True
        else:
            Constants.isPlaying = False
        pygame.mixer.music.pause()
        Constants.paused = False
        play_pause_btn.config(image=play_btn_image)


def next_music():
    Constants.isLoad = False
    try:
        songlist.selection_clear(0, END)
        if songs.index(Constants.current_song) != songlist.size() - 1:
            songlist.selection_set(songs.index(Constants.current_song) + 1)
        else:
            songlist.selection_set(0)
        #songlist.selection_set(songs.index(Constants.current_song) + 1)
        Constants.current_song = songs[songlist.curselection()[0]]
        Constants.paused = False
        play_pause_music()
    except:
        pass


def back_music():
    Constants.isLoad = False
    try:
        songlist.selection_clear(0, END)
        if songs.index(Constants.current_song) != 0:
            songlist.selection_set(songs.index(Constants.current_song) - 1)
        else:
            songlist.selection_set(songlist.size() - 1)
        #songlist.selection_set(songs.index(Constants.current_song) - 1)
        Constants.current_song = songs[songlist.curselection()[0]]
        Constants.paused = False
        play_pause_music()
    except:
        pass

def change_volume(value):
    volume = int(value) / 100  # Преобразование значения в диапазоне от 0 до 1
    pygame.mixer.music.set_volume(volume)

organise_menu = Menu(menubar, tearoff=False)
songlist = Listbox(root, bg="red", fg="white", width=100, height=15)
songlist.pack()

play_btn_image = PhotoImage(file='logo/play.png')
pause_btn_image = PhotoImage(file='logo/pause.png')
next_btn_image = PhotoImage(file='logo/next.png')
back_btn_image = PhotoImage(file='logo/back.png')
cycle_btn_image = PhotoImage(file='logo/cycle.png')
random_btn_image = PhotoImage(file='logo/random.png')
add_btn_image = PhotoImage(file='logo/add.png')
delete_btn_image = PhotoImage(file='logo/delete.png')

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

volume_slider = Scale(root, from_=0, to=100, orient=HORIZONTAL)
volume_slider.pack(anchor=tkinter.S)
volume_slider.set(100)

volume_slider.config(command=change_volume)

load_music() # загрузка треков при запуске

root.mainloop()
