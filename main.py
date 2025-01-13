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
                    else:
                        print("Bienvenido administrador")
                    break
                else:
                    print("Datos incorrectos")
                    fallas+=1
            else:
                print("Identificacion no encontrada")
                fallas+=1
