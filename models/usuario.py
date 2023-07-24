"""
Aplicacion Music Tour, Grupo 1, Modelo de datos de Usuario.
===========================================================
"""

class Usuario:
	def __init__(self, id_usuario: int, nombre: str, apellido: str, historial_eventos: list[int]):
		self.id_usuario = id_usuario
		self.nombre = nombre
		self.apellido = apellido
		self.historial_eventos = historial_eventos

	def to_json(self):
			return {"id_usuario": self.id_usuario, "nombre": self.nombre, "apellido": self.apellido, "historial_eventos": self.historial_eventos}

	@classmethod
	def from_json(cls, json_data):
		data = json.loads(json_data)
		return cls(data["id_usuario"], data["nombre"], data["apellido"], data["historial_eventos"])