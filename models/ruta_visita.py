"""
Aplicacion Music Tour, Grupo 1, Modelo de datos de la Ruta de Visita.
Se relacion con los Eventos.
=======================================================================================
"""
import json
#from json import scanner

class RutaVisita:
	def __init__(self, id_ruta_visita: int, nombre: str, destinos: list[int]):
		self.id_ruta_visita = id_ruta_visita
		self.nombre = nombre
		self.destinos = destinos

	def to_json(self):
			return {"id_ruta_visita": self.id, "nombre": self.nombre, "destinos": self.destinos }

	
	@classmethod
	def cargar_ruta_json(cls, archivo):
		with open(archivo, "r") as f:
			data = json.load(f)
			print(data)


