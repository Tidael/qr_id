#Proyecto Iot - Assignment #1
#Authors: Alvaro Delgado Brenes, Felipe Guzman,
#Isaac Touma Rodriguez

import Database

class DaoUsers:
    """
        Testing Data Access Object  of a User Table in the database
    """
    def __init__(self,db):
        self.db = db

    #CRUD operations

    #Inserting register into usuario
    def insert(self,username, password):
        sql_statement = "INSERT INTO usuario (username,password) values(%s,%s)"
        values = (username,password)
        self.db.getCursor().execute(sql_statement,values)
        self.db.getConnection().commit()
    
    #selecting all registers from usuario
    
    def select(self): 
        sql_statement = "SELECT * FROM usuario"
        self.db.my_database.execute(sql_statement)
        output = self.db.my_database.fetchall()
        for x in output:
            print(x)
    
    #updating register from usuario

    def update(self,password,username):
        sql_statement = "UPDATE usuario SET password= %s where username= %s"
        data = (password, username)
        self.db.my_database.execute(sql_statement,data)
        self.db.db_connection.commit()
    
    #Deleting register from usuario

    def delete(self,username):        
        sql_query = "DELETE FROM usuario where username= %s"
        data = (username,)
        self.db.my_database.execute(sql_query,data)
        self.db.db_connection.commit()
        print("Row(s) deleted successfully")
















