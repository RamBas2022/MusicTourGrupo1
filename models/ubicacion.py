"""
Aplicacion Music Tour, Grupo 1, Modelo de Ubicacion de los Eventos.
===================================================================
"""
import json
#from json import scanner

class Ubicacion:
	def __init__(self, id: int, nombre: str, direccion: str, coordenadas: list[float]):
		self.id_ubicacion = id_ubicacion
		self.nombre = nombre
		self.direccion = direccion
		self.coordenadas = coordenadas

	def to_json(self):
			return {"id_ubicacion": self.id_ubicacion, "nombre": self.nombre, "direccion": self.direccion, "coordenadas": self.coordenadas}

	@classmethod
	@classmethod
	def cargar_ubicacion_json(cls, archivo):
		with open(archivo, "r") as f:
			data = json.load(f)
			print(data)
