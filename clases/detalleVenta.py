from pathlib import Path
import sys
sys.path.append(str(Path(__file__).parent.parent))
from clases.conexion import Conexion

class DetalleVenta():
  def __init__(self, id_detalleVenta, venta, producto,cantidad, precioVenta):
    self.__id_detalleVenta=id_detalleVenta
    self.__venta=venta
    self.__producto=producto
    self.__cantidad=cantidad
    self.__precioVenta=precioVenta
    

  def __str__(self):
    cadena=self.__id_detalleVenta+" "+"/n"+self.__venta+" "+"/n"+self.__producto+" "+"/n"+self.__cantidad+" "+"/n"+self.__precioVenta
    return cadena
  
  @property
  def id_detalleVenta(self):
    return self.__id_detalleVenta
  @property
  def venta(self):
    return self.__venta
  @property
  def producto(self):
    return self.__producto
  @property
  def cantidad(self):
    return self.__cantidad
  @property
  def precioVenta(self):
    return self.__precioVenta

  @id_detalleVenta.setter
  def id_detalleVenta(self, nuevovalor):
    self.__id_detalleVenta=nuevovalor
  @venta.setter
  def venta(self, nuevovalor):
    self.__venta=nuevovalor  
  @producto.setter
  def producto(self, nuevovalor):
    self.__producto=nuevovalor
  @cantidad.setter
  def cantidad(self, nuevovalor):
    self.__cantidad=nuevovalor
  @precioVenta.setter
  def precioVenta(self, nuevovalor):
    self.__precioVenta=nuevovalor    


  def insertarDV(self): 
    datos=(self.venta,self.producto,self.cantidad,self.precioVenta)
    conexion=Conexion("BaseDatos\superMarket.db")
    conexion.insert("INSERT INTO detalleVenta (id_venta, id_producto,cantidad,precioVenta) VALUES (?,?,?,?)", datos)
  
  def consultaDV(self):
    conexion=Conexion("BaseDatos\superMarket.db")
    datos=conexion.read(f"SELECT * FROM detalleVenta WHERE id_detalleVenta={self.__id_detalleVenta}") 
    return datos[0][3]
  
  def consutaCruzada(self):
    conexion=Conexion("BaseDatos\superMarket.db")
    datos=conexion.read(f"SELECT p.id_producto, p.nombre,p.descripcion, p.precio_venta, c.cantidad  FROM detalleVenta AS dv INNER JOIN producto AS p USING (id_producto)") 
    return datos
  
  def precioTotal(self):
    conexion=Conexion("BaseDatos\superMarket.db")
    dato=conexion.read(f"SELECT p.precio * dv.cantidad  AS total FROM detalleVenta AS dv INNER JOIN producto AS p USING (id_producto)") 
    return dato[0][0]
  

#carrito=CarritoCompra(0,0,0,0)
#carrito.insertarCarrito()
#carrito.eliminarPCarrito()
#print(carrito.consultaCarrito())
#print(carrito.precioTotal())
#print(carrito.consutaCruzada())