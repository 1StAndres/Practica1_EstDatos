class Direccion:
  def __init__(self):
    self._calle = "None"
    self._nomenclatura = "None"
    self._barrio = "None"
    self._ciudad = "None"
    self._edificio = "None"
    self._apto = "None"

  #metodos SET
  def setCalle(self, calle):
    self._calle = calle
  def setNomenclatura(self, nomenclatura):
    self._nomenclatura = nomenclatura
  def setBarrio(self, barrio):
    self._barrio = barrio
  def setCiudad(self, ciudad):
    self._ciudad = ciudad
  def setEdificio(self, edificio):
    self._edificio = edificio
  def setApto(self, apto):
    self._apto = apto

  #metodos GET
  def getCalle(self):
    return self._calle
  def getNomenclatura(self):
    return self._nomenclatura
  def getBarrio(self):
    return self._barrio
  def getCiudad(self):
    return self._ciudad
  def getEdificio(self):
    return self._edificio
  def getApto(self):
    return self._apto

  def setAll(self, calle, nomenclatura, barrio, ciudad, edificio, apto):
    self._calle = calle
    self._nomenclatura = nomenclatura
    self._barrio = barrio
    self._ciudad = ciudad
    self._edificio = edificio
    self._apto = apto

  #Retorno direccion
  def __str__(self):
    return self._calle + " " + self._nomenclatura + " " + self._barrio + " " + self._ciudad +  " " + self._edificio +  " " + self._apto
