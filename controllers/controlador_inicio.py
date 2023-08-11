# Controllers

class ControladorInicio:
    def __init__(self, app):
        self.app = app

    def mostrar_eventos(self):
        self.app.cambiar_frame(self.app.vista_eventos)

    def mostrar_historial(self):
        self.app.cambiar_frame(self.app.vista_historial)

    def mostrar_busqueda(self):
        self.app.cambiar_frame(self.app.vista_busqueda)