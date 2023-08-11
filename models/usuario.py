"""
Aplicacion Music Tour, Grupo 1, Modelo de datos de Usuario.
===========================================================
"""
import json
#from json import scanner

class Usuario:
	def __init__(self, id_usuario: int, nombre: str, apellido: str, historial_eventos: list[int]):
		self.id_usuario = id_usuario
		self.nombre = nombre
		self.apellido = apellido
		self.historial_eventos = historial_eventos

	
	@classmethod
	def cargar_usuario_json(cls, archivo):
		with open(archivo, "r") as f:
			data = json.load(f)
			print(data)
		
		return [cls(**usuario) for usuario in data]



	