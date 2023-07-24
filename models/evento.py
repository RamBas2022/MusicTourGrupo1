"""
Aplicacion Music Tour, Grupo 1, Modelo de datos de los Eventos.
Se relaciona con el modelo de Ubicacion, donde esta la direccion y coordenadas del Evento.
==========================================================================================

"""

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


		def to_json(self):
			return {"id_evento": self.id_evento, "nombre": self.nombre, "artista": self.artista, "genero": self.genero, "id_ubicacion": self.id_ubicacion, "hora_inicio": self.hora_inicio, "hora_fin": self.hora_fin, "descripcion":	self.descripcion, "imagen": self.imagen }

		@classmethod
		def from_json(cls, json_data):
			data = json.loads(json_data)
			return cls(data["id_evento"], data["nombre"], data["artista"], data["genero"], data["id_ubicacion"], data["hora_inicio"], data["hora_fin"], data["descripcion"], data["imagen"])

