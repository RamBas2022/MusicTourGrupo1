# Archivo Principal, inicial
from tkinter import *
import tkinter as tk
from tkinter import ttk
import json

# MODELS
# Importamos models: Evento, Review, RutaVisita, Ubicacion, Usuario
from models.evento import Evento
from models.review import Review
from models.ruta_visita import RutaVisita
from models.ubicacion import Ubicacion
from models.usuario import Usuario

# VIEWS
# Vista inicial de la aplicacion
from views.vista_inicio import VistaInicio

# Importamos vista_eventos, historial y busqueda
from views.vista_eventos import VistaEventos
from views.vista_historial import VistaHistorial
from views.vista_busqueda import VistaBusqueda

# Vista detallada del evento
from views.vista_info import VistaInfo

#CONTROLLERS
# Importamos Controlador de los Frames de Evento, Historial y Busqueda
from controllers.controlador_inicio import ControladorInicio

# Importamos controlador de eventos, historial y busqueda
from controllers.controlador_eventos import ControladorEventos
from controllers.controlador_historial import ControladorHistorial
from controllers.controlador_busqueda import ControladorBusqueda

from controllers.controlador_info import ControladorInfo

import recibeUsuario


# Imagen presentacion
root = Tk()
root.title("Dr.Monkey, el especialista en eventos!!!")
# Ajustar tamaño    
root.geometry("960x640")
root.resizable(False, False)
root.configure(bg = 'LightYellow')

# Agrega imagen
bg = tk.PhotoImage(file = "assets/monkey.png")
# Crea Canvas
canvas1 = Canvas(root, width = 960, height = 540)
canvas1.pack(fill = "both", expand = True)
# Mostrar imagen
canvas1.create_image( 0, 0, image = bg, anchor = "nw")

# Verificamos si el usuario esta registrado
def print_value():
    value = var.get()
    print(f"El valor inicial es: {value}")
    # Tenemos 4 usuarios registrados. 
    if (verificar_usuario(value)):
        print(f"El valor es: {value}")
        
        label_status.config(text="Inicio de sesión exitoso!", fg="green")
        root.destroy() # Para continuar en la Aplicacion principal
        #root.withdraw()
    else:
        label_status.config(text="Numero de usuario no registrado!", fg="red")
        print(f"El usuario no esta registrado")    

def verificar_usuario(value): # Abrimos archivo usuario.json
    indice = 0
    with open("data/usuario.json", "r") as f:
            data_u = json.load(f)
            print(data_u)
            dato = len(data_u)
            print(value)
            
    for data in data_u:
        dicc = data_u[indice]
        print (dicc) 
        indice = indice + 1

        # Verificamos si el usuario esta en algun diccionario
        if value == dicc["id_usuario"]:
            value1 = dicc["id_usuario"]
            value2 = dicc["nombre"]
            value3 = dicc["apellido"]
            value4 = dicc["historial_eventos"]
            recibeUsuario.user(value1, value2, value3, value4)
            label_status.config(text="Inicio de sesión exitoso!", fg="green")
            return True

frame = tk.Frame(root)
frame.pack(fill=tk.BOTH, expand=True)

# Entry para el numero de usuario
var = tk.IntVar()
entry = tk.Entry(frame, textvariable=var)
entry.pack()

button = tk.Button(frame, text="Ingrese su nùmero de usuario: 1,2,3", command=print_value)
button.pack()

# Etiqueta de estado
label_status = tk.Label(frame, text="")
label_status.pack()

# Boton Quit, para salir
ttk.Button(root, text='Salir de la App', command=quit).pack(side=BOTTOM)

# Ciclo de eventos
root.mainloop()


# Aplicacion principal
# ====================

class Aplicacion(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title("Dr.Monkey Event's")
        self.geometry("960x540")
        self.resizable(False, False)
        self.inicializar()
        self.cambiar_frame(self.vista_inicio)
        
    def inicializar(self):
       
        eventos = Evento.cargar_evento_json("data/evento.json")
        usuarios = Usuario.cargar_usuario_json("data/usuario.json")
        reviews = Review.cargar_review_json("data/review.json")
        ubicaciones = Ubicacion.cargar_ubicacion_json("data/ubicacion.json")
        rutas = RutaVisita.cargar_ruta_json("data/ruta_visita.json")

        print(eventos)
        print(usuarios)
        print(reviews)
        print(ubicaciones)
        print(rutas)

        print("Recibido usuario")
        print(recibeUsuario.user)
        user1 = recibeUsuario.user
        print(user1)

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
        self.ajustar_frame(self.vista_info)
   

    def ajustar_frame(self, frame):
        frame.grid(row=0, column=0, sticky="nsew")
        frame.config(bg="LightYellow")

    def cambiar_frame(self, frame_destino):
        frame_destino.tkraise()
        frame_destino.config(bg="LightYellow")

if __name__ == "__main__":
    app = Aplicacion()
    app.mainloop()
