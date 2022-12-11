import conexion

class Carrito():
  def __init__(self, id_venta, productos):
    self.__id_venta=id_venta
    self.__productos=[]

  def __str__(self):
    cadena=self.__id_venta+" "+"/n"+self.__productos
    return cadena
  
  @property
  def id_venta(self):
    return self.__id_venta
  @property
  def productos(self):
    return self.__productos

  @id_venta.setter
  def id_venta(self, nuevovalor):
    self.__id_venta=nuevovalor
  @productos.setter
  def productos(self, nuevovalor):
    self.__productos=nuevovalor

  def agregarProducto(self): 
    insetrar()
    self.__productos.append()
    pass
      
  def quitarProducto(self):
    delet()
    self.__producto.remove()
    pass