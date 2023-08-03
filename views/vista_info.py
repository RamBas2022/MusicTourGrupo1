# Views info

import tkinter as tk


class VistaInfo(tk.Frame):
    def __init__(self, master=None, controlador=None):
        """
        Crea la vista de la información de un evento.
        """
        super().__init__(master)
        self.master = master
        self.controlador = controlador
        #evento_font = Font(family="Open Sans", size=10, weight="bold")
        self.evento_label = tk.Label(self, text="Detalle del evento seleccionado:")
        
        self.evento_label.pack(pady=50)
        
        self.evento_label.config(justify=tk.LEFT)
        self.boton_regresar = tk.Button(
            self,
            text="Regresar al Indice de Eventos",
            command=self.controlador.regresar_eventos,
        )
        self.boton_regresar.pack(pady=10)
    

    def mostrar_info_evento(self, evento):
        """
        Muestra la información del Evento recibido como parámetro.
        """
        info = f"Título: {evento.nombre}\nArtista: {evento.artista}\nGenero: {evento.genero}\nFecha,Hra.Inicio: {evento.hora_inicio}\nFecha,Hra.Fin: {evento.hora_fin}"
        self.evento_label["text"] = info