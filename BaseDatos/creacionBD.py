import sqlite3 
from sqlite3 import Error
import tkinter as tk
from tkinter import messagebox

def creacionBD(db_file):
    conexion=None
    try:
        conexion=sqlite3.connect(db_file) 
    except Error as e:
        print(e)
    '''
    finally:
        if conexion:
            conexion.close()
    '''
    return conexion

def create_table(conexion, table_sql):
    """ create a table from the create_table_sql statement
    :param conexion: Connection object
    :param table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c=conexion.cursor()
        c.execute(table_sql)
        #messagebox.showinfo("BBDD", "Base de datos creada con exito")
    except Error as e:
        #messagebox.showwarning("Atencion !", "La base de datos ya existe")
        print(e)
    #conexion.close()


def main():
    database='BaseDatos\superMarket.db'

    create_producto_table = """ CREATE TABLE IF NOT EXISTS producto (
                                    id_producto INTEGER primary key autoincrement, 
                                    nombre TEXT, 
                                    descripcion TEXT, 
                                    precio_venta REAL, 
                                    stock INTEGER,
                                    categoria TEXT
                                ); """

    create_usuario_table = """CREATE TABLE IF NOT EXISTS usuario(
                                    id_usuario TEXT primary key,
                                    clave INTEGER ,
                                    tipo INTEGER DEFAULT 1,
                                    FOREIGN KEY (id_usuario) REFERENCES cliente(correo)
                                );"""

    create_cliente_table = """CREATE TABLE IF NOT EXISTS cliente(
                                    id_cliente INTEGER primary key autoincrement, 
                                    nombre TEXT,
                                    apellido TEXT, 
                                    dni INTEGER(8),
                                    id_direccion TEXT,
                                    correo TEXT,
                                    FOREIGN KEY (id_direccion) REFERENCES direccion(id_direccion)
                                );"""

    create_venta_table = """ CREATE TABLE IF NOT EXISTS venta(
                                    id_venta INTEGER primary key autoincrement, 
                                    fecha DATE, 
                                    id_cliente INTEGER, 
                                    FOREIGN KEY(id_cliente) REFERENCES cliente(id_cliente)
                                );"""

    create_carrito_table = """CREATE TABLE IF NOT EXISTS carrito(
                                    id_carrito INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                                    id_producto INTEGER,
                                    cantidad INTEGER,
                                    subTotal REAL, 
                                    FOREIGN KEY(id_producto) REFERENCES producto(id_producto)
                                );"""  

    create_direccion_table = """CREATE TABLE IF NOT EXISTS direccion(
                                    id_direccion INTEGER primary key autoincrement, 
                                    calle TEXT,
                                    altura INTEGER,
                                    localidad TEXT,
                                    provincia TEXT,
                                    codidoPostal TEXT
                                );"""


    # crear  coneccion a base de datos
    conexion=creacionBD(database)

    # create tables
    if conexion is not None:
        # create table
        create_table(conexion, create_producto_table)

        create_table(conexion, create_usuario_table)

        create_table(conexion, create_cliente_table)

        create_table(conexion, create_venta_table)

        create_table(conexion, create_detalle_venta_table)

        create_table(conexion, create_direccion_table)

        print("Base de Datos Creada")
        
    else:
        print("Error! No se puede crear la coneccion a la Base de Datos.")
    

if __name__ == '__main__':
    main() 

'''    
    def conexionBD(db_file):

        conexion=sqlite3.connect(db_file)
        cursor= conexion.cursor()
        try:
            cursor.execute("CREATE TABLE IF NOT EXISTS producto (id_producto INTEGER primary key autoincrement, nombre TEXT, descripcion TEXT, categoria TEXT,precio_venta REAL, stock INTEGER)");
            cursor.execute("CREATE TABLE IF NOT EXISTS usuario(id_usuario INTEGER primary key autoincrement, nombre_US TEXt, clave INTEGER, tipo INTEGER NOY NULL DEFAULT 1, FOREIGN KEY (nombre_US) REFERENCES cliente(correo),tipo INTEGER)");
            cursor.execute("CREATE TABLE IF NOT EXISTS cliente(id_cliente INTEGER primary key autoincrement, nombre TEXT,apellido TEXT, dni INTEGER(8),correo TEXT,FOREIGN KEY (direccion) REFERENCES direccion(id_direccion))");
            cursor.execute("CREATE TABLE IF NOT EXISTS venta(id_venta INTEGER primary key autoincrement, fecha DATE, id_cliente INTEGER, FOREIGN KEY(id_cliente) REFERENCES cliente(id_cliente))");
            cursor.execute("CREATE TABLE IF NOT EXISTS detalle_venta(id_venta INTEGER, cantidad INTEGER, id_producto INTEGER, FOREIGN KEY(id_venta) REFERENCES venta(id_venta), FOREIGN KEY(id_producto) REFERENCES producto(id_producto))");
            cursor.execute("CREATE TABLE IF NOT EXISTS direccion(id_direccion INTEGER primary key autoincrement, calle TEXT,altura INTEGER,localidad TEXT,provincia TEXT,codidoPostal TEXT)");

            messagebox.showinfo("BBDD", "Base de datos creada con exito")
        except:
            messagebox.showwarning("Atencion !", "La base de datos ya existe")
            
        conexion.close()

conexionBD('BaseDatos\superMarket.db')
'''