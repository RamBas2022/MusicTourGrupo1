"""
Aplicacion Music Tour, Grupo 1, Modelo de Ubicacion de los Eventos.
===================================================================
"""

class Ubicacion:
	def __init__(self, id: int, nombre: str, direccion: str, coordenadas: list[float]):
		self.id_ubicacion = id_ubicacion
		self.nombre = nombre
		self.direccion = direccion
		self.coordenadas = coordenadas

	def to_json(self):
			return {"id_ubicacion": self.id_ubicacion, "nombre": self.nombre, "direccion": self.direccion, "coordenadas": self.coordenadas}

	@classmethod
	def from_json(cls, json_data):
		data = json.loads(json_data)
		return cls(data["id_ubicacion"], data["nombre"], data["direccion"], data["coordenadas"])
