import eyed3
import os

class SongHolder:
    def __init__(self):
        pass

        def Checkmemory(self):
            directory = os.getcwd()
            for file in os.listdir(directory):
                filename = os.fsdecode(file)
                print(filename)
                if filename.endswith(".mp3"):
                    self = eyed3.load(filename)
                    print(self.tag.album)

pol = SongHolder()
pol.Checkmemory()