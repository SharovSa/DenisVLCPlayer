from UserQueue import UserQueue
from songholder import SongHolder
from song import Song


class SongManager:

    def __init__(self):
        self.__current_playlist = UserQueue()
        self.__all_songs = SongHolder()
        self.__playing_song = self.__all_songs.get_song_by_id(0)
        self.__played_songs = []
        self.__is_random = False
        self.__is_cycled = False
        self.__size_of_remaining = 5

    def prew_song(self):
        """
        Проверяет состояния SongManager и в зависимости от них возвращает предыдущую песню
        :return: предыдущая песня
        """
        if self.__is_cycled:
            return self.get_song()
        if len(self.__played_songs) != 0:
            tmp = self.__playing_song
            self.__playing_song = self.get_last_played_song()
            # self.add_song_to_queue(tmp)
            return self.__playing_song
        if self.__is_random:
            self.add_song_to_queue(self.__playing_song)
            self.__playing_song = self.get_all_songs().get_random_song(self.__playing_song.get_song_id())
            return self.__playing_song
        curr_id = self.__playing_song.get_song_id()
        if curr_id != 0:
            self.add_song_to_queue(self.__playing_song)
        self.__playing_song = self.__all_songs.get_song_by_id(curr_id - 1)
        return self.__playing_song

    def next_song(self):
        """
        Проверяет состояния SongManager и UserQueue и в зависимости от них возвращает следующую песню
        :return: следующая песня
        """
        if self.__is_cycled:
            return self.get_song()
        if self.__current_playlist.get_count_of_songs() > 0:
            self.add_to_played(self.__playing_song)
            self.__playing_song = self.__current_playlist.get_next()
            return self.__playing_song
        if self.__is_random:
            self.add_to_played(self.__playing_song)
            self.__playing_song = self.__all_songs.get_random_song(self.__playing_song.get_song_id())
            return self.__playing_song
        curr_id = self.__playing_song.get_song_id()
        self.add_to_played(self.__playing_song)
        self.__playing_song = self.__all_songs.get_song_by_id(curr_id + 1)
        # self.__current_playlist.add_song_to_queue(self.__playing_song)
        return self.__playing_song

    def get_song(self):
        return self.__playing_song

    def change_song_to_selected(self, song):
        """
        Меняет текущую играющую песню на выбранную
        :param song: выбранная песня
        :return:
        """
        self.add_to_played(self.__playing_song)
        self.__playing_song = song
        self.__current_playlist = UserQueue()
        self.__current_playlist.add_song_to_queue(self.__playing_song)

    def add_song_to_queue(self, song):
        self.__current_playlist.add_song_to_queue(song)
        self.__current_playlist.get_next_list()

    def add_song_to_queue_end(self, song):
        self.__current_playlist.add_song_to_queue_end(song)
        self.__current_playlist.get_next_list()

    def delete_song_from_queue(self, curr_song):
        self.__current_playlist.delete_selected_song(curr_song)
        self.__current_playlist.get_next_list()

    def set_random_status(self, flag):
        self.__is_random = flag

    def get_random_status(self):
        return self.__is_random

    def add_to_played(self, song):
        """
        Добавляет отыгранную песню в очередь отыгранных
        :param song: отыгранная песня
        :return:
        """
        if len(self.__played_songs) == self.__size_of_remaining:
            self.__played_songs.pop(0)
        self.__played_songs.append(song)

    def get_last_played_song(self):
        """
        Возвращает предыдущую отыгранную песню
        :return:
        """
        return self.__played_songs.pop()

    def get_all_songs(self):
        return self.__all_songs

    def get_queue(self):
        return self.__current_playlist

    def get_cycle_status(self):
        return self.__is_cycled

    def set_cycle_status(self, flag):
        self.__is_cycled = flag
