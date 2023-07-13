from song import Song


class UserQueue:
    __current_position = 0
    __count = 0
    __songs_playlist = []

    def __init__(self, current_position=0, count=0, songs_playlist=None):
        if songs_playlist is None:
            songs_playlist = []
        self.__current_position = current_position
        self.__count = count
        self.__songs_playlist = songs_playlist

    def delete_last_song(self):
        if self.__songs_playlist:
            self.__songs_playlist.pop()
        else:
            return
        if self.__current_position == (self.__count - 1):
            self.__current_position -= 1
        self.__count -= 1

    def add_song_to_queue(self, song):
        self.__songs_playlist.append(song)
        self.__count += 1

    def get_next(self):
        if self.__current_position + 1 == self.__count:
            self.__current_position = 0
        else:
            self.__current_position += 1
        return self.__songs_playlist[self.__current_position]

    def get_previous(self):
        if self.__current_position == 0:
            self.__current_position = self.__count - 1
        else:
            self.__current_position -= 1
        return self.__songs_playlist[self.__current_position]

    def clear_queue(self):
        while self.__songs_playlist:
            self.__songs_playlist.pop()
