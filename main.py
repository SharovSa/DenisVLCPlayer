import tkinter
from tkinter import Tk, Menu, END, Listbox, Button, PhotoImage, Frame, Scale, HORIZONTAL, X, BOTTOM, Label, GROOVE, E
import pygame
import os
import time
from player import Player
from song import Song

root = Tk()
root.title('DenisPlayer')
root.geometry("600x350")
root.resizable(width=False, height=False)
player_owner = Player()

try:
    pygame.mixer.init()
except:
    print("Аудиовыход не найден")

menubar = Menu(root)
root.config(menu=menubar)
songs = []


class Constants:
    isLoad = False


class GlobalPlayer:
    def __init__(self):
        self.organise_menu = Menu(menubar, tearoff=False)
        self.songlist = Listbox(root, bg="black", fg="white")

        self.play_btn_image = PhotoImage(file='logo/play.png')
        self.pause_btn_image = PhotoImage(file='logo/pause.png')
        self.next_btn_image = PhotoImage(file='logo/next.png')
        self.back_btn_image = PhotoImage(file='logo/back.png')
        self.cycle_btn_image = PhotoImage(file='logo/cycle.png')
        self.cycle_active_btn_image = PhotoImage(file='logo/cycle_active.png')
        self.random_btn_image = PhotoImage(file='logo/random.png')
        self.random_active_btn_image = PhotoImage(file='logo/random_active.png')
        self.add_btn_image = PhotoImage(file='logo/add.png')
        self.delete_btn_image = PhotoImage(file='logo/delete.png')
        self.erase_btn_image = PhotoImage(file='logo/eraser_queque.png')

        self.status_bar = Label(root, text='', bd=1, relief=GROOVE, anchor=E)

        self.control_frame = Frame(root)

        self.play_pause_btn = Button(self.control_frame, image=self.play_btn_image, borderwidth=0,
                                     command=self.play_pause_music)
        self.next_btn = Button(self.control_frame, image=self.next_btn_image, borderwidth=0, command=self.next_music)
        self.back_btn = Button(self.control_frame, image=self.back_btn_image, borderwidth=0, command=self.back_music)
        self.cycle_btn = Button(self.control_frame, image=self.cycle_btn_image, borderwidth=0,
                                command=self.cycle_button)
        self.add_btn = Button(self.control_frame, image=self.add_btn_image, borderwidth=0, command=self.add_track)
        self.random_btn = Button(self.control_frame, image=self.random_btn_image, borderwidth=0,
                                 command=self.random_button)
        self.delete_btn = Button(self.control_frame, image=self.delete_btn_image, borderwidth=0,
                                 command=self.delete_cur)
        self.erase_btn = Button(self.control_frame, image=self.erase_btn_image, borderwidth=0, command=self.clear_all)

        self.volume_slider = Scale(root, from_=0, to=100, orient=HORIZONTAL)

    def load_music(self):
        """
        Загружает музыку из папки
        :return:
        """
        root.directory = "songs/"

        for song in os.listdir(root.directory):
            name, ext = os.path.splitext(song)
            if ext == '.mp3':
                songs.append(song)

        for song in songs:
            self.songlist.insert("end", song)

        self.songlist.selection_set(0)

        Constants.current_song = songs[self.songlist.curselection()[0]]

    def play_pause_music(self):
        """
        Загружает музыку в функцию плеера, если она не загружена
        Ставит музыку на паузу или снимает с неё в зависимости от состояния player_owner
        :return:
        """
        if not Constants.isLoad:
            pygame.mixer.music.load(player_owner.get_manager().get_song().get_link())
            Constants.isLoad = True

        if player_owner.is_paused():
            if player_owner.is_playing():
                pygame.mixer.music.unpause()
            else:
                pygame.mixer.music.play()
                player_owner.set_playing(True)
            self.play_pause_btn.config(image=self.pause_btn_image)
            player_owner.set_pause(False)
        else:
            pygame.mixer.music.pause()
            player_owner.set_pause(True)
            self.play_pause_btn.config(image=self.play_btn_image)
        self.current_time()

    def next_music(self):
        """
        Включает следующую из очереди песню, либо берет следующую из списка всех песен
        в зависимости от состояния player_owner.
        Если песен в очереди нет и все песни из списка уже проиграны, то включает случайную.
        :return:
        """
        Constants.current_song = songs[self.songlist.curselection()[0]]
        cur_song = player_owner.get_manager().next_song()
        pygame.mixer.music.load(cur_song.get_link())
        self.songlist.selection_clear(0, END)
        self.songlist.selection_set(player_owner.get_manager().get_song().get_song_id())
        if not player_owner.get_manager().get_queue().check_track(cur_song):
            self.songlist.itemconfig(self.songlist.curselection()[0], bg='black')
        self.songlist.selection_clear(0, END)
        self.songlist.selection_set(player_owner.get_manager().get_song().get_song_id())
        self.songlist.selection_clear(0, END)
        self.songlist.selection_set(player_owner.get_manager().get_song().get_song_id())
        player_owner.set_pause(True)
        player_owner.set_playing(False)
        self.play_pause_music()

    def back_music(self):
        """
        Включает предыдущую из очереди проигранных песню, либо берет следующую из списка всех песен
        в зависимости от состояния player_owner.
        :return:
        """
        pygame.mixer.music.load(player_owner.get_manager().prew_song().get_link())
        self.songlist.selection_clear(0, END)
        self.songlist.selection_set(player_owner.get_manager().get_song().get_song_id())
        self.clear_all()
        player_owner.set_pause(True)
        player_owner.set_playing(False)
        self.play_pause_music()

    def add_track(self):
        """
        Добавляет выбранную песню в очередь проигрывания.
        :return:
        """
        player_owner.add_to_queue(self.songlist.curselection()[0])
        self.songlist.itemconfig(self.songlist.curselection()[0], bg='green')

    def change_volume(self, value):
        """
        Меняет громкость на переданную
        :param value: значение громкости
        :return:
        """
        volume = int(value) / 100  # Преобразование значения в диапазоне от 0 до 1
        pygame.mixer.music.set_volume(volume)

    def random_button(self):
        """
        Включает/выключает режим "слушать вперемешку"
        :return:
        """
        player_owner.get_manager().set_random_status(not player_owner.get_manager().get_random_status())
        if self.random_btn["image"] == 'pyimage7':
            self.random_btn.config(image=self.random_active_btn_image)
        else:
            self.random_btn.config(image=self.random_btn_image)

    def clear_all(self):
        """
        Очищает очередь
        :return:
        """
        player_owner.clear_queue()
        for i in range(0, self.songlist.size()):
            self.songlist.itemconfig(i, bg='black')

    def cycle_button(self):
        """
        Включает/выключает режим "повтор песни"
        :return:
        """
        player_owner.get_manager().set_cycle_status(not player_owner.get_manager().get_cycle_status())
        if self.cycle_btn["image"] == 'pyimage5':
            self.cycle_btn.config(image=self.cycle_active_btn_image)
        else:
            self.cycle_btn.config(image=self.cycle_btn_image)

    def delete_cur(self):
        """
        Удаляет выбранную песню из очереди
        :return:
        """
        cur_song = player_owner.get_manager().get_all_songs().get_song_by_id(self.songlist.curselection()[0])
        if not player_owner.get_manager().get_queue().delete_selected_song(cur_song):
            self.songlist.itemconfig(self.songlist.curselection()[0], bg='black')

    def current_time(self):
        """
        Выводит текущие время песни
        :return:
        """
        cur_time = pygame.mixer.music.get_pos() / 1000
        converted_time = time.strftime('%M:%S', time.gmtime(cur_time))
        self.status_bar.config(text=converted_time)
        if converted_time != '59:59':
            self.status_bar.after(1000, self.current_time)
        else:
            self.status_bar.config(text='')


if __name__ == "__main__":
    """
    Стартовая функция
    """
    global_player = GlobalPlayer()
    global_player.songlist.pack(fill=tkinter.BOTH, side=tkinter.TOP, expand=True)
    global_player.control_frame.pack()

    global_player.play_pause_btn.grid(row=0, column=4, padx=7, pady=10)
    global_player.next_btn.grid(row=0, column=5, padx=7, pady=10)
    global_player.back_btn.grid(row=0, column=3, padx=7, pady=10)
    global_player.cycle_btn.grid(row=0, column=2, padx=7, pady=10)
    global_player.random_btn.grid(row=0, column=0, padx=7, pady=10)
    global_player.add_btn.grid(row=0, column=6, padx=7, pady=10)
    global_player.delete_btn.grid(row=0, column=7, padx=7, pady=10)
    global_player.erase_btn.grid(row=0, column=8, padx=7, pady=10)

    global_player.volume_slider.pack()
    global_player.volume_slider.set(100)
    global_player.volume_slider.config(command=global_player.change_volume)

    global_player.load_music()  # загрузка треков при запуске

    global_player.status_bar.pack(fill=X, side=BOTTOM, ipadx=2)

    root.mainloop()
