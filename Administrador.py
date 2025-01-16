from DoubleList import DoubleList
from Investigador import Investigador
from datetime import datetime
from Direccion import Direccion
from Fecha import Fecha

class Administrador(Investigador):

    control_de_cambio = DoubleList()

    def __init__(self, nombre, id, fecha_nacimiento, ciudad_nacimiento, tel, email, dir):
        super().__init__(nombre, id, fecha_nacimiento, ciudad_nacimiento, tel, email, dir)
    
    def revisar_solicitudes_nuevo(self):
        ahora = datetime.now().strftime('%d %m %Y %H %M %S')
        for solicitud in Investigador.solicitudes_nuevo:
            print("El Investigador:", solicitud.first().getNext().getData().getNombre(), "quiere solitictar un nuevo equipo: ", solicitud.first().getData().getNombre(), "con valor: ", str(solicitud.first().getData().getValor()))
            resultado = input("A continuación escriba Aprobado o Desaprobado: ")
            if resultado == "Aprobado":
                cambio = str(solicitud.first().getNext().getData().getId()) + " " + str(solicitud.first().getData().getPlaca()) + " " + "Agrega" + ahora
                Administrador.control_de_cambio.addLast(cambio)
                solicitud.first().getNext().getData().getLista_equipos().addLast(solicitud.first().getData())
                solicitud.first().getNext().getData().generarEquipotxt()
                for pendiente in Investigador.estado_solicitudes_general:
                    if pendiente.first().getNext().getNext().getData() == solicitud.first().getNext().getData().getNombre():
                        if pendiente.first().getData() == solicitud.first().getData().getNombre():
                            pendiente.removeLast()
                            pendiente.addLast("Aprobado (Agregar)")
                print("Solicitud aprobada")
            elif resultado == "Desaprobado":
                for pendiente in Investigador.estado_solicitudes_general:
                    if pendiente.first().getNext().getNext().getData() == solicitud.first().getNext().getData().getNombre():
                        if pendiente.first().getData() == solicitud.first().getData().getNombre():
                            pendiente.removeLast()
                            pendiente.addLast("Desaprobado (Agregar)")
                print("Solicitud desaprobada")
            else:
                print("Por favor copie Aprobado o Desaprobado")

    def revisar_solicitudes_eliminar(self):
        ahora = datetime.now().strftime('%d %m %Y %H %M %S')
        for solicitud in Investigador.solicitudes_eliminar:
            print("Equipo con número de placa:", solicitud.first().getData(), ", Razón para eliminarlo: ", solicitud.first().getNext().getData())
            resultado = input("A continuación escriba Aprobado o Desaprobado")
            if resultado == "Aprobado":
                cambio = solicitud.first().getNext().getNext().getData() + ' ' + solicitud.first().getData() + ' ' +  "Eliminar" + ahora
                Administrador.control_de_cambio.addLast(cambio)
                for equipo in solicitud.first().getNext().getNext().getNext().getData().getLista_equipos():
                    if str(equipo.getPlaca()) == solicitud.first().getData():
                        solicitud.first().getNext().getNext().getNext().getData().getLista_equipos().remove(equipo)
                for pendiente in Investigador.estado_solicitudes_general:
                    if pendiente.first().getNext().getNext().getData() == solicitud.first().getNext().getNext().getNext().getData().getNombre():
                        if pendiente.first().getData() == solicitud.first().getData():
                            pendiente.removeLast()
                            pendiente.addLast("Desaprobado (Eliminar)")
                print("Solicitued aprobada")
                #informar al investigador falta
            if resultado == "Desaprobado":
                for pendiente in Investigador.estado_solicitudes_general:
                    if pendiente.first().getNext().getNext().getData() == solicitud.first().getNext().getNext().getNext().getData().getNombre():
                        if pendiente.first().getData() == solicitud.first().getData():
                            pendiente.removeLast()
                            pendiente.addLast("Desaprobado (Eliminar)")
                print("Solicitud desaprobada")
            else:
                print("Por favor copie Aprobado o Desaprobado")
    
    def Registrar_Usuario(self):
        nombre_nue = input("Nombre:")
        id_nue = input("identifiacion:")
        dia_nue = input("Dia de nacimiento:")
        mes_nue = input("Mes de nacimiento:")
        año_nue = input("Año de nacimiento en formato AAAA:")
        ciu_nue = input("Ciudad de nacimiento:")
        tel_nue = input("Telefono o celular:")
        email_nue = input("Email del nuevo usuario:")
        calle = input("Calle de residencia:")
        nomen = input("Nomenclatura:")
        bar = input("Barrio:")
        ciu = input("Ciudad:")
        edi = input("Nombre del edificio o urbanizacion (en caso de no aplicar escriba null):")
        apa = input("Numero del apartamento o casa (en caso de no aplicar escriba null):")
        dir_user = Direccion()
        dir_user.setAll(calle, nomen, bar, ciu, edi, apa)
        new_user = Investigador(nombre_nue, id_nue, Fecha(dia_nue, mes_nue, año_nue), ciu_nue, tel_nue, email_nue, dir_user)
        with open("Empleados.txt", "a") as f:
            f.write(f"{new_user.__str__()}")
        contr_nue = input("Contraseña para el nuevo usuario:")
        rol_nue = input("Rol que ocupara el nuevo usuario:")
        with open("Password.txt", "a") as r:
            r.write(f"{id_nue} {contr_nue} {rol_nue} ") 

    def Eliminar_usuario(self):        
        id_eli = input("Ingrese identificacion del usuario a eliminar:")
        ##Elimina usuario en password txt
        with open("Password.txt", "r") as f:
            lineas = f.readlines()
            lineas_fil = [linea for linea in lineas if not linea.startswith(id_eli + " ")]
        with open("Password.txt", "w") as f:
            f.writelines(lineas_fil)  
            ##Elimina usuario en empleados txt
        with open("Empleados.txt","r") as r:
            line = r.readlines()
            line_fil = [linea for linea in line if linea.split()[1] != id_eli]  
        with open("Empleados.txt", "w") as r:
            r.writelines(line_fil)

    def Cambiar_contraseña(self):
        Id_contra_chance = input("Ingrese el id del usuario a cambiar contraseña:")
        contra_chance = input("Escriba la nueva contraseña:")
        with open("Password.txt", "r") as f:
            lineas = f.readlines()

    # Modificar la línea correspondiente al usuario
        lineas_modificadas = []
        for linea in lineas:
            partes = linea.strip().split()
            if partes[0] == Id_contra_chance: 
                partes[1] = contra_chance 
                lineas_modificadas.append(" ".join(partes) + "\n")
            else:
                lineas_modificadas.append(linea)

        with open("Password.txt", "w") as f:
            f.writelines(lineas_modificadas)                  
    #entrabajo
    def generarInventariotxt(self,identificacion):
        lista = DoubleList()
        with open("InventarioGeneral.txt","r")as archivo:
            for linea in archivo:
                if identificacion in linea:
                    lista.addLast(linea)
        with open(f"info_inventario{identificacion}.txt","w") as fi:
            lineaActual = lista.first()
            while lineaActual:               
                fi.write(lineaActual.getData().split(identificacion, 1)[1].strip())
                lineaActual = lineaActual.getNext()
    
    def generarInventarioCompletotxt(self, listaEmpleados):
    # Abre el archivo para escritura
        with open("InventarioGeneral.txt", "w") as fi:
            # Itera sobre la lista de empleados
            empleado_actual = listaEmpleados.first().getData()
            while empleado_actual:
                # Obtén la lista doble de equipos del empleado actual
                lista_equipos = empleado_actual._lista_equipos
                
                # Ordenar la lista doblemente enlazada in-place según el último número de cada cadena
                if lista_equipos.first() and lista_equipos.first().getNext():
                    self.ordenarDoubleList(lista_equipos)
                
                # Escribir los datos ordenados de la lista en el archivo
                equipo_actual = lista_equipos.first()
                while equipo_actual:
                    fi.write(equipo_actual.getData() + "\n")
                    equipo_actual = equipo_actual.getNext()
                
                # Pasa al siguiente empleado
                empleado_actual = listaEmpleados.first().getNext()

    def ordenarDoubleList(self, lista):
        # Implementación de un algoritmo de ordenamiento para una lista doblemente enlazada
        cambiado = True
        while cambiado:
            cambiado = False
            actual = lista.first()
            while actual and actual.getNext():
                siguiente = actual.getNext()
                # Comparar el último número de las cadenas
                valor_actual = int(actual.getData().split()[-1])
                valor_siguiente = int(siguiente.getData().split()[-1])
                if valor_actual > valor_siguiente:
                    # Intercambiar los valores de los nodos
                    actual_data = actual.getData()
                    siguiente_data = siguiente.getData()
                    actual.setData(siguiente_data)
                    siguiente.setData(actual_data)
                    cambiado = True
                actual = siguiente
    
    def generarControlDeCambiostxt(self):
        with open("Control_de_cambios.txt", "w") as fi:
            cambio_actual = Administrador.control_de_cambio.first()
            while cambio_actual:
                fi.write(cambio_actual.getData() + "\n")
                cambio_actual = cambio_actual.getNext()
    
    def generarSolicitudesAgregarPendientesTxt(self):
        with open("Solicitudes_agregar.txt", "w") as fi:
            solicitud_actual = Investigador.solicitudes_nuevo.first()
            while solicitud_actual:
                fi.write(solicitud_actual.getData() + "\n")
                solicitud_actual = solicitud_actual.getNext()

    def generarSolicitudesEliminarPendientesTxt(self):
        with open("“Solicitudes_eliminar.txt", "w") as fi:
            solicitud_actual = Investigador.solicitudes_eliminar.first()
            while solicitud_actual:
                fi.write(solicitud_actual.getData() + "\n")
                solicitud_actual = solicitud_actual.getNext()

