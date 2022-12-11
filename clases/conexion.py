import sqlite3
from sqlite3 import Error


class Conexion:
  def __init__(self, bd):
    self.__bd=bd
    self.__conexion=""
    self.__cursor=""

  def insert(self,consulta,datos):
    try:
      self.__conexion=sqlite3.connect(self.__bd)
      self.__cursor=self.__conexion.cursor()
      self.__cursor.execute(consulta,datos)
      self.__conexion.commit()
      self.__conexion.close()
    except Error as e:
      print(e)

  def read(self,consulta):
    datos=None
    try:
      self.__conexion=sqlite3.connect(self.__bd)
      self.__cursor=self.__conexion.cursor()
      self.__cursor.execute(consulta)
      datos=self.__cursor.fetchall()
      self.__conexion.close()
    except Error as e:
      print(e)
    return datos

  def delete(self,consulta):
    try:
      self.__conexion=sqlite3.connect(self.__bd)
      self.__cursor=self.__conexion.cursor()
      self.__cursor.execute(consulta)
      self.__conexion.commit()
      self.__conexion.close()
    except Error as e:
      print(e)

  def update(self,consulta, datos):
    try:
      self.__conexion=sqlite3.connect(self.__bd)
      self.__cursor=self.__conexion.cursor()
      self.__cursor.execute(consulta,datos)
      self.__conexion.commit()
      self.__conexion.close()
    except Error as e:
      print(e)
