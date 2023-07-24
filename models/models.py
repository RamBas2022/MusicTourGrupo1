class Evento:
	def __init__(self, id: int, nombre: str, artista: str, genero: str, id_ubicacion: int, hora_inicio: str, hora_fin: str, descripcion: str, imagen: str)
		self.id = id
		self.nombre = nombre
		self.artista = artista
		self.genero = genero
		self.id_ubicacion = id_ubicacion
		self.hora_inicio = hora_inicio
		self.hora_fin = hora_fin
		self.descripcion = descripcion
		self.imagen = imagen

		def to_json(self):
			return {"id": self.id, "nombre": self.nombre, "artista": self.artista, "genero": self.genero, "id_ubicacion": self.id_ubicacion, "hora_inicio": self.hora_inicio, "hora_fin": self.hora_fin, "descripcion":	self.descripcion, "imagen": self.imagen }

		@classmethod
		def from_json(cls, json_data):
			data = json.loads(json_data)
			return cls(data["id"], data["nombre"], data["artista"], data["genero"], data["id_ubicacion"], data["hora_inicio"], data["hora_fin"], data["descripcion"], data["imagen"])

class Usuario:
	def __init__(self, id: int, nombre: str, apellido: str, historial_eventos: list[int])
		self.id = id
		self.nombre = nombre
		self.apellido = apellido
		self.historial_eventos = historial_eventos

	def to_json(self):
			return {"id": self.id, "nombre": self.nombre, "apellido": self.apellido, "historial_eventos": self.historial_eventos}

	@classmethod
	def from_json(cls, json_data):
		data = json.loads(json_data)
		return cls(data["id"], data["nombre"], data["apellido"], data["historial_eventos"])		


class Ubicacion:
	def __init__(self, id: int, nombre: str, direccion: str, coordenadas: list[float])
		self.id = id
		self.nombre = nombre
		self.direccion = direccion
		self.coordenadas = coordenadas

	def to_json(self):
			return {"id": self.id, "nombre": self.nombre, "direccion": self.direccion, "coordenadas": self.coordenadas}

	@classmethod
	def from_json(cls, json_data):
		data = json.loads(json_data)
		return cls(data["id"], data["nombre"], data["direccion"], data["coordenadas"])

class Review:
	def __init__(self, id: int, id_evento: int, id_usuario: int, calificacion: int, comentario: str, animo: str)
		self.id = id
		self.id_evento = id_evento
		self.id_usuario = id_usuario
		self.calificacion = calificacion
		self.comentario = comentario
		self.animo = animo

	def to_json(self):
			return {"id": self.id, "id_evento": self.id_evento,"id_usuario": self.id_usuario,"calificacion": self.calificacion, "comentario": self.comentario, "animo": self.animo}

	@classmethod
	def from_json(cls, json_data):
		data = json.loads(json_data)
		return cls(data["id"], data["id_evento"], data["id_usuario"], data["calificacion"], data["comentario"], data["animo"])

class RutaVisita:
	def __init__(self, id: int, nombre: str, destinos: list[int])
		self.id = id
		self.nombre = nombre
		self.destinos = destinos

	def to_json(self):
			return {"id": self.id, "nombre": self.nombre, "destinos": self.destinos }

	@classmethod
	def from_json(cls, json_data):
		data = json.loads(json_data)
		return cls(data["id"], data["nombre"], data["destinos"])


