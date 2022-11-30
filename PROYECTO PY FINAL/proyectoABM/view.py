from tkinter import *
from tkinter.messagebox import *
from tkinter import ttk
from tkinter.tix import Tree


class View:
    def __init__(self, root, controller):
        self.root = root

        self.main_title = Label(
            self.root, text="MOVIES", bg="#FFA5E6", fg="white", height=2, width=50
        )
        self.main_title.grid(
            row=0, column=0, columnspan=6, padx=1, pady=1, sticky=W + E
        )

        self.title_label = Label(self.root, text="Title")
        self.title_label.grid(row=1, column=0, sticky=W + E)

        self.description_label = Label(self.root, text="Description")
        self.description_label.grid(row=2, column=0, sticky=W + E)

        self.genre_label = Label(self.root, text="Genre")
        self.genre_label.grid(row=3, column=0, sticky=W + E)

        self.language_label = Label(self.root, text="Language")
        self.language_label.grid(row=4, column=0, sticky=W + E)

        self.length = Label(self.root, text="Length")
        self.length.grid(row=5, column=0, sticky=W + E)

        self.title = StringVar()
        self.description = StringVar()
        self.genre = StringVar()
        self.language = StringVar()
        self.lenght = IntVar()

        self.entry_title = Entry(self.root, textvariable=self.title)
        self.entry_title.grid(row=1, column=1, sticky=W + E)
        self.entry_description = Entry(self.root, textvariable=self.description)
        self.entry_description.grid(row=2, column=1, sticky=W + E)

        self.entry_genre = Entry(self.root, textvariable=self.genre)
        self.entry_genre.grid(row=3, column=1, sticky=W + E)

        self.entry_language = Entry(self.root, textvariable=self.language)
        self.entry_language.grid(row=4, column=1, sticky=W + E)

        self.entry_length = Entry(self.root, textvariable=self.lenght)
        self.entry_length.grid(row=5, column=1, sticky=W + E)

        ### Boton de crear ###
        self.boton_create = Button(
            self.root,
            text="CREATE",
            bg="#DF69BF",
            fg="white",
            command=lambda: controller.create(),
        )
        self.boton_create.grid(row=6, column=1, sticky=W + E, pady=20)

        ### Boton de borrar ###
        self.boton_delete = Button(
            self.root,
            text="DELETE",
            bg="#DF69BF",
            fg="white",
            command=lambda: controller.delete(),
        )
        self.boton_delete.grid(row=4, column=2, sticky=E)

        ### Boton de crear ###
        self.boton_search = Button(
            self.root,
            text="SEARCH",
            bg="#DF69BF",
            fg="white",
            command=lambda: controller.search(),
        )
        self.boton_search.grid(row=2, column=2, sticky=E)

        self.tree = ttk.Treeview(self.root)

        self.tree["columns"] = ("col1", "col2", "col3", "col4", "col5")
        self.tree.column("#0", width=90, minwidth=50, anchor=W)
        self.tree.column("col1", width=200, minwidth=80)
        self.tree.column("col2", width=200, minwidth=80)
        self.tree.column("col3", width=200, minwidth=80)
        self.tree.column("col4", width=200, minwidth=80)

        self.tree.heading("#0", text="ID")
        self.tree.heading("col1", text="Title")
        self.tree.heading("col2", text="Description")
        self.tree.heading("col3", text="Genre")
        self.tree.heading("col4", text="Language")
        self.tree.heading("col5", text="Legth")

        self.tree.grid(row=10, column=0, columnspan=4)
