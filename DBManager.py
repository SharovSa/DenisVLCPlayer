import sqlite3 as sql
from playlist import Playlist
from song import Song

class DBManager:
    db_name = "player.db"

    def __init__(self):
        self.con = sql.connect(self.db_name)
        self.cur = self.con.cursor()
        self.cur.execute("create table if not exists playlists(playlist_id, song_id)")
        self.cur.execute("create table if not exists pl_props(id INTEGER PRIMARY KEY ASC, name TEXT, pic_name TEXT, "
                         "count_of_songs INTEGER, duration INTEGER)")
        self.cur.execute("create table if not exists song_props(id INTEGER PRIMARY KEY ASC, author TEXT, name TEXT, "
                         "duration INTEGER, picture TEXT, link TEXT, album TEXT)")
        self.con.commit()
        self.con.close()

    def get_playlists(self):
        """
        :return: список плейлистов( id плейлиста = индекс в списке + 1)
        """
        con = sql.connect(self.db_name)
        cur = con.cursor()
        playlists = []
        for playlist in cur.execute("select * from pl_props"):
            playlists.append(Playlist(playlist[0],playlist[1], playlist[3], playlist[4], playlist[2]))
        con.close()
        return playlists

    def add_playlist(self, name, pic_name="", count_of_songs=0, duration=0):
        con = sql.connect(self.db_name)
        cur = con.cursor()
        cur.execute(f"insert into pl_props(name, pic_name, count_of_songs, duration) values ('{name}', '{pic_name}',"
                    f" {count_of_songs}, {duration})")
        con.commit()
        con.close()

    def add_song_to_playlist(self, playlist_id, song_id):
        con = sql.connect(self.db_name)
        cur = con.cursor()
        cur.execute(f"insert into playlists values ({playlist_id}, {song_id})")
        con.commit()
        con.close()

    def add_song(self, song, album):
        con = sql.connect(self.db_name)
        cur = con.cursor()
        cur.execute(f"insert into song_props(author, name, duration, picture, link, album) values"
                    f" ('{song.get_author()}', '{song.get_name()}', {song.get_duration()}, '{song.get_picture()}',"
                    f" '{song.get_link()}', '{album}')")
        con.commit()
        con.close()

    def get_songs_from_playlist(self, pl_id):
        con = sql.connect(self.db_name)
        cur = con.cursor()
        songs = []
        for song in cur.execute(f"select * from playlists where playlist_id = {pl_id}"):
            songs.append(song[1])
        print(*songs)
        con.close()

    def get_songs(self):
        con = sql.connect(self.db_name)
        cur = con.cursor()
        songs = []
        for song in cur.execute("select * from song_props"):
            songs.append(Song(song[2], song[1], song[3], song[4], song[5], song[0]))
        con.close()



manager = DBManager()
manager.get_songs_from_playlist(1)

