import sqlite3 as sql


class DBManager:
    def __init__(self):
        self.con = sql.connect("player.db")
        self.cur = self.con.cursor()
        self.cur.execute("create table if not exists playlists(playlist_id INTEGER, song_id INTEGER)")
        self.cur.execute("create table if not exists pl_props(id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, name TEXT, pic_name TEXT, count_of_songs INTEGER, duration INTEGER)")
        self.cur.execute("create table if not exists song_props(id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, author TEXT, name TEXT, duration INTEGER, picture TEXT, link TEXT, album TEXT)")
        self.con.commit()

    def get_playlists(self):
        playlists = self.cur.execute("select * from pl_props")
        playlists.fetchall()


manager = DBManager()

