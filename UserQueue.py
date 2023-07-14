from song import Song


class UserQueue:

    def __init__(self, count=0, songs_playlist=None):
        if songs_playlist is None:
            songs_playlist = []

        self.__songs_playlist = songs_playlist

    def add_song_to_queue(self, song):
        self.__songs_playlist.insert(0, song)

    def add_song_to_queue_end(self, song):
        self.__songs_playlist.append(song)

    def check_track(self, song):
        for track in self.__songs_playlist:
            if track.get_link() == song.get_link():
                return True
        return False

    def get_next(self):
        return self.__songs_playlist.pop(0)

    def clear_queue(self):
        self.__songs_playlist.clear()

    def get_count_of_songs(self):
        return len(self.__songs_playlist)

    def get_next_list(self):
        for i in self.__songs_playlist:
            print(i.get_name())

    def delete_selected_song(self, curr_song):
        deleted = False
        has_dublicate = False
        for i in range(len(self.__songs_playlist) - 1, -1, -1):
            song = self.__songs_playlist[i]
            if song == curr_song and not deleted:
                self.__songs_playlist.pop(i)
                deleted = True
            if song == curr_song and deleted:
                has_dublicate = True
                break
        return has_dublicate
