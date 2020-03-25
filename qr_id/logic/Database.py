#Proyecto Iot - Assignment #1
#Authors: Alvaro Delgado Brenes, Felipe Guzman,
#Isaac Touma Rodriguez

import mysql.connector


class RelDatabase:
  """
    Class that establishes a connection to a MySQL database
  """
  def __init__(self):
    self.db_connection = mysql.connector.connect(
      host="127.0.0.1",
      user="root",
      passwd="root",
      database="Users"
    )
    self.my_database = self.db_connection.cursor()
  def getConnection(self):  
    return self.db_connection
  def getCursor(self):
    return self.my_database

