import tkinter as tk
from tkinter import messagebox
import json

# Funcion para guardar el animo en el archivo "data/animo.json"
def guardar_animo(animo_data):
    with open("data/animo.json", "w") as file:
        json.dump(animo_data, file)

# Funcion para guardar una reseña en el archivo "data/reviews.json"
def guardar_review(review):
    with open("data/reviews.json", "a") as file:
        json.dump(review, file)
        file.write("\n")

# Funcion para mostrar la ventana de señalar animo
def mostrar_ventana_animo():
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
    guardar_animo({"animo": animo})
    messagebox.showinfo("Señalar ánimo de la review", f"Ánimo '{animo}' guardado exitosamente.")
    ventana_animo.destroy()

    boton_guardar_animo = tk.Button(ventana_animo, text="Guardar Ánimo", command=guardar_animo_seleccionado)
    boton_guardar_animo.pack(pady=10)

    # Retornar el animo seleccionado para que pueda ser capturado en la funcion de guardar_review_comentario()
    return animo_seleccionado

# Funcion para mostrar la ventana de reseña y calificaciones
def mostrar_ventana_resena():
    ventana_resena = tk.Toplevel(root)
    ventana_resena.title("Reseña y calificaciones")

    nombres_eventos = [evento["nombre"] for evento in eventos]
    evento_seleccionado = tk.StringVar(ventana_resena)
    evento_seleccionado.set(nombres_eventos[0]) 

    label_evento = tk.Label(ventana_resena, text="Seleccione un evento:")
    label_evento.pack()

    menu_eventos = tk.OptionMenu(ventana_resena, evento_seleccionado, *nombres_eventos)
    menu_eventos.pack()

    comentario_label = tk.Label(ventana_resena, text="Escriba su reseña:")
    comentario_label.pack()

    comentario_text = tk.Text(ventana_resena, height=5, width=40)
    comentario_text.pack()

    calificacion_label = tk.Label(ventana_resena, text="Seleccione una calificación:")
    calificacion_label.pack()

    calificacion_seleccionada = tk.IntVar()
    for i in range(1, 6):
        radiobutton = tk.Radiobutton(ventana_resena, text=str(i), variable=calificacion_seleccionada, value=i)
        radiobutton.pack(anchor=tk.W)

def guardar_review_comentario():
        evento_nombre = evento_seleccionado.get()
        calificacion = calificacion_seleccionada.get()
        comentario = comentario_text.get("1.0", tk.END).strip()

        if not comentario:
            messagebox.showerror("Error", "Por favor, ingrese un comentario.")
            return

        # Obtener el ID del evento seleccionado
        id_evento_seleccionado = next((evento["id_evento"] for evento in eventos if evento["nombre"] == evento_nombre), None)

        if id_evento_seleccionado is None:
            messagebox.showerror("Error", "Evento inválido.")
            return

        # Capturar el animo seleccionado desde la ventana de señalar animo
        animo_seleccionado = mostrar_ventana_animo().get()

        review = {
            "id_review": len(eventos) + 1,
            "id_evento": id_evento_seleccionado,
            "id_usuario": 1,  # ID de usuario ficticio
            "calificacion": calificacion,
            "Comentario": comentario,
            "animo": animo_seleccionado  # Utilizar el ánimo seleccionado en la reseña
        }

        guardar_review(review)
        messagebox.showinfo("Escribir review", "Review guardada exitosamente.")
        ventana_resena.destroy()

        boton_guardar_review = tk.Button(ventana_resena, text="Guardar Review", command=guardar_review_comentario)
        boton_guardar_review.pack(pady=10)

        boton_señalar_animo = tk.Button(ventana_resena, text="Señalar Ánimo de Review", command=mostrar_ventana_animo)
        boton_señalar_animo.pack(pady=10)


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
            mensaje = f"Se compartirá en: {', '.join(seleccionadas)}"
        else:
            mensaje = "No se seleccionaron redes sociales para compartir."

        messagebox.showinfo("Compartir en redes sociales", mensaje)

        boton_compartir = tk.Button(ventana_compartir, text="Compartir", command=compartir)
        boton_compartir.pack(pady=10)
    
        # Leer datos de eventos desde el archivo "data/evento.json"
        with open("data/evento.json", "r") as eventos_file:
            eventos = json.load(eventos_file)

# Crear la ventana principal
root = tk.Tk()
root.title("Detalles del evento")
root.geometry("960x540")  # Tamaño fijo del marco

titulo_label = tk.Label(root, text="Detalles del evento", font=("Open Sans", 16))
titulo_label.pack(pady=20)

boton_mapa = tk.Button(root, text="Mapa y planificador de rutas")
boton_mapa.pack()

boton_resena = tk.Button(root, text="Reseñas y Calificaciones", command=mostrar_ventana_resena)
boton_resena.pack()

boton_compartir = tk.Button(root, text="Compartir en redes sociales", command=mostrar_ventana_compartir)
boton_compartir.pack()

root.mainloop()