class Hora:
  def __init__(self,hora,minutos):#No se si incluir segundos
    self.hora = hora
    self.minutos = minutos
  
  def getHora(self):
    return self.Hora
  
  def getMinutos(self):
    return self.minutos
  
  def setHora(self, hora):
    self.hora = hora
  
  def setMinutos(self, minutos):
    self.minutos = minutos

  def setAll(self,hora,minutos):
    self.hora = hora
    self.minutos = minutos
