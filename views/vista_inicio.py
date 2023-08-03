# Views inicio

import tkinter as tk
from tkinter.font import Font


class VistaInicio(tk.Frame):
    def __init__(self, master=None, controlador=None):
        """
        Crea la vista de inicio.
        """
        super().__init__(master)
        self.master = master
        self.controlador = controlador

        # Define una fuente grande y en negrita para el título
        #titulo_font = Font(size=24, weight="bold")
        titulo_font = Font(family="Open Sans", size=18, weight="bold")

        # Crea una etiqueta para el título y la agrega a la vista
        
        self.titulo = tk.Label(self, text="Dr. Monkey Event's", font=titulo_font)
        self.titulo.grid(row=0, column=0, pady=10)

        # Define una fuente más pequeña para la descripción de la funcionalidad
        descripcion_font = Font(family="Open Sans", size=12, weight="bold")

        # Crea una etiqueta para la descripción de la funcionalidad y la agrega a la vista
        self.descripcion = tk.Label(
            self,
            text="Aquí puedes buscar y seleccionar todos los Eventos Musicales de temporada, con toda la información necesaria para que puedas asistir!",
            font=descripcion_font,
            # wraplength=300,
            wraplength=900
        )
        # self.descripcion.grid(row=1, column=0, pady=50)
        self.descripcion.grid(row=1, column=0, padx=40, pady=10)

        
        # Crea el botón para ir a Eventos y lo agrega a la vista
        
        self.boton_eventos = tk.Button(
            self, text="Indice de Eventos", command=self.controlador.mostrar_eventos
        )
        # self.boton_eventos.grid(row=2, column=0, pady=10)
        self.boton_eventos.grid(row=3, column=0, padx=10, pady=10)

        # Crea el botón para ir a Historial de Eventos asistidos y lo agrega a la vista

        self.boton_busqueda_e = tk.Button(
            self, text="Historial de Eventos", command=self.controlador.mostrar_historial
        )
        # self.boton_busqueda_e.grid(row=2, column=1, pady=10)
        self.boton_busqueda_e.grid(row=5, column=0, padx=10, pady=10)

        # Crea el botón para ir a Busqueda y filtrado de Eventos y lo agrega a la vista
        
        self.boton_historial = tk.Button(
            self, text="Busqueda y filtrado", command=self.controlador.mostrar_busqueda
        )
        # self.boton_historial.grid(row=2, column=2, pady=10)
        self.boton_historial.grid(row=7, column=0, padx=10, pady=10)
