from Investigador import Investigador
from Usuario import Usuario
from Fecha import Fecha
from Direccion import Direccion
from Administrador import Administrador
from Equipo import Equipo
from DoubleList import DoubleList

def menu_administrador():
    """Menú para usuarios con rol de administrador."""
    while True:
        print("\n--- Menú Administrador ---")
        print("1. Consultar la lista de equipos que están en el inventario del centro de investigación cargados a su nombre")
        print("2. Registrar Usuario")
        print("3. Eliminar usuarios")
        print("4. cambiar contraseñas")
        print("5. responder las solicitudes agregar")
        print("6. responder las solicitudes eliminar")
        print("7. generar un archivo txt con la información del inventario de un investigador en específico")
        print("8. archivo txt con la información de todo el inventario del centro discriminado por investigador")
        print("9. un archivo de texto con el control de cambios")
        print("10.un archivo de texto para cada tipo de solicitud pendiente por responder (agregar (“Solicitudes_agregar.txt”) o eliminar (“Solicitudes_eliminar.txt”)).")
        print("11. Salir")
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            print("Consultando información...")
            Investigador.cargar_equipos(user_admin)
        elif opcion == "2":
            print("Registrando Usuario...")
            Administrador.Registrar_Usuario(user_admin)
        elif opcion == "3":
            #falta
            print("Eliminando usuarios...")
        elif opcion == "4":
            #falta
            print("cambiando contraseñas")
        elif opcion == "5":
            user_admin.revisar_solicitudes_nuevo()
        elif opcion == "6":
            print("Abriendo solicitudes para eliminar")
            user_admin.revisar_solicitudes_eliminar()
        elif opcion == "7":
            print("Generando un archivo txt con la información del inventario de un investigador en específico")
            idInv = input("ingrese el id del investigador")
            Administrador.generarInventariotxt(idInv)
        elif opcion == "8":
            print("Generando archivo de texto con la información de todo el inventario del centro de investigacion...")
            Administrador.generarInventarioCompletotxt()
        elif opcion == "9":
            print("Generando archivo de texto con el control de cambios")
            Administrador.generarControlDeCambiostxt()
        elif opcion == "10":
            respuesta = input("¿Qué desea, el txt de eliminar o agregar? ")
            if respuesta == "eliminar":
                user_admin.generarSolicitudesEliminarPendientesTxt
            if respuesta == "agregar":
                user_admin.generarSolicitudesAgregarPendientesTxt
            else:
                print("Opción no válida. Intente nuevamente.")
        elif opcion == "11":
            print("Saliendo del menú administrador...")
            break
        else:
            print("Opción no válida. Intente nuevamente.")

def menu_investigador():
    """Menú para usuarios con rol de investigador."""
    while True:
        print("\n--- Menú Investigador ---")
        print("1. Consultar la lista de equipos que están en el inventario del centro de investigación cargados a su nombre") # a quien le toque el punto lo redacta como quiera
        print("2.  Solicitar agregar nuevos equipos")
        print("3.  Solicitar eliminar equipos de su inventario.")
        print("4. Consultar el estado de sus solicitudes")
        print("5. Generar un archivo txt con la información de su inventario")
        print("6. Generar un archivo txt con el estado de sus solicitudes")
        print("7. Salir")
        opcion = input("Seleccione una opción: ")
        # Cada quien modifica lo que le toque para que el menu lo haga
        if opcion == "1":
            print("Consultando información...")
            user_ejemplo.cargar_equipos()
        elif opcion == "2":
            print("Solicitando agregar nuevos equipos...")
            nombre = input("Nombre del equipo:")
            placa = input("ingrese numero de placa del equipo:")
            dia = input("dia de compra del equipo:")
            mes = input("mes de compra del equipo :")
            año = input("año de compra del equipo en formato AAAA:")
            fecha = Fecha(dia, mes, año)
            valor = input("valor compra del equipo:")
            equipo_nuevo = Equipo(nombre, placa, fecha, valor) #objeto del parametro de solcitar_nuevo
            equipo_nuevo.setUsuario(user_ejemplo)
            user_ejemplo.solicitar_nuevo(equipo_nuevo)
            #solicitud = DoubleList()
            #solicitud.addLast(equipo_nuevo)
            #solicitud.addLast(user_ejemplo)
            #Administrador.solicitudes_nuevo.addLast(solicitud)
        elif opcion == "3":
            print("Por favor digite numero de placa y agregue una justificacion para eliminar equipos de su inventario...")
            numero_placa = input("ingrese numero de placa del equipo:")
            justificacion = input("ingrese una justificacion:")
            user_ejemplo.solicitar_eliminar(numero_placa,justificacion)
            #solicitud = DoubleList()
            #solicitud.addLast(str(numero_placa))
            #solicitud.addLast(justificacion)
            #solicitud.addLast(str(user_ejemplo.getId()))
            #solicitud.addLast(user_ejemplo)
            #Administrador.solicitudes_eliminar.addFirst(solicitud)
        elif opcion == "4":
            for estado in Investigador.estado_solicitudes_general:
                if user_ejemplo.getNombre() == estado.first().getNext().getNext().getData():
                    print(estado.first().getData())
                    print(estado.first().getNext().getData())
        elif opcion == "5":
            print("Generando un archivo txt con la información de su inventario...")
            Investigador.generarEquipotxt()
        elif opcion == "6":
            print("Generando un archivo txt con el estado de sus solicitudes...")
            Investigador.generarEstadoSolicitudestxt(user_ejemplo)
        elif opcion == "7":
            print("Saliendo del menú investigador...")
            break
        else:
            print("Opción no válida. Intente nuevamente.")

#usuario de ejemplo
user_ejemplo = Investigador("Juan-Perez", "24567898", Fecha("12", "10", "1980"), "Medellin", "3003233234", "juanperez@edl.edu.co", Direccion())
#print(user_ejemplo)

direc = Direccion()
direc.setAll("tr45", "4S-73", "Poblado", "Medellin", "null", "null")
user_admin = Administrador("Camila-Jimenez", "2345902", Fecha("15", "09", "1985"), "Cali", "3003234567", "camilajimenez@edl.edu.co", direc)
print(user_admin)
#inicio del sistema
#lee archivos empleados y password
with open("Empleados.txt", "r") as arc_empleados, open("Password.txt", "r") as arc_password:
    #diccionario para almacenar contraseñas 
    contraseñas = {}
    rangos = {}
    for linea in arc_password:
        #cada linea tiene formato de id contra rango
        identificacion, contraseña, rango = linea.strip().split()
        contraseñas[identificacion] = contraseña
        rangos[identificacion] = rango

    fallas=0
    while fallas<=3:
        if fallas==3:
            print('Lo siento, su acceso no es permitido')
            break
        else:
            identificacion = input("Ingrese su identificacion: ")
            contraseña = input("Ingrese su contraseña: ")
            #verificacion de id
            if identificacion in contraseñas:
                #verificacion de contraseña
                if contraseña == contraseñas[identificacion]:
                    print("Acceso permitido :D")
                    fallas=0
                    #verificacion si es investigador o administrador
                    if rangos[identificacion] == "investigador":
                        print("Bienvenido investigador")
                        #punto numero 3
                        menu_investigador()
                    else:
                        print("Bienvenido administrador")
                        menu_administrador()
                    break
                else:
                    print("Datos incorrectos")
                    fallas+=1
            else:
                print("Identificacion no encontrada")
                fallas+=1