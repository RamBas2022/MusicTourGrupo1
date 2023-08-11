import tkinter as tk
import json

def cargar_datos():
    with open('data/evento.json', 'r') as archivo:
        eventos = json.load(archivo)
    with open('data/ubicacion.json', 'r') as ubicacion_archivo:
        ubicaciones = {u['id_ubicacion']: u for u in json.load(ubicacion_archivo)}
    return eventos, ubicaciones

def buscar_eventos():
    global resultados, marco_resultados
    criterio = entrada_busqueda.get().lower()
    resultados = [evento for evento in eventos if
                  criterio in evento['nombre'].lower() or
                  criterio in evento['genero'].lower() or
                  criterio in evento['artista'].lower()]
    mostrar_resultados()

def filtrar_por_ubicacion_horario():
    global resultados, marco_resultados
    criterio = entrada_filtro.get().lower()
    resultados = [evento for evento in eventos if
                  criterio in ubicaciones.get(evento['id_ubicacion'], {}).get('nombre', '').lower() or
                  criterio in evento['hora_inicio'].lower() or
                  criterio in evento['hora_fin'].lower()]
    mostrar_resultados()

def mostrar_resultados():
    lista_resultados.delete(0, tk.END)
    for evento in resultados:
        evento_details = f"Nombre: {evento['nombre']}\nGénero: {evento['genero']}\nArtista: {evento['artista']}"
        lista_resultados.insert(tk.END, evento_details)

def mostrar_detalles(evento_seleccionado):
    if not evento_seleccionado:
        return
    
    indice_seleccionado = lista_resultados.curselection()[0]
    evento = resultados[indice_seleccionado]

    evento_details = f"Nombre: {evento['nombre']}\nGénero: {evento['genero']}\nArtista: {evento['artista']}"

    reviews = reviews_data.get(str(evento['id_evento']), [])
    if reviews:
        evento_details += "\n\nReseñas:\n"
        for review in reviews:
            evento_details += f"Calificación: {review['calificacion']} - Comentario: {review['Comentario']} - Animo: {review['animo']}\n"

    lista_resultados.delete(0, tk.END)
    lista_resultados.insert(tk.END, evento_details)

#Ventana principal
ventana = tk.Tk()
ventana.title("Búsqueda y Filtrado de Eventos")
ventana.geometry("960x540")
ventana.configure(bg="#E5E5E5")

eventos, ubicaciones = cargar_datos()

marco_busqueda = tk.Frame(ventana, borderwidth=2, relief="ridge", padx=10, pady=10, bg="#A1A892")
marco_busqueda.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

etiqueta_busqueda = tk.Label(marco_busqueda, text="Buscar por Nombre, Género y Artista:", font=("Open Sans", 12), bg="#A1A892")
etiqueta_busqueda.pack()

entrada_busqueda = tk.Entry(marco_busqueda, font=("Open Sans", 12))
entrada_busqueda.pack()

boton_buscar = tk.Button(marco_busqueda, text="Buscar", command=buscar_eventos, font=("Open Sans", 12))
boton_buscar.pack()

marco_filtro = tk.Frame(ventana, borderwidth=2, relief="ridge", padx=10, pady=10, bg="#A1A892")
marco_filtro.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

etiqueta_filtro = tk.Label(marco_filtro, text="Filtro por Ubicación o Horario:", font=("Open Sans", 12), bg="#A1A892")
etiqueta_filtro.pack()

entrada_filtro = tk.Entry(marco_filtro, font=("Open Sans", 12))
entrada_filtro.pack()

boton_filtrar = tk.Button(marco_filtro, text="Filtrar", command=filtrar_por_ubicacion_horario, font=("Open Sans", 12))
boton_filtrar.pack()

marco_resultados = tk.Frame(ventana, borderwidth=2, relief="ridge", padx=10, pady=10, bg="#A1A892")
marco_resultados.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

lista_resultados = tk.Listbox(marco_resultados, font=("Open Sans", 12))
lista_resultados.pack(fill=tk.BOTH, expand=True)

reviews_data = {}
with open('data/review.json', 'r') as review_archivo:
    reviews_list = json.load(review_archivo)
    for review in reviews_list:
        id_evento = str(review['id_evento'])
        if id_evento not in reviews_data:
            reviews_data[id_evento] = []
        reviews_data[id_evento].append(review)

lista_resultados.bind('<<ListboxSelect>>', lambda event: mostrar_detalles(lista_resultados.get(lista_resultados.curselection()[0])))

ventana.mainloop()
