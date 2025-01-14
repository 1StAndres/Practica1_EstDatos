from DoubleList import DoubleList
from Investigador import Investigador
from datetime import datetime

class Administrador(Investigador):

    solicitudes_nuevo = DoubleList()
    solicitudes_eliminar = DoubleList()
    control_de_cambio = DoubleList()

    def __init__(self, nombre, id, fecha_nacimiento, ciudad_nacimiento, tel, email, dir, lista_equipos, estado_solicitudes):
        super().__init__(nombre, id, fecha_nacimiento, ciudad_nacimiento, tel, email, dir)
        self._lista_equipos = lista_equipos
    
    def revisar_solicitudes_nuevo(self):
        ahora = datetime.now().strftime('%d %m %Y %H %M %S')
        for solicitud in Administrador.solicitudes_nuevo:
            print("El Investigador:", solicitud.first().getData().getNombre(), "quiere solitictar un nuevo equipo: ", solicitud.first().getNext().getData().getNombre(), "con valor: ", str(solicitud.first().getNext().getData().getValor()))
            resultado = input("A continuación escriba Aprobado o Desaprobado")
            if resultado == "Aprobado":
                cambio = str(solicitud.first().getNext().getData().getId()) + " " + str(solicitud.first().getData().getPlaca()) + " " + "Agrega"
                Administrador.control_de_cambio.addLast(cambio)
                solicitud.first().getNext().getData().getLista_equipos().addLast(solicitud.first().getData())
                #poner a lo mejor un atributo más para investigador, que se vacíe cada vez 
                #que se printee un mensaje indicandole al inves el resultado de su solicitud
            if resultado == "Desaprobado":
                print("Solicitud desaprobada")
            else:
                print("Por favor copie Aprobado o Desaprobado")

    def revisar_solicitudes_eliminar(self):
        ahora = datetime.now().strftime('%d %m %Y %H %M %S')
        for solicitud in Administrador.solicitudes_eliminar:
            print("Equipo con número de placa:", solicitud.first().getData(), ", Razón para eliminarlo: ", solicitud.first().getNext().getData())
            resultado = input("A continuación escriba Aprobado o Desaprobado")
            if resultado == "Aprobado":
                cambio = solicitud.first().getNext().getNext().getData() + ' ' + solicitud.first().getData() + ' ' +  "Eliminar" + ahora
                Administrador.control_de_cambio.addLast(cambio)
                for equipo in solicitud.first().getNext().getNext().getNext().getLista_equipos():
                    if str(equipo.getPlaca()) == solicitud.first().getNext().getNext().getNext():
                        solicitud.first().getNext().getNext().getNext().getData().getLista_equipos().remove(equipo)
                
                #informar al investigador falta
            if resultado == "Desaprobado":
                print("Solicitud desaprobada")#lo puse porque me marcaba error y no me dejaba correr investigador, si necesitan cambiar sientanse libre de hacerlo
            else:
                print("Por favor copie Aprobado o Desaprobado")

