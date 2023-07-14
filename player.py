import pygame

from SongManager import SongManager



class Player:
    def __init__(self):
        self.__is_paused = True
        self.__is_playing = False
        self.__is_random = False
        self.__time = 0
        self.__song_manager = SongManager()


    def is_paused(self):
        return self.__is_paused

    def is_playing(self):
        return self.__is_playing

    def set_pause(self, flag):
        self.__is_paused = flag

    def set_playing(self, flag):
        self.__is_playing = flag

    def get_manager(self):
        return self.__song_manager

    def add_to_queue(self, flag):
        self.__song_manager.add_song_to_queue_end(self.__song_manager.get_all_songs().get_song_by_id(flag))
        print(self.__song_manager.get_queue().get_count_of_songs())
