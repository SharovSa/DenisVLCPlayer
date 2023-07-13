from UserQueue import UserQueue
from songholder import SongHolder
from song import Song


class SongManager:
    __current_playlist = UserQueue()
    __all_songs = SongHolder()
    __playing_song = Song()

    def __init__(self):
        pass

    def prew_song(self):
        curr_id = self.__playing_song.get_song_id()
        self.__playing_song = self.__all_songs.GetSongById(curr_id - 1)
        self.__current_playlist = UserQueue()
        self.__current_playlist.add_song_to_queue(self.__playing_song)

    def next_song(self):
        curr_id = self.__playing_song.get_song_id()
        self.__playing_song = self.__all_songs.GetSongById(curr_id + 1)
        self.__current_playlist = UserQueue()
        self.__current_playlist.add_song_to_queue(self.__playing_song)

    def get_song(self):
        return self.__playing_song

    def change_song_to_selected(self, song):
        self.__playing_song = song
        self.__current_playlist = UserQueue()
        self.__current_playlist.add_song_to_queue(self.__playing_song)

    def add_song_to_queue(self, song):
        self.__current_playlist.add_song_to_queue(song)

    def delete_song_from_queue(self):
        self.__current_playlist.delete_last_song()