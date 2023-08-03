# Archivo Principal, inicial
from tkinter import *
import tkinter as tk

# Agregamos models: Evento, Review, RutaVisita, Ubicacion, Usuario
from models.evento import Evento
from models.review import Review
from models.ruta_visita import RutaVisita
from models.ubicacion import Ubicacion
from models.usuario import Usuario

from views.vista_inicio import VistaInicio

# Agregamos vista_eventos, historial y busqueda
from views.vista_eventos import VistaEventos
from views.vista_historial import VistaHistorial
from views.vista_busqueda import VistaBusqueda


from views.vista_info import VistaInfo
from controllers.controlador_inicio import ControladorInicio

# Agregamos controlador de eventos, historial y busqueda
from controllers.controlador_eventos import ControladorEventos
from controllers.controlador_historial import ControladorHistorial
from controllers.controlador_busqueda import ControladorBusqueda

from controllers.controlador_info import ControladorInfo

# Insercion provisoria de imagen. Ver con el Profe.
root = Tk()
# Ajustar tamaño   
root.geometry("960x540")
# Agrega imagen
bg = tk.PhotoImage(file = "assets/monkey.png")
# Crea Canvas
canvas1 = Canvas( root, width = 960, height = 540)
canvas1.pack(fill = "both", expand = True)
# Mostrar imagen
canvas1.create_image( 0, 0, image = bg, anchor = "nw")

class Aplicacion(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title("Dr.Monkey Event's")
        # self.geometry("330x300")
        self.geometry("960x540")
        self.resizable(False, False)
        self.inicializar()
        self.cambiar_frame(self.vista_inicio)


    def inicializar(self):
       
        eventos = Evento.cargar_evento_json("data/evento.json")
        print(eventos)
        controlador_inicio = ControladorInicio(self)
        
        # controladores de Eventos, Historial y Busqueda
        controlador_eventos = ControladorEventos(self, eventos)
        controlador_historial = ControladorHistorial(self, eventos)
        controlador_busqueda = ControladorBusqueda(self, eventos)

        controlador_info = ControladorInfo(self)

        self.vista_inicio = VistaInicio(self, controlador_inicio)
        
        # vista de eventos, historial y busqueda
        self.vista_eventos = VistaEventos(self, controlador_eventos)
        self.vista_historial = VistaHistorial(self, controlador_historial)
        self.vista_busqueda = VistaBusqueda(self, controlador_busqueda)

        self.vista_info = VistaInfo(self, controlador_info)

        self.ajustar_frame(self.vista_inicio)
        # vistas evento, hitorial y busqueda
        self.ajustar_frame(self.vista_eventos)
        self.ajustar_frame(self.vista_historial)
        self.ajustar_frame(self.vista_busqueda)
        self.ajustar_frame(self.vista_eventos)
        self.ajustar_frame(self.vista_info)
   

    def ajustar_frame(self, frame):
        frame.grid(row=0, column=0, sticky="nsew")

    def cambiar_frame(self, frame_destino):
        frame_destino.tkraise()


if __name__ == "__main__":
    app = Aplicacion()
    app.mainloop()
