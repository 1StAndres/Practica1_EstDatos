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
                    break
                else:
                    print("Datos incorrectos")
                    fallas+=1
            else:
                print("Identificacion no encontrada")
                fallas+=1
