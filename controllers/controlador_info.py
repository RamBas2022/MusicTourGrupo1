# Controllers

class ControladorInfo:
    def __init__(self, app):
        self.app = app


    def regresar_eventos(self):
        self.app.cambiar_frame(self.app.vista_eventos)

    def regresar_historial(self):
        self.app.cambiar_frame(self.app.vista_historial)

    def regresar_busqueda(self):
        self.app.cambiar_frame(self.app.vista_busqueda)
