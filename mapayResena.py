import tkinter as tk
from tkinter import simpledialog, messagebox
import json

# Initialize the JSON file with empty data structure
initial_data = {
    "reviews": [],
    "animo": []
}

with open("data/review.json", "w") as file:
    json.dump(initial_data, file, indent=4)

# Funcion para guardar el animo en el archivo "data/review.json"
def guardar_animo(animo_data):
    with open("data/review.json", "r") as file:
        reviews_data = json.load(file)

    reviews_data["animo"].append(animo_data)

    with open("data/review.json", "w") as file:
        json.dump(reviews_data, file, indent=4)

# Funcion para guardar una reseña en el archivo "data/review.json"
def guardar_review(review):
    with open("data/review.json", "r") as file:
        reviews_data = json.load(file)

    reviews_data["reviews"].append(review)

    with open("data/review.json", "w") as file:
        json.dump(reviews_data, file, indent=4)

# Funcion para mostrar la ventana de señalar animo
def mostrar_ventana_animo(id_evento, id_usuario):
    ventana_animo = tk.Toplevel(root)
    ventana_animo.title("Señalar ánimo")

    animo_seleccionado = tk.StringVar(ventana_animo)
    animo_seleccionado.set("Positivo")  # Opción predeterminada

    label_animo = tk.Label(ventana_animo, text="Seleccione el ánimo de la review:")
    label_animo.pack()

    opciones_animo = ["Positivo", "Negativo"]
    for opcion in opciones_animo:
        radiobutton = tk.Radiobutton(ventana_animo, text=opcion, variable=animo_seleccionado, value=opcion)
        radiobutton.pack(anchor=tk.W)

    def guardar_animo_seleccionado():
        animo = animo_seleccionado.get()
        guardar_animo({"animo": animo, "id_evento": id_evento, "id_usuario": id_usuario})
        messagebox.showinfo("Señalar ánimo de la review", f"Ánimo '{animo}' guardado exitosamente.")
        ventana_animo.destroy()

    boton_guardar_animo = tk.Button(ventana_animo, text="Guardar Ánimo", command=guardar_animo_seleccionado)
    boton_guardar_animo.pack(pady=10)

    # Retornar el animo seleccionado para que pueda ser capturado en la funcion de guardar_review_comentario()
    return animo_seleccionado

# Funcion para mostrar la ventana de escribir reseña
def mostrar_ventana_escribir_review(id_evento, id_usuario):
    ventana_escribir_review = tk.Toplevel(root)
    ventana_escribir_review.title("Escribir Review")

    label_evento = tk.Label(ventana_escribir_review, text=f"Nro. de Evento: {id_evento}")
    label_evento.pack()

    label_usuario = tk.Label(ventana_escribir_review, text=f"Nro. de Usuario: {id_usuario}")
    label_usuario.pack()

    comentario_label = tk.Label(ventana_escribir_review, text="Escriba su reseña:")
    comentario_label.pack()

    comentario_text = tk.Text(ventana_escribir_review, height=5, width=40)
    comentario_text.pack()

    calificacion_label = tk.Label(ventana_escribir_review, text="Seleccione una calificación:")
    calificacion_label.pack()

    calificacion_seleccionada = tk.IntVar()
    for i in range(1, 6):
        radiobutton = tk.Radiobutton(ventana_escribir_review, text=str(i), variable=calificacion_seleccionada, value=i)
        radiobutton.pack(anchor=tk.W)

    def guardar_review_comentario():
        calificacion = calificacion_seleccionada.get()
        comentario = comentario_text.get("1.0", tk.END).strip()

        if not comentario:
            messagebox.showerror("Error", "Por favor, ingrese un comentario.")
            return

        review = {
            "id_review": len(eventos) + 1,
            "id_evento": id_evento,
            "id_usuario": id_usuario,
            "calificacion": calificacion,
            "Comentario": comentario,
        }

        guardar_review(review)
        messagebox.showinfo("Escribir review", "Review guardada exitosamente.")
        ventana_escribir_review.destroy()

    boton_guardar_review = tk.Button(ventana_escribir_review, text="Guardar Review", command=guardar_review_comentario)
    boton_guardar_review.pack(pady=10)

    boton_volver_menu = tk.Button(ventana_escribir_review, text="Volver al Menú Principal", command=root.deiconify)
    boton_volver_menu.pack(pady=10)

