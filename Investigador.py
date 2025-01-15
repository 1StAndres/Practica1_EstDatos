from DoubleList import DoubleList
from Usuario import Usuario


class Investigador(Usuario):
    def __init__(self, nombre, id, fecha_nacimiento, ciudad_nacimiento, tel, email, dir): 
        super().__init__(nombre, id, fecha_nacimiento, ciudad_nacimiento, tel, email, dir)
        self._lista_equipos = DoubleList()
        self._estado_solicitudes = DoubleList()
        self._archivo_equipos = f"{self.getNombre()} {self.getId()}.txt"

    def cargar_equipos(self):
        """Carga los equipos del usuario"""
        with open(f"{self.getNombre()} {self.getId()}.txt", "r") as file:
            self._lista_equipos = [line.strip() for line in file if line.strip()]
        
        for equipo in self._lista_equipos:
                print(equipo)    

    def solicitar_nuevo(self, equipo):
        from Administrador import Administrador
        solicitud = DoubleList()
        solicitud.addLast(equipo)
        solicitud.addLast(self)
        Administrador.solicitudes_nuevo.addLast(solicitud)

    #aca se pide todo el objeto de tipo equipo
    
    def solicitar_eliminar(self, numero_placa, justificacion):
        from Administrador import Administrador
        solicitud = DoubleList()
        solicitud.addLast(str(numero_placa))
        solicitud.addLast(justificacion)
        solicitud.addLast(str(self.getId()))
        solicitud.addLast(self)
        Administrador.solicitudes_eliminar.addFirst(solicitud)
    #aca se pide una justificacion, y un solo atributo del objeto equipo
    
    def getLista_equipos(self):
        return self._lista_equipos
    
    def setLista_equipos(self, lista_equipos):
        self._lista_equipos = lista_equipos

    def getEstado_solicitudes(self):
        return self._estado_solicitudes
    
    def setEstado_solicitudes(self):
        self._estado_solicitudes

    # Entrabajo
    def generarEquipotxt(self):
        with open("info_inventario","w") as fi:
            fi.write(self._lista_equipos)
    
    def generarEstadoSolicitudestxt(self):
        with open("estado_solicitudes","w") as fi:
            fi.write(self._estado_solicitudes)    