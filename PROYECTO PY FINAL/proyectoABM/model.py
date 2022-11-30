import re
from connection import DB


class Model:
    def __init__(self):
        db = DB("mibase.db")
        self.connection = db.conn

    def create(self, title, description, genre, language, length):
        patron = "^[A-Za-záéíóú]*$"
        if re.match(patron, title):
            print(title, description, genre, language, length)
            cursor = self.connection.cursor()
            data = (title, description, genre, language, length)
            sql = "INSERT INTO movies(title, description, genre, language, length) VALUES(?, ?, ?, ?, ?)"
            try:
                cursor.execute(sql, data)
                self.connection.commit()
                print("Se creo con exito la lista")
                return self.reset_search()
            except Exception as err:
                print("Error en la base de datos", err)
            cursor.close()
        else:
            print("Error guardando la lista")

    def search(self, title, genre):
        if (title == "") and (genre == ""):
            return self.reset_search()
        else:
            cursor = self.connection.cursor()
            searchQuery = "SELECT * FROM movies WHERE title=? OR genre=?"
            datos = cursor.execute(
                searchQuery,
                (
                    title,
                    genre,
                ),
            )
            resultados = datos.fetchall()
            cursor.close()
            return resultados

    def delete(self, id):
        cursor = self.connection.cursor()
        data = (id,)
        sql = "DELETE FROM movies WHERE id = ?;"
        cursor.execute(sql, data)
        self.connection.commit()
        cursor.close()

    def reset_search(self):
        sql = "SELECT * FROM movies ORDER BY id ASC"
        cursor = self.connection.cursor()
        datos = cursor.execute(sql)
        resultados = datos.fetchall()
        return resultados
