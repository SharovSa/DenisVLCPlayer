import pygame

from SongManager import *
from main import play_pause_btn, pause_btn_image, Constants, play_btn_image


class Player:
    def __init__(self):
        self.__is_paused = False
        self.__is_random = False
        self.__time = 0
        self.__song_manager = SongManager()


    def play_pause(self):
        if not self.__is_paused:
            pygame.mixer.music.load(SongManager.next_song())
            pygame.mixer.music.play()
            play_pause_btn.config(image=pause_btn_image)
            Constants.paused = True
        else:
            pygame.mixer.music.pause()
            Constants.paused = False
            play_pause_btn.config(image=play_btn_image)