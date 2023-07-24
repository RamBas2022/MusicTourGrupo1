"""
Aplicacion Music Tour, Grupo 1, Modelo de datos de los Review, para calificar los Eventos.
==========================================================================================
"""

class Review:
	def __init__(self, id_review: int, id_evento: int, id_usuario: int, calificacion: int, comentario: str, animo: str):
		self.id_review = id_review
		self.id_evento = id_evento
		self.id_usuario = id_usuario
		self.calificacion = calificacion
		self.comentario = comentario
		self.animo = animo

	def to_json(self):
			return {"id_review": self.id_review, "id_evento": self.id_evento,"id_usuario": self.id_usuario,"calificacion": self.calificacion, "comentario": self.comentario, "animo": self.animo}

	@classmethod
	def from_json(cls, json_data):
		data = json.loads(json_data)
		return cls(data["id_review"], data["id_evento"], data["id_usuario"], data["calificacion"], data["comentario"], data["animo"])
