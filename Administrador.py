from Investigador import Investigador

class Administrador(Investigador):

    solicitudes_nuevo = []
    solicitudes_eliminar = [] 

    def __init__(self, nombre, id, fecha_nacimiento, ciudad_nacimiento, tel, email, dir, lista_equipos):
        super().__init__(nombre, id, fecha_nacimiento, ciudad_nacimiento, tel, email, dir)
        self._lista_equipos = lista_equipos
    
    def revisar_solicitudes_nuevo(self):
        for solicitud in Administrador.solicitudes_nuevo:
            print(solicitud[0])
            resultado =input("A continuación escriba Aprobado o Desaprobado")
            if resultado == "Aprobado":
                
            if resultado == "Desaprobado":

            else:
                print("Por favor copie Aprobado o Desaprobado")

    #def revisar_solicitudes_eliminar():
