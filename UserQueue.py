from song import Song


class UserQueue:
    __count = 0
    __songs_playlist = []

    def __init__(self, count=0, songs_playlist=None):
        if songs_playlist is None:
            songs_playlist = []
        self.__count = count
        self.__songs_playlist = songs_playlist

    def add_song_to_queue(self, song):
        self.__songs_playlist.append(song)
        self.__count += 1

    def get_next(self):
        return self.__songs_playlist.pop(0)

    def clear_queue(self):
        self.__count = 0
        while self.__songs_playlist:
            self.__songs_playlist.pop()

    def get_count_of_songs(self):
        return self.__count

    def delete_selected_song(self, curr_song):
        for i in range(0, self.__count):
            song = self.__songs_playlist[i]
            if song.get_link() == curr_song:
                self.__songs_playlist.pop(i)
                break
