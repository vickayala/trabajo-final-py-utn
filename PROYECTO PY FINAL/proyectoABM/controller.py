from tkinter import *
from view import View
from model import Model
from decorador import *
from observador import Observador


class Controller:
    def __init__(self, root):
        self.root = root
        self.view = View(root, self)
        self.model = Model()

        # Make a first Print of the table
        firstPrint = self.model.reset_search()
        self.actualizar_treeview(firstPrint)

    @decoradorCreate
    def create(self):
        resultados = self.model.create(
            self.view.title.get(),
            self.view.description.get(),
            self.view.genre.get(),
            self.view.language.get(),
            self.view.lenght.get(),
        )
        self.actualizar_treeview(
            resultados,
        )
        self.observador = Observador.observadorGenre(self, self.view.genre.get())

    @decoradorDelete
    def delete(self):
        valor = self.view.tree.selection()
        item = self.view.tree.item(valor)
        id = item["text"]
        self.model.delete(id)
        self.view.tree.delete(valor)

    @decoradorSearch
    def search(self):
        resultados = self.model.search(self.view.title.get(), self.view.genre.get())
        self.actualizar_treeview(resultados)

    def actualizar_treeview(self, resultados):
        records = self.view.tree.get_children()
        for element in records:
            self.view.tree.delete(element)

        for fila in resultados:
            print(fila)
            self.view.tree.insert(
                "",
                0,
                text=fila[0],
                values=(fila[1], fila[2], fila[3], fila[4], fila[5]),
            )


if __name__ == "__main__":
    root = Tk()
    Controller(root)
    root.mainloop()
