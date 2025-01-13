from Usuario import Usuario
from Administrador import Administrador


class Investigador(Usuario):
    def __init__(self, nombre, id, fecha_nacimiento, ciudad_nacimiento, tel, email, dir): 
        super().__init__(nombre, id, fecha_nacimiento, ciudad_nacimiento, tel, email, dir)
        self._lista_equipos = "None"

    def solicitar_nuevo(self, equipo):
        Administrador.solicitudes_nuevo.append(equipo)
    #aca se pide todo el objeto de tipo equipo
    def solicitar_eliminar(self, numero_placa, justificacion):
        solicitud = ["Equipo con número de placa:" + str(numero_placa) + ", Razón: " + justificacion, str(self.getId())]
        Administrador.solicitudes_eliminar.append(solicitud)
    #aca se pide una justificacion, y un solo atributo del objeto equipo
