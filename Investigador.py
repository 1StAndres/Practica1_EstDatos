from Usuario import Usuario


class Investigador(Usuario):
    def __init__(self, nombre, id, fecha_nacimiento, ciudad_nacimiento, tel, email, dir): 
        super().__init__(nombre, id, fecha_nacimiento, ciudad_nacimiento, tel, email, dir)
        self._lista_equipos = "None"

    def solicitar_nuevo(self, equipo):
