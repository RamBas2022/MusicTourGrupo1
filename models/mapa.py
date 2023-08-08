#Mapa y planificador de rutas

import tkinter
from tkintermapview 
from TkinterMapView
import tkintermapview as mapa
import customtkinter as ctk

self = tkinter.Tk()
ctk.set_appearance_mode("dark")

class VistaMapa (ctk.CtkFrame):
    def __int__(self, master=None, controlador=None):
        super().__int__(master)
        self.master.controlador = controlador
        self.ubicaciones = []

        #ventana mapa
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

    def crear_mapa (self):
        evento_seleccionado = self.controlador.ubicación_seleccionada
        self.mapa.set_position(evento_seleccionado.latitud, evento_seleccionado.longitud)
        self.mapa.set_marekr(evento_seleccionado.latitud, evento_seleccionado.longitud)



    def Agregar_marcador_de_evento (cords):

      lista = []
      nombre = input ("Nombre del evento: ")
      click = self.mapa.set_marker (cords[1], cords[2], text = nombre_evento)
      dirección = (cords[1], cords[2])
      lista.append ((nombre_evento, dirección, cords[1], cords[2]))
      mensaje = tk.messagebox.eventoinfo ("Evento", f" '{nombre_evento}' ha sido agregado")

      return lista


    self.ubicaciones = self.mapa.add_left_click_map_command(Agregar_marcador_de_evento)         



