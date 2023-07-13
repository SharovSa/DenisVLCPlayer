import eyed3
import os
from song import Song
import random
class SongHolder:

    def __init__(self):
        self.__songs_array = []
        self.__count = 0

        directory = os.getcwd()

        for file in os.listdir(directory):
            filename = os.fsdecode(file)

            if filename.endswith(".mp3"):

                file = eyed3.load(filename)
                title = file.tag.title

                if title is None:
                    title = filename

                cursong = Song(title, file.tag.artist, file.info.time_secs, "-", filename, self.__count)
                self.__songs_array.append(cursong)
                self.__count += 1
        pass

    def song_list(self):
        for i in self.__songs_array:
            print(i.get_name())



    def Checkmemory(self):
        directory = os.getcwd()
        for file in os.listdir(directory):
            filename = os.fsdecode(file)
            if filename.endswith(".mp3"):
                self.__count += 1
                file = eyed3.load(filename)
                title = file.tag.title
                if title is None:
                    title = filename

                print(title)

    def get_random_song(self):
        elem = random.randint(0, self.__count - 1)
        return self.__songs_array[elem]

    def get_song_by_id(self, id):
        if id < 0 or id >= self.__count:
            return self.get_random_song()
        return self.__songs_array[id]


