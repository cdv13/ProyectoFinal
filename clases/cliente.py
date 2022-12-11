from conexion import Conexion

class Cliente():
  def __init__(self,id_cliente,nombre,apellido,dni,correo):
    self.__id_cliente=id_cliente
    self.__nombre=nombre
    self.__apellido=apellido
    self.__dni=dni
    self.__correo=correo
    self.__direccion=""

  def __str__(self):
    cadena=self.__id_cliente+" "+"/n"+self.__nombre+"/n"+self.__apellido+"/n"+str(self.__dni)+"/n"+self.__correo
    return cadena

  @property
  def nombre(self):
    return self.__nombre
  @property
  def apellido(self):
    return self.__apellido
  @property
  def dni(self):
    return self.__dni
  @property
  def correo(self):
    return self.__correo

  @nombre.setter
  def nombre(self, nuevoValor):
    self.__nombre=nuevoValor
  @apellido.setter
  def apellido(self, nuevoValor):
    self.__apellido=nuevoValor
  @dni.setter
  def dni(self, nuevoValor):
    self.__dni=nuevoValor
  @correo.setter
  def correo(self, nuevoValor):
    self.__correo=nuevoValor
    
  def insertar_CL(self):
    datosC=(self.nombre,self.apellido, self.dni,self.correo)
    conexion=Conexion("BaseDatos\superMarket.db")
    conexion.insert("INSERT INTO cliente (nombre,apellido,dni,correo) VALUES (?,?,?,?)", datosC)
    
  def eliminar_CL(self):
    conexion=Conexion("BaseDatos\superMarket.db")
    conexion.delete(f"DELETE FROM cliente WHERE id_cliente={self.__id_cliente}")

  def consulta_CL(self):
    conexion=Conexion("BaseDatos\superMarket.db")
    conexion.read(f"SELECT * FROM cliente WHERE id_cliente={self.__id_cliente}") 


#cliente=Cliente("", "Prueba2", "Prueba2", 12345678, "prueba2@gmail.com")
#cliente.insertar_CL()
#cliente.eliminar_CL()
#cliente.consulta_CL()
#print(cliente)