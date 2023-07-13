import eyed3
import os
from song import Song
import random
class SongHolder:

    def __init__(self):
        self.songs_array = []
        self.count = 0

        directory = os.getcwd()

        for file in os.listdir(directory):
            filename = os.fsdecode(file)

            if filename.endswith(".mp3"):

                file = eyed3.load(filename)
                title = file.tag.title

                if title is None:
                    title = filename

                cursong = Song(title, file.tag.artist, file.info.time_secs, "-", filename, self.count)
                self.songs_array.append(cursong)
                self.count += 1
        pass

    def SongList(self):
        for i in self.songs_array:
            print(i.get_name())



    def Checkmemory(self):
        directory = os.getcwd()
        for file in os.listdir(directory):
            filename = os.fsdecode(file)
            if filename.endswith(".mp3"):
                self.count += 1
                file = eyed3.load(filename)
                title = file.tag.title
                if title is None:
                    title = filename

                print(title)

    def GetRandomSong(self):
        elem = random.randint(0, self.count - 1)
        return self.songs_array[elem]

    def GetSongById(self, id):
        if id < 0 or id >= self.count:
            return self.GetRandomSong()
        return self.songs_array[id]


