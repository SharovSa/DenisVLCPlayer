import tkinter
from tkinter import Tk, Menu, END, Listbox, Button, PhotoImage, Frame, Scale, HORIZONTAL, Label, BOTTOM, X, GROOVE, E
import pygame
import os
import time
from player import Player
from song import Song

root = Tk()
root.title('DenisPlayer')
root.geometry("600x350")
player_owner = Player()
try:
    pygame.mixer.init()
except:
    print("Аудиовыход не найден")

menubar = Menu(root)
root.config(menu=menubar)
songs = []


class Constants:
    current_song = ""
    isLoad = False


def load_music():
    root.directory = "songs/"

    for song in os.listdir(root.directory):
        name, ext = os.path.splitext(song)
        if ext == '.mp3':
            songs.append(song)

    for song in songs:
        songlist.insert("end", song)

    songlist.selection_set(0)

    Constants.current_song = songs[songlist.curselection()[0]]



def play_pause_music():
    if not Constants.isLoad:
        pygame.mixer.music.load(player_owner.get_manager().get_song().get_link())
        Constants.isLoad = True

    if player_owner.is_paused():
        if player_owner.is_playing():
            pygame.mixer.music.unpause()
        else:
            pygame.mixer.music.play()
            player_owner.set_playing(True)
        play_pause_btn.config(image=pause_btn_image)
        player_owner.set_pause(False)
    else:
        """if pygame.mixer.music.get_busy():
            Constants.isPlaying = True
        else:
            Constants.isPlaying = False"""
        pygame.mixer.music.pause()
        player_owner.set_pause(True)
        play_pause_btn.config(image=play_btn_image)

    current_time()

def next_music():

    try:
        Constants.current_song = songs[songlist.curselection()[0]]
        cur_song = player_owner.get_manager().next_song()
        pygame.mixer.music.load(cur_song.get_link())
        songlist.selection_clear(0, END)
        songlist.selection_set(player_owner.get_manager().get_song().get_song_id())
        if not player_owner.get_manager().get_queue().check_track(cur_song):
            songlist.itemconfig(songlist.curselection()[0], bg='black')

        songlist.selection_clear(0, END)
        songlist.selection_set(player_owner.get_manager().get_song().get_song_id())
        songlist.selection_clear(0, END)
        songlist.selection_set(player_owner.get_manager().get_song().get_song_id())
        player_owner.set_pause(True)
        player_owner.set_playing(False)
        play_pause_music()
    finally:
        pass


def back_music():

    try:

        Constants.current_song = songs[songlist.curselection()[0]]
        pygame.mixer.music.load(player_owner.get_manager().prew_song().get_link())
        songlist.selection_clear(0, END)
        songlist.selection_set(player_owner.get_manager().get_song().get_song_id())
        clear_all()
        player_owner.set_pause(True)
        player_owner.set_playing(False)
        play_pause_music()
    except:
        pass

def add_track():
    player_owner.add_to_queue(songlist.curselection()[0])
    songlist.itemconfig(songlist.curselection()[0], bg='green')

def change_volume(value):
    volume = int(value) / 100  # Преобразование значения в диапазоне от 0 до 1
    pygame.mixer.music.set_volume(volume)


def random_button():
    player_owner.get_manager().set_random_status(not player_owner.get_manager().get_random_status())
    if random_btn["image"] == 'pyimage7':
        random_btn.config(image=random_active_btn_image)
    else:
        random_btn.config(image=random_btn_image)


def clear_all():
    player_owner.clear_queue()
    for i in range(0, songlist.size()):
        songlist.itemconfig(i, bg='black')


def cycle_button():
    player_owner.get_manager().set_cycle_status(not player_owner.get_manager().get_cycle_status())
    if cycle_btn["image"] == 'pyimage5':
        cycle_btn.config(image=cycle_active_btn_image)
    else:
        cycle_btn.config(image=cycle_btn_image)

def delete_cur():
    cur_song = player_owner.get_manager().get_all_songs().get_song_by_id(songlist.curselection()[0])
    if not player_owner.get_manager().get_queue().delete_selected_song(cur_song):
        songlist.itemconfig(songlist.curselection()[0], bg='black')

def current_time():
    cur_time = pygame.mixer.music.get_pos() / 1000
    converted_time = time.strftime('%M:%S', time.gmtime(cur_time))
    status_bar.config(text=converted_time)
    if converted_time != '59:59':
        status_bar.after(1000, current_time)
    else:
        status_bar.config(text='')

organise_menu = Menu(menubar, tearoff=False)
songlist = Listbox(root, bg="black", fg="white")
songlist.pack(fill=tkinter.BOTH, side=tkinter.TOP, expand=True)

play_btn_image = PhotoImage(file='logo/play.png')
pause_btn_image = PhotoImage(file='logo/pause.png')
next_btn_image = PhotoImage(file='logo/next.png')
back_btn_image = PhotoImage(file='logo/back.png')
cycle_btn_image = PhotoImage(file='logo/cycle.png')
cycle_active_btn_image = PhotoImage(file='logo/cycle_active.png')
random_btn_image = PhotoImage(file='logo/random.png')
random_active_btn_image = PhotoImage(file='logo/random_active.png')
add_btn_image = PhotoImage(file='logo/add.png')
delete_btn_image = PhotoImage(file='logo/delete.png')
erase_btn_image = PhotoImage(file='logo/eraser_queque.png')

control_frame = Frame(root)
control_frame.pack()

play_pause_btn = Button(control_frame, image=play_btn_image, borderwidth=0, command=play_pause_music)
next_btn = Button(control_frame, image=next_btn_image, borderwidth=0, command=next_music)
back_btn = Button(control_frame, image=back_btn_image, borderwidth=0, command=back_music)
cycle_btn = Button(control_frame, image=cycle_btn_image, borderwidth=0, command=cycle_button)
add_btn = Button(control_frame, image=add_btn_image, borderwidth=0, command=add_track)
random_btn = Button(control_frame, image=random_btn_image, borderwidth=0, command=random_button)
delete_btn = Button(control_frame, image=delete_btn_image, borderwidth=0, command=delete_cur)
erase_btn = Button(control_frame, image=erase_btn_image, borderwidth=0, command=clear_all)

play_pause_btn.grid(row=0, column=4, padx=7, pady=10)
next_btn.grid(row=0, column=5, padx=7, pady=10)
back_btn.grid(row=0, column=3, padx=7, pady=10)
cycle_btn.grid(row=0, column=2, padx=7, pady=10)
random_btn.grid(row=0, column=0, padx=7, pady=10)
add_btn.grid(row=0, column=6, padx=7, pady=10)
delete_btn.grid(row=0, column=7, padx=7, pady=10)
erase_btn.grid(row=0, column=8, padx=7, pady=10)

volume_slider = Scale(root, from_=0, to=100, orient=HORIZONTAL)
volume_slider.pack()
volume_slider.set(100)

volume_slider.config(command=change_volume)

status_bar = Label(root, text='', bd = 1, relief=GROOVE, anchor=E)
status_bar.pack(fill=X, side=BOTTOM, ipadx=2)


load_music()  # загрузка треков при запуске

root.mainloop()
