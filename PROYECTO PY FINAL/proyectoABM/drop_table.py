from connection import DB


def drop_table(table):
    db = DB("mibase.db")
    con = db.conn
    cursor = con.cursor()
    drop = "DROP TABLE " + table
    cursor.execute(drop)
    con.commit()
    cursor.close()
    con.close()


userInput = input("Cuál tabla desea borrar?")

drop_table(userInput)
