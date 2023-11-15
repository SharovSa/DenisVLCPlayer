class Song:
    __name = ""
    __author = ""
    __duration = 0
    __picture = ""
    __link = ""
    __song_id = 0

    def __init__(self, name="", author="", duration=-1, picture="", link="", song_id=-1):
        self.__name = name
        self.__link = link
        self.__song_id = song_id
        self.__picture = picture
        self.__duration = duration
        self.__author = author

    def get_name(self):
        return self.__name

    def get_author(self):
        return self.__author

    def get_duration(self):
        return self.__duration

    def get_picture(self):
        return self.__picture

    def get_link(self):
        return self.__link

    def get_song_id(self):
        return self.__song_id

    def set_name(self, name_):
        self.__name = name_

    def set_author(self, author_):
        self.__author = author_

    def set_duration(self, duration_):
        self.__duration = duration_

    def set_picture(self, picture_):
        self.__picture = picture_

    def set_link(self, link_):
        self.__link = link_

    def set_song_id(self, song_id_):
        self.__song_id = song_id_
