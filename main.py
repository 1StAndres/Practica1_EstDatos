
#A_empleados = open("Empleados.txt", "r")
#print(A_empleados.read())
#A_empleados.close()

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
        elif opcion == "2":
            print("Registrando Usuario...") 
        elif opcion == "3":
            print("Eliminando usuarios...")
        elif opcion == "4":
            print("cambiando contraseñas")
        elif opcion == "5":
            print("responder las solicitudes agregar")
        elif opcion == "6":
            print("responder las solicitudes eliminar")
        elif opcion == "7":
            print("generar un archivo txt con la información del inventario de un investigador en específico")
        elif opcion == "8":
            print("archivo txt con la información de todo el inventario del centro discriminado por investigador")
        elif opcion == "9":
            print("un archivo de texto con el control de cambios")
        elif opcion == "10":
            print("un archivo de texto para cada tipo de solicitud pendiente por responder (agregar (“Solicitudes_agregar.txt”) o eliminar (“Solicitudes_eliminar.txt”)).")
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
    elif opcion == "2":
      print("Solicitando agregar nuevos equipos...")
    elif opcion == "3":
      print("Solicitando eliminar equipos de su inventario...")
    elif opcion == "4":
      print("Consultando el estado de sus solicitudes...")
    elif opcion == "5":
      print("Generando un archivo txt con la información de su inventario...")
    elif opcion == "6":
      print("Generando un archivo txt con el estado de sus solicitudes...")
    elif opcion == "7":
      print("Saliendo del menú investigador...")
    else:
      print("Opción no válida. Intente nuevamente.")
from Investigador import Investigador
from Usuario import Usuario
from Fecha import Fecha
from Direccion import Direccion
from Administrador import Administrador
from Equipo import Equipo

def menu_administrador(user_admin):
    """Menú para usuarios con rol de administrador."""
    while True:
        print("\n--- Menú Administrador ---")
        print("1. Consultar la lista de equipos que están en el inventario del centro de investigación cargados a su nombre")
        print("2. Registrar Usuario")
        print("3. Eliminar usuarios")
        print("4. Cambiar contraseñas")
        print("5. Responder las solicitudes agregar")
        print("6. Responder las solicitudes eliminar")
        print("7. Generar un archivo txt con la información del inventario de un investigador en específico")
        print("8. Generar un archivo txt con la información de todo el inventario del centro discriminado por investigador")
        print("9. Generar un archivo de texto con el control de cambios")
        print("10. Generar un archivo de texto para cada tipo de solicitud pendiente por responder (agregar o eliminar).")
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
            print("Cambiando contraseñas...")
        elif opcion == "5":
            user_admin.revisar_solicitudes_nuevo()
        elif opcion == "6":
            user_admin.revisar_solicitudes_eliminar()
        elif opcion == "7":
            idInv = input("Ingrese el ID del investigador: ")
            user_admin.generarInventariotxt(idInv)
        elif opcion == "8":
            user_admin.generarInventarioCompletotxt()
        elif opcion == "9":
            user_admin.generarControlDeCambiostxt()
        elif opcion == "10":
            respuesta = input("¿Qué desea, el txt de eliminar o agregar? ")
            if respuesta == "eliminar":
                user_admin.generarSolicitudesEliminarPendientesTxt()
            elif respuesta == "agregar":
                user_admin.generarSolicitudesAgregarPendientesTxt()
            else:
                print("Opción no válida. Intente nuevamente.")
        elif opcion == "11":
            print("Saliendo del menú administrador...")
            break
        else:
            print("Opción no válida. Intente nuevamente.")

def menu_investigador(user_inves):
    """Menú para usuarios con rol de investigador."""
    while True:
        print("\n--- Menú Investigador ---")
        print("1. Consultar la lista de equipos que están en el inventario del centro de investigación cargados a su nombre")
        print("2. Solicitar agregar nuevos equipos")
        print("3. Solicitar eliminar equipos de su inventario.")
        print("4. Consultar el estado de sus solicitudes")
        print("5. Generar un archivo txt con la información de su inventario")
        print("6. Generar un archivo txt con el estado de sus solicitudes")
        print("7. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            print("Consultando información...")
            user_inves.cargar_equipos()
        elif opcion == "2":
            nombre = input("Nombre del equipo: ")
            placa = input("Ingrese número de placa del equipo: ")
            dia = input("Día de compra del equipo: ")
            mes = input("Mes de compra del equipo: ")
            año = input("Año de compra del equipo en formato AAAA: ")
            fecha = Fecha(dia, mes, año)
            valor = input("Valor de compra del equipo: ")
            equipo_nuevo = Equipo(nombre, placa, fecha, valor)
            user_inves.solicitar_nuevo(equipo_nuevo)
            print("Solicitud para agregar equipo enviada.")
        elif opcion == "3":
            num_placa = input("Ingrese número de placa del equipo: ")
            justifi = input("Ingrese una justificación: ")
            user_inves.solicitar_eliminar(num_placa, justifi)
            print("Solicitud para eliminar equipo enviada.")
        elif opcion == "4":
            for estado in user_inves.getEstado_solicitudes():
                print(estado.first().getData())
                print(estado.first().getNext().getData())
        elif opcion == "5":
            print("Generando un archivo txt con la información de su inventario...")
            user_inves.generarEquipotxt()
        elif opcion == "6":
            print("Generando un archivo txt con el estado de sus solicitudes...")
            user_inves.generarEstadoSolicitudestxt()
        elif opcion == "7":
            print("Saliendo del menú investigador...")
            break
        else:
            print("Opción no válida. Intente nuevamente.")

# Inicio del sistema
with open("Empleados.txt", "r") as arc_empleados, open("Password.txt", "r") as arc_password:
    contraseñas = {}
    rangos = {}
    empleados = arc_empleados.readlines()

    for linea in arc_password:
        identificacion, contraseña, rango = linea.strip().split()
        contraseñas[identificacion] = contraseña
        rangos[identificacion] = rango

    while True:
        identificacion = input("Ingrese su identificación: ")
        contraseña = input("Ingrese su contraseña: ")

        if identificacion in contraseñas and contraseña == contraseñas[identificacion]:
            print("Acceso permitido.")
            if rangos[identificacion] == "investigador":
                print("Bienvenido investigador.")
                for linea in empleados:
                    datos = linea.strip().split()
                    if datos[1] == identificacion:
                        direccion = Direccion()
                        direccion.setAll(*datos[8:14])
                        user_inves = Investigador(datos[0], datos[1], Fecha(*datos[2:5]), datos[5], datos[6], datos[7], direccion)
                        menu_investigador(user_inves)
                        break
            elif rangos[identificacion] == "administrador":
                print("Bienvenido administrador.")
                for linea in empleados:
                    datos = linea.strip().split()
                    if datos[1] == identificacion:
                        direccion = Direccion()
                        direccion.setAll(*datos[8:14])
                        user_admin = Administrador(datos[0], datos[1], Fecha(*datos[2:5]), datos[5], datos[6], datos[7], direccion)
                        menu_administrador(user_admin)
                        break
        else:
            print("Datos incorrectos. Intente nuevamente.")
