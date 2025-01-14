from Usuario import Usuario
from Administrador import Administrador


class Investigador(Usuario):
    def __init__(self, nombre, id, fecha_nacimiento, ciudad_nacimiento, tel, email, dir): 
        super().__init__(nombre, id, fecha_nacimiento, ciudad_nacimiento, tel, email, dir)
        self._lista_equipos = []
        self._estado_solicitudes = []
        self._archivo_equipos = f"{self.getNombre()} {self.getId()}.txt"

    def cargar_equipos(self):
        """Carga los equipos del usuario"""
        with open(self._archivo_equipos, "r") as file:
            self._lista_equipos = [line.strip() for line in file if line.strip()]
        print(f"Equipos cargados desde {self._archivo_equipos}.")
        
        for equipo in self._lista_equipos:
                print(equipo)    

    def solicitar_nuevo(self, equipo):
        Administrador.solicitudes_nuevo.append(equipo)
    #aca se pide todo el objeto de tipo equipo
    def solicitar_eliminar(self, numero_placa, justificacion):
        solicitud = [str(numero_placa), justificacion, str(self.getId()), self]
        Administrador.solicitudes_eliminar.append(solicitud)
    #aca se pide una justificacion, y un solo atributo del objeto equipo
    
    def getLista_equipos(self):
        return self._lista_equipos
    
    def setLista_equipos(self, lista_equipos):
        self._lista_equipos = lista_equipos

    def getEstado_solicitudes(self):
        return self._estado_solicitudes
    
    def setEstado_solicitudes(self):
        self._estado_solicitudes
    