"""
Aplicacion Music Tour, Grupo 1, Modelo de datos de la Ruta de Visita.
Se relacion con los Eventos.
=======================================================================================
"""

class RutaVisita:
	def __init__(self, id_ruta_visita: int, nombre: str, destinos: list[int])
		self.id_ruta_visita = id_ruta_visita
		self.nombre = nombre
		self.destinos = destinos

	def to_json(self):
			return {"id_ruta_visita": self.id, "nombre": self.nombre, "destinos": self.destinos }

	@classmethod
	def from_json(cls, json_data):
		data = json.loads(json_data)
		return cls(data["id_ruta_visita"], data["nombre"], data["destinos"])


