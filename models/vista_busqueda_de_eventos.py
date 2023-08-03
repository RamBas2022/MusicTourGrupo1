import tkinter as tk

class EventSearchView(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.create_widgets()

    def create_widgets(self):
        # Crear etiqueta de búsqueda y entrada
        self.search_label1 = tk.Label(self, text="Buscar por Nombre:")
        self.search_label1.pack(side=tk.LEFT)
        self.search_entry1 = tk.Entry(self)
        self.search_entry1.pack(side=tk.LEFT)

        # Crear botón buscar
        self.search_button = tk.Button(self, text="Buscar", command=self.search_events)
        self.search_button.pack(side=tk.LEFT)

        self.search_label2 = tk.Label(self, text="Buscar por Género:")
        self.search_label2.pack(side=tk.LEFT)
        self.search_entry2 = tk.Entry(self)
        self.search_entry2.pack(side=tk.LEFT)

        # Crear botón buscar
        self.search_button = tk.Button(self, text="Buscar", command=self.search_events)
        self.search_button.pack(side=tk.LEFT)

        self.search_label3 = tk.Label(self, text="Buscar por Artista:")
        self.search_label3.pack(side=tk.LEFT)
        self.search_entry3 = tk.Entry(self)
        self.search_entry3.pack(side=tk.LEFT)

        # Crear botón buscar
        self.search_button = tk.Button(self, text="Buscar", command=self.search_events)
        self.search_button.pack(side=tk.LEFT)

        # Crear etiqueta de filtrado y entrada
        self.filter_label1 = tk.Label(self, text="Filtrado por Ubicación:")
        self.filter_label1.pack(side=tk.LEFT)
        self.filter_entry1 = tk.Entry(self)
        self.filter_entry1.pack(side=tk.LEFT)

        # Crear botón filtrar
        self.filter_button = tk.Button(self, text="Filtrar", command=self.filter_events)
        self.filter_button.pack(side=tk.LEFT)

        self.filter_label2 = tk.Label(self, text="Filtrado por Horario:")
        self.filter_label2.pack(side=tk.LEFT)
        self.filter_entry2 = tk.Entry(self)
        self.filter_entry2.pack(side=tk.LEFT)

        # Crear botón filtrar
        self.filter_button = tk.Button(self, text="Filtrar", command=self.filter_events)
        self.filter_button.pack(side=tk.LEFT)

    def search_events(self):
        search_text1 = self.search_entry1.get()
        search_text2 = self.search_entry2.get()
        search_text3 = self.search_entry3.get()

        # Realizar la lógica de búsqueda aquí

        # Borrar los campos de entrada de búsqueda
        self.search_entry1.delete(0, tk.END)
        self.search_entry2.delete(0, tk.END)
        self.search_entry3.delete(0, tk.END)

        # Actualizar la lista de eventos con los resultados de la búsqueda

    def filter_events(self):
        filter_text1 = self.filter_entry1.get()
        filter_text2 = self.filter_entry2.get()

        # Realizar la lógica de filtrado aquí

        # Borrar los campos de entrada de filtrado
        self.filter_entry1.delete(0, tk.END)
        self.filter_entry2.delete(0, tk.END)

        # Actualizar la lista de eventos con los resultados del filtrado


# Crear la ventana principal de la aplicación
root = tk.Tk()

# Crear la instancia de EventSearchView y empaquetarla en la ventana raíz
event_search_view = EventSearchView(root)
event_search_view.pack()

# Iniciar el ciclo de eventos de Tkinter
root.mainloop()