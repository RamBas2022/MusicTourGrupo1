"""
Aplicacion Music Tour, Grupo 1, Modelo de datos de los Eventos.
Se relaciona con el modelo de Ubicacion, donde esta la direccion y coordenadas del Evento.
==========================================================================================
"""
import json
#from json import scanner

class Evento:
	def __init__(self, id_evento: int, nombre: str, artista: str, genero: str, id_ubicacion: int, hora_inicio: str, hora_fin: str, descripcion: str, imagen: str):
		self.id_evento= id_evento
		self.nombre = nombre
		self.artista = artista
		self.genero = genero
		self.id_ubicacion = id_ubicacion
		self.hora_inicio = hora_inicio
		self.hora_fin = hora_fin
		self.descripcion = descripcion
		self.imagen = imagen

	@classmethod
	def cargar_evento_json(cls, archivo):
		with open(archivo, "r") as f:
			data = json.load(f)
			print(data)
		
		return [cls(**evento) for evento in data]

	

