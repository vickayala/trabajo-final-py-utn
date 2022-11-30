import sqlite3


class DB:
    def __init__(self, dbName):
        # con = sqlite3.connect("mibase.db")
        self.name = dbName
        self.connection()

    def connection(self):
        self.conn = sqlite3.connect(self.name)
