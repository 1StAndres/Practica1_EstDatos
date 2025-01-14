from Usuario import Usuario
from datetime import datetime

class Administrador(Usuario):

    solicitudes_nuevo = []
    solicitudes_eliminar = [] 
    Control_de_cambio = []

    def __init__(self, nombre, id, fecha_nacimiento, ciudad_nacimiento, tel, email, dir, lista_equipos, estado_solicitudes):
        super().__init__(nombre, id, fecha_nacimiento, ciudad_nacimiento, tel, email, dir)
        self._lista_equipos = lista_equipos
    
    def revisar_solicitudes_nuevo(self):
        ahora = datetime.now().strftime('%d %m %Y %H %M %S')


    def revisar_solicitudes_eliminar(self):
        ahora = datetime.now().strftime('%d %m %Y %H %M %S')
        for solicitud in Administrador.solicitudes_eliminar:
            print("Equipo con número de placa:", solicitud[0], ", Razón para eliminarlo: ", solicitud[1])
            resultado = input("A continuación escriba Aprobado o Desaprobado")
            if resultado == "Aprobado":
                cambio = solicitud[2] + ' ' + solicitud[0] + ' ' +  "Eliminar" + ahora
                Administrador.Control_de_cambio.append(cambio)
                for equipo in solicitud[3].getLista_equipos():
                    if str(equipo.getPlaca()) == solicitud[0]:
                        solicitud[3].getLista_equipos().remove(equipo)
                
                #informar al investigador falta
            if resultado == "Desaprobado":
                print("solicitud desaprobada")#lo puse porque me marcaba error y no me dejaba correr investigador, si necesitan cambiar sientanse libre de hacerlo
            else:
                print("Por favor copie Aprobado o Desaprobado")

    #def revisar_solicitudes_eliminar():
