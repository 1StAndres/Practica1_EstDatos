from DoubleList import DoubleList

class Equipo:
    todos_los_equipos = DoubleList()
    def __init__(self, nombre, placa, fecha, valor):
        self._nombre_del_equipo = nombre
        self._numero_de_placa = placa
        self._fecha_de_compra = fecha
        self._valor_de_compra = valor
        self._usuario = "None"


        Equipo.todos_los_equipos.addLast(self)

    def getNombre(self):
        return self._nombre_del_equipo
    
    def getPlaca(self):
        return self._numero_de_placa
    
    def getFecha(self):
        return self._fecha_de_compra
    
    def getValor(self):
        return self._valor_de_compra
    
    def getUsuario(self):
        return self._usuario     
