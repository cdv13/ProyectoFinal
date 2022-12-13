from conexion import Conexion

class CarritoCompra():
  def __init__(self, id_carrito, producto,cantidad, subTotal):
    self.__id_carrito=id_carrito
    self.__producto=producto
    self.__cantidad=cantidad
    self.__subTotal=subTotal

  def __str__(self):
    cadena=self.__id_venta+" "+"/n"+self.__producto+" "+"/n"+self.cantidad+" "+"/n"+self.__subTotal
    return cadena
  
  @property
  def id_venta(self):
    return self.__id_venta
  @property
  def producto(self):
    return self.__producto
  @property
  def cantidad(self):
    return self.__cantidad
  @property
  def subTotal(self):
    return self.__subTotal

  @id_venta.setter
  def id_venta(self, nuevovalor):
    self.__id_venta=nuevovalor
  @producto.setter
  def producto(self, nuevovalor):
    self.__producto=nuevovalor
  @cantidad.setter
  def cantidad(self, nuevovalor):
    self.__cantidad=nuevovalor
  @subTotal.setter
  def subTotal(self, nuevovalor):
    self.__subTotal=nuevovalor

  def insertarCarrito(self): 
    datos=(self.producto,self.cantidad, self.subTotal)
    conexion=Conexion("BaseDatos\superMarket.db")
    conexion.insert("INSERT INTO carrito (id_producto,cantidad,subTotal) VALUES (?,?,?)", datos)

  def eliminarPCarrito(self):
    conexion=Conexion("BaseDatos\superMarket.db")
    conexion.delete(f"DELETE FROM carrito WHERE id_carrito={self.__id_carrito}")
  
  def vaciarCarrito(self):
    conexion=Conexion("BaseDatos\superMarket.db")
    conexion.delete(f"DELETE FROM carrito") 
    
  def consultaCarrito(self):
    conexion=Conexion("BaseDatos\superMarket.db")
    datos=conexion.read(f"SELECT * FROM carrito WHERE id_carrito={self.__id_carrito}") 
    #print(datos)
    return datos[0][2], datos[0][3]
  
  def consutaCruzada(self):
    conexion=Conexion("BaseDatos\superMarket.db")
    datos=conexion.read(f"SELECT p.id_producto, p.nombre,p.descripcion, p.precio_venta, c.cantidad , c.subTotal  FROM carrito AS c INNER JOIN producto AS p USING (id_producto)") 
    return datos
  
  def precioCarrito(self):
    conexion=Conexion("BaseDatos\superMarket.db")
    dato=conexion.read(f"SELECT SUM (subTotal) FROM carrito") 
    return dato[0][0]

  def sumaProductos(self):
    conexion=Conexion("BaseDatos\superMarket.db")
    dato=conexion.read(f"SELECT SUM (cantidad) FROM carrito") 
    return dato[0][0]


carrito=CarritoCompra(0,0,0,0)
#carrito.insertarCarrito()
#carrito.eliminarPCarrito()
#print(carrito.consultaCarrito())
#print(carrito.precioCarrito())
print(carrito.consutaCruzada())