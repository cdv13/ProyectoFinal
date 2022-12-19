from pathlib import Path
import sys
sys.path.append(str(Path(__file__).parent.parent))
from clases.conexion import Conexion

class Usuario():
  def __init__(self,id_usuario,clave): 
    self.__id_usuario=id_usuario
    self.__clave=clave
    self.__tipo=""

  def __str__(self):
    cadena=self.__id_usuario+" "+"\n"+str(self.__clave)
    return cadena

  @property
  def id_usuario(self):
    return self.__id_usuario
  @property
  def clave(self):
    return self.__clave
  @property
  def tipo(self):
    return self.__tipo

  @id_usuario.setter
  def id_usuario(self, nuevoValor):
    self.__id_usuario=nuevoValor
  @clave.setter
  def clave(self, nuevoValor):
    self.__clave=nuevoValor

  def consulta_US(self):
    conexion=Conexion("BaseDatos\superMarket.db")
    datos=conexion.read(f"SELECT * FROM usuario WHERE id_usuario='{self.__id_usuario}' and clave='{self.__clave}'")
    
    #no me da el error cuando ingreso cualqier cosa  
    print("datos",datos)
    if datos !=[]:
      return True
    else:
      return False

  def consulta_tipo(self):
      conexion=Conexion("BaseDatos\superMarket.db")
      tipo=conexion.read(f"SELECT tipo FROM usuario WHERE id_usuario='{self.__id_usuario}' and clave='{self.__clave}'")
      return tipo[0][0]

  def insertar_US(self):
    datosU=(self.id_usuario, self.clave)
    
    conexion=Conexion("BaseDatos\superMarket.db")
    conexion.insert("INSERT INTO usuario (id_usuario,clave) VALUES (?,?)", datosU)
    
  def eliminar_US(self):
    conexion=Conexion("BaseDatos\superMarket.db")
    conexion.delete(f"DELETE FROM usuario WHERE id_usuario='{self.__id_usuario}'")

  def consultarCliente(self):
    conexion=Conexion("BaseDatos\superMarket.db")
    dato=conexion.read(f"SELECT id_cliente FROM cliente INNER JOIN usuario WHERE correo='{self.id_usuario}'")
    return dato[0][0]

#usuario=Usuario("sandra@gmail.com",1234)
#usuario.insertar_US()
#usuario.eliminar_US()
#usuario.consulta_tipo()
#print(usuario.consultarCliente())