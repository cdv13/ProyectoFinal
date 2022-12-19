from pathlib import Path
import sys
sys.path.append(str(Path(__file__).parent.parent))
from clases.conexion import Conexion

class Producto():
  def __init__(self, id_producto:int,nombre:str,descripcion:str,precio:float,stock:int, categoria:str):
    self.__id_producto=id_producto
    self.__nombre=nombre
    self.__descripcion=descripcion
    self.__precio=precio
    self.__stock=stock
    self.__categoria=categoria
  
  def __str__(self):
    cadena=self.__nombre+" "+str(round(self.__precio, 2))+" "+str(self.__stock)+"\n"+self.__descripcion+"\n"+self.__categoria
    return cadena
 
  @property
  def id_producto(self):
    return self.__id_producto
  @property
  def nombre(self):
    return self.__nombre
  @property
  def descripcion(self):
    return self.__descripcion
  @property
  def precio(self):
    return self.__precio
  @property
  def stock(self):
    return self.__stock
  @property
  def categoria(self):
    return self.__categoria
  
  @nombre.setter
  def nombre(self, nuevovalor):
    self.__nombre=nuevovalor
  @descripcion.setter
  def descripcion(self, nuevovalor):
    self.__descripcion=nuevovalor
  @precio.setter
  def precio(self, nuevovalor):
    self.__precio=nuevovalor
  @stock.setter
  def stock(self, nuevovalor):
    self.__stock=nuevovalor
  @categoria.setter
  def categoria(self, nuevovalor):
    self.__categoria=nuevovalor

  def insertar(self):
    datos=(self.__nombre,self.__descripcion,self.__precio,self.__stock, self.__categoria)
    conexion=Conexion("BaseDatos\superMarket.db")
    conexion.insert("INSERT INTO producto (nombre,descripcion,precio,stock,categoria) VALUES (?,?,?,?,?)", datos)

  def eliminar(self):
    conexion=Conexion("BaseDatos\superMarket.db")
    conexion.delete(f"DELETE FROM producto WHERE id_producto={self.__id_producto}")

  def modificar(self):
    datos=(self.nombre, self.descripcion, self.precio, self.stock,self.categoria, self.__id_producto)
    conexion=Conexion("BaseDatos\superMarket.db")
    conexion.update("UPDATE producto SET nombre=?, descripcion=?,precio=?, stock=?, categoria=?  WHERE id_producto=?", datos)
  
  def mostrar(self):
    conexion=Conexion("BaseDatos\superMarket.db")
    productos=conexion.read("SELECT * FROM producto")
    return productos
  
  def mostrarfiltrado(self):
    conexion=Conexion("BaseDatos\superMarket.db")
    productos=conexion.read(f"SELECT * FROM producto WHERE categoria='{self.categoria}'")
    return productos

  def mostrarbusqueda(self, nombre):
    conexion=Conexion("BaseDatos\superMarket.db")
    productos=conexion.read(f'SELECT * FROM producto WHERE nombre LIKE "{nombre}%"')
    return productos

  def modificarStock(self):
    datos=(self.stock, self.__id_producto)
    conexion=Conexion("BaseDatos\superMarket.db")
    conexion.update(f"UPDATE producto SET stock=stock-?  WHERE id_producto=?", datos)
  

#producto=Producto(25,"Aceite","",0,300,"") 
#producto.insert()
#producto.eliminar()
#producto.modificar()
#print(producto.mostrar())
#print(producto.mostrarfiltrado())
#producto.modificarStock() 
#print(producto.mostrarbusqueda("Aceite"))