#Mapa y planificador de rutas
import tkinter as tk
from tkinter import ttk
from tkintermapview import mapa
import customtkinter as ctk
import tkintermapview as tk

ctk.set_appearance_mode("dark")

class VistaMapa (ctk.CtkFrame):
    def __init__(self, master=None, controlador=None):
        tk.Tk.__init__(self)
        self.title("Mapa")
        super().__init__(master)
        self.master.controlador = controlador
        self.ubicaciones = []

        #"ventana mapa"
        self.mapa = mapa.TkinterMapView(self, width=800, height=600, corner_radius=15)
        self.mapa.pack(pady=10, padx=10)
        self.mapa.set_position(-24.7859, -65.41166, marker=True) #Salta, Argentina
        self.mapa.set_zoom(15)

    
        #boton
        ubicaciones = ctk.CTkButton(
            self,

            text="Visualizar Ubicación",
            corner_radius=15)


        add = ctk.CTkButton(
            self,
            text="Agregar Ubicación",
            corner_radius=15)

    #planificar rutas
    def planificar_ruta(self):
        tu_ubicacion = tu_ubicacion.get()
        ubicacion_evento = ubicacion_evento.get()

        add = ctk.CTkButton(
            self,

            text="Planificar ruta",
            corner_radius=10)
        
        mapa.clear_layers()
        mapa.plan_route(tu_ubicacion, ubicacion_evento)
        mapa.show_routes()
        

    def crear_mapa (self):
        evento_seleccionado = self.controlador.ubicación_seleccionada
        self.mapa.set_position(evento_seleccionado.latitud, evento_seleccionado.longitud)
        self.mapa.set_marker(evento_seleccionado.latitud, evento_seleccionado.longitud)


    def Agregar_marcador_de_evento (cords, self):
      lista = []
      nombre_evento = input ("Nombre del evento: ")
      click = self.mapa.set_marker (cords[1], cords[2], text=nombre_evento)
      dirección = (cords[1], cords[2])
      lista.append ((nombre_evento, dirección, cords[1], cords[2]))
      mensaje = tk.messagebox.eventoinfo ("Eventos", f" '{nombre_evento}' ha sido agregado")

      self.ubicaciones = self.mapa.add_left_click_map_command()  

      return lista

if __name__=="__main__":
    app = VistaMapa()
    app.mainloop()
    



   



