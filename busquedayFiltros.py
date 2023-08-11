import tkinter as tk
import json

# Define resultados como una lista vacía al inicio del programa
resultados = []

def buscar_eventos():
    global resultados
    criterio = entrada_busqueda.get().lower()
    resultados.clear()

    with open('data/evento.json', 'r') as archivo:
        eventos = json.load(archivo)
        for evento in eventos:
            if (criterio in evento['nombre'].lower() or
                criterio in evento['genero'].lower() or
                criterio in evento['artista'].lower()):
                resultados.append(evento)

    mostrar_resultados(resultados)

def filtrar_por_ubicacion_horario():
    global resultados
    criterio = entrada_filtro.get().lower()
    resultados.clear()

    with open('data/evento.json', 'r') as archivo:
        eventos = json.load(archivo)
        with open('data/ubicacion.json', 'r') as ubicacion_archivo:
            ubicaciones = json.load(ubicacion_archivo)
            for evento in eventos:
                ubicacion = next((u for u in ubicaciones if u['id_ubicacion'] == evento['id_ubicacion']), None)
                if ubicacion and (criterio in ubicacion['nombre'].lower() or criterio in evento['hora_inicio'].lower() or criterio in evento['hora_fin'].lower()):
                    resultados.append(evento)

    mostrar_resultados(resultados)

def mostrar_resultados(resultados):
    lista_resultados.delete(0, tk.END)
    for evento in resultados:
        evento_details = f"Nombre: {evento['nombre']}\n Género: {evento['genero']}\n Artista: {evento['artista']}"
        lista_resultados.insert(tk.END, evento_details)

def mostrar_detalles(evento_seleccionado):
    indice_seleccionado = lista_resultados.curselection()[0]  # Obtiene el índice seleccionado
    evento = resultados[indice_seleccionado]  # Obtiene el evento correspondiente

    evento_details = f"Nombre: {evento['nombre']}\n Género: {evento['genero']}\n Artista: {evento['artista']}"

    reviews = reviews_data.get(str(evento['id_evento']), [])
    if reviews:
        evento_details += "\n\nReseñas:\n"
        for review in reviews:
            evento_details += f"Calificación: {review['calificacion']} - Comentario: {review['comentario']} - Animo: {review['animo']}\n"

    lista_resultados.delete(0, tk.END)
    lista_resultados.insert(tk.END, evento_details)



ventana = tk.Tk()
ventana.title("Búsqueda y Filtrado de Eventos")
ventana.geometry("960x540")

# Color de fondo
ventana.configure(bg="LightYellow")

marco_busqueda = tk.Frame(ventana, borderwidth=2, relief="ridge", padx=10, pady=10)
marco_busqueda.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
marco_busqueda.configure(bg="LightYellow")

etiqueta_busqueda = tk.Label(marco_busqueda, text="Buscar Evento por Nombre, Género y Artista:")
etiqueta_busqueda.pack()

entrada_busqueda = tk.Entry(marco_busqueda)
entrada_busqueda.pack()

boton_buscar = tk.Button(marco_busqueda, text="Buscar", command=buscar_eventos)
boton_buscar.pack()

marco_filtro = tk.Frame(ventana, borderwidth=2, relief="ridge", padx=10, pady=10)
marco_filtro.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
marco_filtro.configure(bg="LightYellow")

etiqueta_filtro = tk.Label(marco_filtro, text="Filtrar por Ubicación u Horario:")
etiqueta_filtro.pack()

entrada_filtro = tk.Entry(marco_filtro)
entrada_filtro.pack()

boton_filtrar = tk.Button(marco_filtro, text="Filtrar", command=filtrar_por_ubicacion_horario)
boton_filtrar.pack()

marco_resultados = tk.Frame(ventana, borderwidth=2, relief="ridge", padx=10, pady=10)
marco_resultados.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
marco_resultados.configure(bg="LightYellow")

lista_resultados = tk.Listbox(marco_resultados)
lista_resultados.pack(fill=tk.BOTH, expand=True)

# Load reviews data from 'data/review.json'
reviews_data = {}
with open('data/review.json', 'r') as review_archivo:
    reviews_data = json.load(review_archivo)

# Bind the function to show details when an event is selected
lista_resultados.bind('<<ListboxSelect>>', lambda event: mostrar_detalles(lista_resultados.get(lista_resultados.curselection()[0])))

ventana.mainloop()