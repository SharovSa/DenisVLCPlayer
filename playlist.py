class Playlist:
    __id = 0
    __name = ""
    __count_of_songs = 0
    __duration = 0
    __pic_name = ""

    def __init__(self, id=0, name='', count_of_songs=0, duration=0, pic_name=''):
        self.__id = id
        self.__name = name
        self.__count_of_songs = count_of_songs
        self.__duration = duration
        self.__pic_name = pic_name

    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name

    def get_count_of_songs(self):
        return self.__count_of_songs

    def get_duration(self):
        return self.__duration

    def get_pic_name(self):
        return self.__pic_name
