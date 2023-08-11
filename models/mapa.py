#Mapa y planificador de rutas

import tkinter as tk
import json
from tkintermapview import TkinterMapView

# Leer los datos de eventos del archivo JSON
with open('data/evento.json', 'r') as json_file:
    eventos = json.load(json_file)

# Leer los datos de ubicaciones del archivo JSON
with open('data/ubicacion.json', 'r') as json_file:
    ubicaciones = json.load(json_file)

def obtener_ubicacion_por_id(id_ubicacion):
    ubicacion = next((ubicacion for ubicacion in ubicaciones if ubicacion['id_ubicacion'] == id_ubicacion), None)
    return ubicacion

def mostrar_ubicacion_seleccionada():
    seleccion = evento_listbox.curselection()
    if seleccion:
        index_seleccionado = seleccion[0]
        evento_seleccionado = eventos[index_seleccionado]

        id_ubicacion = evento_seleccionado['id_ubicacion']
        ubicacion = obtener_ubicacion_por_id(id_ubicacion)

        if ubicacion:
            nombre_evento = evento_seleccionado['nombre']
            nombre_ubicacion = ubicacion['nombre']
            nombre_artista = evento_seleccionado['artista']

            # Obtén las coordenadas y dirección directamente del archivo JSON
            coordenadas = ubicacion['coordenadas']
            latitud, longitud = coordenadas
            direccion = ubicacion.get('direccion', '')

            ubicacion_label.config(text=f"Evento: {nombre_evento}\nArtista: {nombre_artista}\nUbicación: {nombre_ubicacion}\nDirección: {direccion}")

            map_view.removemarker()
            marker_popup = f"Artista: {nombre_artista}\nUbicación: {nombre_ubicacion}\nDirección: {direccion}"
            map_view.add_marker(latitud, longitud, title=nombre_evento, popup_text=marker_popup)
            map_view.set_center(latitud, longitud)

def planificar_ruta():
    seleccion = evento_listbox.curselection()
    if len(seleccion) >= 2:
        ubicaciones_seleccionadas = [obtener_ubicacion_por_id(eventos[index]['id_ubicacion']) for index in seleccion]
        coordenadas_seleccionadas = [(ubicacion['coordenadas'][0], ubicacion['coordenadas'][1]) for ubicacion in ubicaciones_seleccionadas if ubicacion is not None]

        map_view.removemarker()
        for coordenada, evento in zip(coordenadas_seleccionadas, eventos):
            latitud, longitud = coordenada
            nombre_evento = evento['nombre']
            nombre_artista = evento['artista']
            map_view.add_marker(latitud, longitud, title=nombre_evento, popup_text=f"Artista: {nombre_artista}")
        map_view.draw_route(coordenadas_seleccionadas)

# Crear la ventana principal
root = tk.Tk()
root.title("Mapa y planificador de rutas")
root.geometry("960x720")  # Ajustar la altura para que todos los elementos encajen cómodamente

# Configuracion de colores
bg_color = "#A1A892"  # Color de fondo general
button_color = "#E6D884"  # Color de fondo del botón
button_text_color = "white"  # Color del texto del botón

root.configure(bg=bg_color)  # Establecer el color de fondo general

# Crear un listbox con scrollbar para mostrar la lista de eventos
evento_frame = tk.Frame(root, bg=bg_color)
evento_frame.pack(padx=20, pady=20, side=tk.LEFT, fill=tk.BOTH)

evento_scrollbar = tk.Scrollbar(evento_frame)
evento_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

evento_listbox = tk.Listbox(evento_frame, selectmode=tk.MULTIPLE, width=40, height=10, yscrollcommand=evento_scrollbar.set)
for evento in eventos:
    evento_listbox.insert(tk.END, evento['nombre'])
evento_listbox.pack(side=tk.LEFT, fill=tk.BOTH)
evento_scrollbar.config(command=evento_listbox.yview)

# Crear el marco para la informacion de ubicacion seleccionada
ubicacion_frame = tk.Frame(root, bg=bg_color)
ubicacion_frame.pack(padx=20, pady=20, side=tk.LEFT, fill=tk.BOTH)

ubicacion_label = tk.Label(ubicacion_frame, text="", padx=10, pady=10, bg="white", borderwidth=2, relief="solid")
ubicacion_label.pack(fill=tk.BOTH)

# Estilos para botones
button_style = {"background": button_color, "foreground": button_text_color}

# Boton para visualizar la ubicación
visualizar_button = tk.Button(root, text="Visualizar Ubicación", command=mostrar_ubicacion_seleccionada, **button_style)
visualizar_button.pack(pady=10, fill=tk.BOTH)

# Boton para planificar ruta
planificar_ruta_button = tk.Button(root, text="Planificar Ruta", command=planificar_ruta, **button_style)
planificar_ruta_button.pack(pady=10, fill=tk.BOTH)

# Crear el mapa en un marco separado
map_frame = tk.Frame(root, bg=bg_color)
map_frame.pack(padx=20, pady=20, side=tk.LEFT, fill=tk.BOTH, expand=True)

map_view = TkinterMapView(map_frame)
map_view.pack(fill=tk.BOTH, expand=True)

# Iniciar el bucle principal de la aplicacion
root.mainloop()

    



   



