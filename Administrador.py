from Investigador import Investigador
from datetime import datetime

class Administrador(Investigador):

    solicitudes_nuevo = []
    solicitudes_eliminar = [] 
    Control_de_cambio = []

    def __init__(self, nombre, id, fecha_nacimiento, ciudad_nacimiento, tel, email, dir, lista_equipos, estado_solicitudes):
        super().__init__(nombre, id, fecha_nacimiento, ciudad_nacimiento, tel, email, dir)
        self._lista_equipos = lista_equipos
    
    def revisar_solicitudes_nuevo(self):
        ahora = datetime.now().strftime('%d %m %Y %H %M %S')
        for solicitud in Administrador.solicitudes_nuevo:
            print("Equipo con número de placa:", solicitud[0], ", Razón: ", solicitud[1])
            resultado = input("A continuación escriba Aprobado o Desaprobado")
            if resultado == "Aprobado":
                cambio = solicitud[2] + ' ' + solicitud[0] + ' ' +  "Agregar" + ahora
                Administrador.Control_de_cambio.append(cambio)
                solicitud[3].lista_equipos
                #informar al investigaro falta
            if resultado == "Desaprobado":

            else:
                print("Por favor copie Aprobado o Desaprobado")

    #def revisar_solicitudes_eliminar():
