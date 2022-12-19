from pathlib import Path
import sys
sys.path.append(str(Path(__file__).parent.parent))
from clases.conexion import Conexion

class Direccion():
  def __init__(self,id_direccion,calle,altura,localidad,provincia, postal):
    self.__id_direccion=id_direccion
    self.__calle=calle
    self.__altura=altura
    self.__localidad=localidad
    self.__provincia=provincia
    self.__postal=postal

  def __str__(self):
    cadena=str(self.__id_direccion)+" "+"/n"+self.__calle+"/n"+str(self.__altura)+"/n"+str(self.__localidad)+"/n"+self.__provincia
    return cadena

  @property
  def calle(self):
    return self.__calle
  @property
  def altura(self):
    return self.__altura
  @property
  def localidad(self):
    return self.__localidad
  @property
  def provincia(self):
    return self.__provincia
  @property
  def direccion(self):
    return self.__direccion
  @property
  def postal(self):
    return self.__postal

  @calle.setter
  def calle(self, nuevoValor):
    self.__calle=nuevoValor
  @altura.setter
  def altura(self, nuevoValor):
    self.__altura=nuevoValor
  @localidad.setter
  def localidad(self, nuevoValor):
    self.__localidad=nuevoValor
  @provincia.setter
  def provincia(self, nuevoValor):
    self.__provincia=nuevoValor
  @direccion.setter
  def direccion(self, nuevoValor):
    self.__direccion=nuevoValor
  @postal.setter
  def postal(self, nuevoValor):
    self.__postal=nuevoValor
    
  def insertar_DR(self):
    datos=(self.calle,self.altura, self.localidad,self.provincia, self.postal)
    conexion=Conexion("BaseDatos\superMarket.db")
    conexion.insert("INSERT INTO direccion (calle,altura,localidad,provincia,codiPopostal) VALUES (?,?,?,?.?)", datos)
    
  def eliminar_DR(self):
    conexion=Conexion("BaseDatos\superMarket.db")
    conexion.delete(f"DELETE FROM direccion WHERE id_direccion={self.__id_direccion}")

  def consulta_DR(self):
    conexion=Conexion("BaseDatos\superMarket.db")
    conexion.read(f"SELECT * FROM direccion WHERE id_direccion={self.__id_direccion}") 

  def modificar_Dir(self):
    datos=(self.calle,self.altura, self.localidad,self.provincia, self.postal, self.direccion)
    conexion=Conexion("BaseDatos\superMarket.db")
    conexion.update("UPDATE direccion SET calle=?, altura=?,localidad=?, provincia=?, codigoPostal=?  WHERE id_direccion=?", datos)
