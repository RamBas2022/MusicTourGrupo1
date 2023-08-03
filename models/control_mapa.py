class Controlador_Mapa:
    def __int__(self, ubicación_seleccionada):
        self.app = app
        self.ubicacion_seleccionada = ubicacion_seleccionada 


    def ver_ubicaciones (self):
        return self.ubicacion_seleccionada

    def seleccionar_ubicación (self):
        indice = self.app.vista_ubicaciones.ver_ubicacion_seleccionada()
        if indice is not None:
            ubicacion = self.ubicacion_seleccionada [indice]
            self.app.vista_info.mostrar_info_ubicacion (ubicacion)
            self.app.cambiar_frame(self.app.vista_info)

    def regresar_incio(self):
        self.app.cambiar_frame(self.app.vista_inicio)            
