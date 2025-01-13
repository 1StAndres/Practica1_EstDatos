class Usuario:
  def __init__(self, nombre, id, fecha_nacimiento, ciudad_nacimiento, tel, email, dir): 
    self._nombre = nombre
    self._id = id
    self._fecha_nacimiento = fecha_nacimiento
    self._ciudad_nacimiento = ciudad_nacimiento
    self._tel = tel
    self._email = email
    self._dir = dir

  def setNombre(self, nombre):
    self._nombre = nombre
  def setId(self, id):
    self._id = id
  def setFecha_nacimiento(self, fecha_nacimiento):
    self._fecha_nacimiento = fecha_nacimiento
  def setCiudad_nacimiento(self, ciudad_nacimiento):
    self._ciudad_nacimiento = ciudad_nacimiento
  def setTel(self, tel):
    self._tel = tel
  def setEmail(self, email):
    self._email = email
  def setDir(self, dir):
    self._dir = dir

  def setAll(self, nombre, id, fecha_nacimiento, ciudad_nacimiento, tel, email, dir):
    self._nombre = nombre
    self._id = id
    self._fecha_nacimiento = fecha_nacimiento
    self._ciudad_nacimiento = ciudad_nacimiento
    self._tel = tel
    self._email = email
    self._dir = dir

  def getNombre(self):
    return self._nombre
  def getId(self):
    return self._id
  def getFecha_nacimiento(self):
    return self._fecha_nacimiento
  def getCiudad_nacimiento(self):
    return self._ciudad_nacimiento
  def getTel(self):
    return self._tel
  def getEmail(self):
    return self._email
  def getDir(self):
    return self._dir
  def toString(self):
    return

  def __str__(self):
    
    return self._nombre + " " + str(self._id) + " " + str(self._fecha_nacimiento) + " " +  self._ciudad_nacimiento + " " +  str(self._tel) + " " + self._email + " " +  str(self._dir) + "\n"
