from pathlib import Path
import sys
sys.path.append(str(Path(__file__).parent.parent))
from clases.conexion import Conexion

class Venta:
    def __init__(self, id_venta,fecha,cliente):
        self.__id_venta=id_venta
        self.__fecha=fecha
        self.__cliente=cliente
        

    def __str__(self):
        cadena=self.__id_venta+" "+"/n"+self.__fecha+" "+"/n"+self.__clientea
        return cadena
    
    @property
    def id_venta(self):
        return self.__id_venta
    @property
    def fecha(self):
        return self.__fecha
    @property
    def cliente(self):
        return self.__cliente


    @id_venta.setter
    def id_venta(self, nuevovalor):
        self.__id_venta=nuevovalor
    @fecha.setter
    def fecha(self, nuevovalor):
        self.__fecha=nuevovalor
    @cliente.setter
    def cliente(self, nuevovalor):
        self.__cliente=nuevovalor


    def insertarVenta(self): 
        datos=(self.fecha,self.cliente)
        conexion=Conexion("BaseDatos\superMarket.db")
        id=conexion.insert("INSERT INTO venta (fecha, id_cliente) VALUES (?,?)", datos)
        self.id_venta=id
        

    def consultaVenta(self):
        conexion=Conexion("BaseDatos\superMarket.db")
        datos=conexion.read(f"SELECT * FROM  WHERE id_venta={self.id_venta}") 
        return datos[0][1], datos[0][2]

    
    def consutaFactura(self):
        conexion=Conexion("BaseDatos\superMarket.db")
        datos=conexion.read(f"SELECT p.descripcion, dv.cantidad , dv.precioVenta,dv.cantidad *dv.precioVenta AS SubTotal, dv.id_venta, v.fecha, c.nombre ||' '||c.apellido AS Cliente FROM detalleVenta dv CROSS JOIN producto p ON p.id_producto =dv.id_producto CROSS JOIN venta  v ON v.id_venta =dv.id_venta CROSS JOIN cliente c ON c.id_cliente =v.id_cliente WHERE v.id_venta={self.id_venta} AND c.id_cliente={self.cliente}") 
        return datos
    
    def calculoTotal(self):
        conexion=Conexion("BaseDatos\superMarket.db")
        datos=conexion.read(f"SELECT SUM(dv.cantidad * dv.precioVenta) FROM venta v JOIN detalleVenta dv ON v.id_venta  = dv.id_venta WHERE v.id_cliente={self.cliente} AND v.id_venta={self.id_venta}") 
        return datos[0][0]
    
    def consultaUltimaVenta(self):
        conexion=Conexion("BaseDatos\superMarket.db")
        dato=conexion.read(f"SELECT id_venta FROM venta ORDER BY id_venta DESC LIMIT 1") #Trae el ultimo ID
        return dato[0][0]+1
    
    '''No Van
    def ingresarFecha(self):
        conexion=Conexion("BaseDatos\superMarket.db")
        conexion.read(f"UPDATE venta SET fecha=(DATE('now')) WHERE id_venta ={self.id_venta})") 
    '''
#v=Venta(1,2,2)
#datos=v.consutaFactura()
#print(datos[0][6])
#print(v.calculoTotal())