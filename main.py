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
            user_admin.cargar_equipos()
        elif opcion == "2":
            user_admin.Registrar_Usuario()
            print("Registrando Usuario...")
        elif opcion == "3":
            user_admin.Eliminar_usuario()
            print("Eliminando usuarios...")
        elif opcion == "4":
            user_admin.Cambiar_contraseña()
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
            #listaEmpleados = DoubleList() faltan los empleados cargados del punto 1
            #listaEmpleados.addLast()
            #Administrador.generarInventarioCompletotxt(listaEmpleados)
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
            user_inves.cargar_equipos()
        elif opcion == "2":
            nombre = input("Nombre del equipo:")
            placa = input("ingrese numero de placa del equipo:")
            dia = input("dia de compra del equipo:")
            mes = input("mes de compra del equipo :")
            año = input("año de compra del equipo en formato AAAA:")
            fecha = Fecha(dia, mes, año)
            valor = input("valor compra del equipo:")
            equipo_nuevo = Equipo(nombre, placa, fecha, valor) #objeto del parametro de solcitar_nuevo
            user_inves.solicitar_nuevo(equipo_nuevo)
            print("Solicitando agregar nuevos equipos...")

        elif opcion == "3":
            print("Por favor digite numero de placa y agregue una justificacion para eliminar equipos de su inventario...")
            num_placa = input("ingrese numero de placa del equipo:")
            justifi = input("ingrese una justificacion:")
            user_inves.solicitar_eliminar(num_placa,justifi)
        elif opcion == "4":
            for estado in user_inves.getEstado_solicitudes():
                print(estado.first().getData())
                print(estado.first().getNext().getData())
        elif opcion == "5":
            print("Generando un archivo txt con la información de su inventario...")
            Investigador.generarEquipotxt()
        elif opcion == "6":
            print("Generando un archivo txt con el estado de sus solicitudes...")
            Investigador.generarEstadoSolicitudestxt(user_inves)
        elif opcion == "7":
            print("Saliendo del menú investigador...")
            break
        else:
            print("Opción no válida. Intente nuevamente.")

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
                    #carga informacion del usuario ingresado
                    #verificacion si es investigador o administrador
                    if rangos[identificacion] == "investigador":
                        print("Bienvenido investigador")
                        for linea in arc_empleados:
                            datos = linea.strip().split()
                            if datos[1] == identificacion:
                                direccion = Direccion()
                                direccion.setAll(datos[8], datos[9], datos[10], datos[11], datos[12], datos[13])
                                user_inves = Investigador(datos[0], int(datos[1]),Fecha(int(datos[2]), int(datos[3]), int(datos[4])), datos[5], datos[6], datos[7], direccion)
                        print(user_inves)    
                        menu_investigador()
                    else:
                        print("Bienvenido administrador")
                        for linea in arc_empleados:
                            datos = linea.strip().split()
                            if datos[1] == identificacion:
                                direccion = Direccion()
                                direccion.setAll(datos[8], datos[9], datos[10], datos[11], datos[12], datos[13])
                                user_admin = Administrador(datos[0], int(datos[1]),Fecha(int(datos[2]), int(datos[3]), int(datos[4])), datos[5], datos[6], datos[7], direccion)
                        print(user_admin)
                        menu_administrador()
                    break
                else:
                    print("Datos incorrectos")
                    fallas+=1
            else:
                print("Identificacion no encontrada")
                fallas+=1
