
class Venta:
    def __init__(self, id_venta, detalle,fecha,total):
        self.__id_venta=id_venta
        self.__detalle=detalle
        self.__detalle=detalle
        self.__total=total

    def __str__(self):
        cadena=self.__id_venta+" "+"/n"+self.__detalle+" "+"/n"+self.fecha+" "+"/n"+self.__total
        return cadena
    
    @property
    def id_venta(self):
        return self.__id_venta
    @property
    def detalle(self):
        return self.__detalle
    @property
    def fecha(self):
        return self.__fecha
    @property
    def total(self):
        return self.__total

    @id_venta.setter
    def id_venta(self, nuevovalor):
        self.__id_venta=nuevovalor
    @detalle.setter
    def detalle(self, nuevovalor):
        self.__detalle=nuevovalor
    @fecha.setter
    def fecha(self, nuevovalor):
        self.__fecha=nuevovalor
    @total.setter
    def total(self, nuevovalor):
        self.__total=nuevovalor

    def insertarVenta(self): 
        datos=(self.detalle,self.fecha, self.total)
        conexion=Conexion("BaseDatos\superMarket.db")
        conexion.insert("INSERT INTO venta (detalle,fecha,total) VALUES (?,?,?)", datos)

    def eliminarVenta(self):
        conexion=Conexion("BaseDatos\superMarket.db")
        conexion.delete(f"DELETE FROM venta WHERE id_venta={self.__id_venta}")
    
    def vaciarVenta(self):
        conexion=Conexion("BaseDatos\superMarket.db")
        conexion.delete(f"DELETE FROM venta") 
        
    def consultaVenta(self):
        conexion=Conexion("BaseDatos\superMarket.db")
        datos=conexion.read(f"SELECT * FROM  WHERE id_venta={self.__id_venta}") 
        #print(datos)
        return datos[0][2], datos[0][3]
    
    def consutaCruzada(self):
        conexion=Conexion("BaseDatos\superMarket.db")
        datos=conexion.read(f"SELECT p.nombre,p.descripcion, p.precio_venta, c.cantidad, c.subTotal  FROM carrito AS c INNER JOIN detalle AS p USING (id_producto)") 
        return datos
    
    def precioCarrito(self):
        conexion=Conexion("BaseDatos\superMarket.db")
        dato=conexion.read(f"SELECT SUM ({self.total}) FROM carrito") 
        return dato[0][0]
    