# Funcion para mostrar la ventana de compartir en redes sociales
def mostrar_ventana_compartir():
    ventana_compartir = tk.Toplevel(root)
    ventana_compartir.title("Compartir en redes sociales")

    redes_sociales = [
        ("WhatsApp", tk.BooleanVar()),
        ("Facebook", tk.BooleanVar()),
        ("Instagram", tk.BooleanVar()),
        ("Telegram", tk.BooleanVar())
    ]

    for red_social, var in redes_sociales:
        checkbutton = tk.Checkbutton(ventana_compartir, text=red_social, variable=var)
        checkbutton.pack(anchor=tk.W)

    def compartir():
        seleccionadas = [red_social for red_social, var in redes_sociales if var.get()]
        if seleccionadas:
            # Aquí guardamos la información en los archivos correspondientes
            guardar_animo({"redes_sociales": seleccionadas})
            guardar_review({"redes_sociales": seleccionadas})
            messagebox.showinfo("Compartir en redes sociales", "Información compartida en redes sociales.")
            ventana_compartir.destroy()
            root.deiconify()  # Vuelve al menú principal después de compartir
        else:
            messagebox.showwarning("Compartir en redes sociales", "No se seleccionaron redes sociales.")

    boton_compartir = tk.Button(ventana_compartir, text="Compartir", command=compartir)
    boton_compartir.pack(pady=10)

    boton_volver_menu = tk.Button(ventana_compartir, text="Volver al Menú Principal", command=root.deiconify)
    boton_volver_menu.pack(pady=10)

# Obtener el número de evento (id_evento) y número de usuario (id_usuario)
id_evento = simpledialog.askinteger("Nro. de Evento", "Ingrese el número de evento:")
id_usuario = simpledialog.askinteger("Nro. de Usuario", "Ingrese el número de usuario:")

# Leer datos de eventos desde el archivo "data/evento.json"
with open("data/evento.json", "r") as eventos_file:
    eventos = json.load(eventos_file)

# Crear la ventana principal
root = tk.Tk()
root.title("Detalles del evento")
root.geometry("960x540")  # Tamaño fijo del marco
root.configure(bg = 'LightYellow')

titulo_label = tk.Label(root, text="Detalles del evento", font=("Open Sans", 16))
titulo_label.pack(pady=20)

boton_mapa = tk.Button(root, text="Mapa y planificador de rutas")
boton_mapa.pack()

def mostrar_ventana_resena():
    ventana_resena = tk.Toplevel(root)
    ventana_resena.title("Reseña y calificaciones")

    boton_escribir_review = tk.Button(ventana_resena, text="Escribir Review", command=lambda: mostrar_ventana_escribir_review(id_evento, id_usuario))
    boton_escribir_review.pack(pady=10)

    boton_señalar_animo = tk.Button(ventana_resena, text="Señalar Ánimo", command=lambda: mostrar_ventana_animo(id_evento, id_usuario))
    boton_señalar_animo.pack(pady=10)

    boton_volver_menu = tk.Button(ventana_resena, text="Volver al Menú Principal", command=root.deiconify)
    boton_volver_menu.pack(pady=10)

boton_resena = tk.Button(root, text="Reseñas y Calificaciones", command=mostrar_ventana_resena)
boton_resena.pack()

boton_compartir = tk.Button(root, text="Compartir en redes sociales", command=mostrar_ventana_compartir)
boton_compartir.pack()

root.mainloop()
