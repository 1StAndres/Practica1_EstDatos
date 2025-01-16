from DoubleList import DoubleList
from Usuario import Usuario

class Investigador(Usuario):

    estado_solicitudes_general = DoubleList()
    solicitudes_nuevo = DoubleList()
    solicitudes_eliminar = DoubleList()

    def __init__(self, nombre, id, fecha_nacimiento, ciudad_nacimiento, tel, email, dir): 
        super().__init__(nombre, id, fecha_nacimiento, ciudad_nacimiento, tel, email, dir)
        self._lista_equipos = DoubleList()
        self._archivo_equipos = f"{self.getNombre()} {self.getId()}.txt"

    def cargar_equipos(self):
        """Carga los equipos del usuario"""
        with open(f"{self.getNombre()} {self.getId()}.txt", "r") as file:
            self._lista_equipos = [line.strip() for line in file if line.strip()]
        
        for equipo in self._lista_equipos:
                print(equipo)    

    def solicitar_nuevo(self, equipo):
        solicitud = DoubleList()
        solicitud.addLast(equipo)
        solicitud.addLast(self)
        Investigador.solicitudes_nuevo.addLast(solicitud)
        estado = DoubleList()
        estado.addLast(equipo.getNombre())
        estado.addLast("Pendiente (Agregar)")
        estado.addLast(self.getNombre())
        Investigador.estado_solicitudes_general.addLast(estado)
        

    #aca se pide todo el objeto de tipo equipo
    
    def solicitar_eliminar(self, numero_placa, justificacion):
        solicitud = DoubleList()
        solicitud.addLast(str(numero_placa))
        solicitud.addLast(justificacion)
        solicitud.addLast(str(self.getId()))
        solicitud.addLast(self)
        Investigador.solicitudes_eliminar.addFirst(solicitud)
        estado = DoubleList()
        estado.addLast(numero_placa)
        estado.addLast("Pendiente (Eliminar)")
        estado.addLast(self.getNombre())
        Investigador.estado_solicitudes_general.addLast(estado)
    
    def getLista_equipos(self):
        return self._lista_equipos
    
    def setLista_equipos(self, lista_equipos):
        self._lista_equipos = lista_equipos


    # Entrabajo
    def generarEquipotxt(self):
        with open("inventario.txt", "w") as fi:
            equipo_actual = self._lista_equipos.first()
            while equipo_actual:
                fi.write(equipo_actual.getData() + "\n")
                equipo_actual = equipo_actual.getNext()
    
    def generarEstadoSolicitudestxt(self):
        estado_actual = Investigador.estado_solicitudes_general.first()
    
        while estado_actual:
            estado_investigador = estado_actual.getData()
            nombre_equipo = estado_investigador.first().getData()
            estado = estado_investigador.first().getNext().getData() 
            nombre_investigador = estado_investigador.first().getNext().getNext().getData()
            archivo_investigador = f"{nombre_investigador}_Solicitudes.txt"

            with open(archivo_investigador, "a") as fi:
                fi.write(f"{nombre_equipo} {estado} {nombre_investigador}\n")
            
            estado_actual = estado_actual.getNext()