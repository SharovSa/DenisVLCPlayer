import eyed3
import os
from song import Song
import random


class SongHolder:

    def __init__(self):
        self.__songs_array = []
        self.__count = 0
        # directory = os.getcwd() + "\\songs\\"
        directory = os.path.join(os.getcwd(), "songs/")
        for file in os.listdir(directory):
            songname = os.fsdecode(file)
            filename = directory + songname

            if filename.endswith(".mp3"):

                file = eyed3.load(filename)
                title = file.tag.title

                if title is None:
                    title = songname

                cursong = Song(title, file.tag.artist, file.info.time_secs, "-", filename, self.__count)
                self.__songs_array.append(cursong)
                self.__count += 1

    def song_list(self):
        for i in self.__songs_array:
            print(i.get_name())

    def check_memory(self):

        directory = os.chdir('songs')

        for file in os.listdir(directory):
            filename = os.fsdecode(file)

            if filename.endswith(".mp3"):

                file = eyed3.load(filename)
                title = file.tag.title

                if title is None:
                    title = filename

                cursong = Song(title, file.tag.artist, file.info.time_secs, "-", filename, self.__count)
                if not (cursong in self.__songs_array):
                    self.__songs_array.append(cursong)
                    self.__count += 1

    def get_random_song(self, id):
        elem = random.randint(0, self.__count - 1)
        if elem == id:
            if elem + 1 >= self.__count:
                return self.__songs_array[elem - 1]
            else:
                return self.__songs_array[elem + 1]
        return self.__songs_array[elem]

    def get_song_by_id(self, id):
        if id < 0:
            return self.__songs_array[0]
        if id >= self.__count:
            return self.get_random_song(id)
        return self.__songs_array[id]

    def get_song_list(self):
        return self.__songs_array
