from connection import DB


def create_table():
    db = DB("mibase.db")
    con = db.conn
    cursor = con.cursor()
    sql = """CREATE TABLE movies 
             (id INTEGER PRIMARY KEY AUTOINCREMENT,
             title varchar(20) NOT NULL,
             description varchar(300),
             genre varchar(20) NOT NULL,
             language varchar(20) NOT NULL,
             length varchar(20) NOT NULL
             )
    """
    cursor.execute(sql)
    con.commit()
    cursor.close()


create_table()
