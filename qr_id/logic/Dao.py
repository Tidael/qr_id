#Proyecto Iot - Assignment #1
#Authors: Alvaro Delgado Brenes, Felipe Guzman,
#Isaac Touma Rodriguez

import Database

class Dao(object):
    """
        Data Access Object 
    """
    def __init__(self,db):
        self.db = db

    def select(self, table, where=None, *args, **kwargs):
        result = None
        query = 'SELECT '
        keys = args
        values = tuple(kwargs.values())
        l = len(keys) - 1

        for i, key in enumerate(keys):
            query += "`"+key+"`"
            if i < l:
                query += ","
        

        query += 'FROM %s' % table

        if where:
            query += " WHERE %s" % where
        

        self.db.my_database.execute(query, values)
        number_rows = self.db.my_database.rowcount
        number_columns = len(self.db.my_database.description)

        if number_rows >= 1 and number_columns > 1:
            result = [item for item in self.db.my_database.fetchall()]
        else:
            result = [item[0] for item in self.db.my_database.fetchall()]

        return result

    def insert(self, table, *args, **kwargs):
        values = None
        query = "INSERT INTO %s " % table
        if kwargs:
            keys = kwargs.keys()
            values = tuple(kwargs.values())
            query += "(" + ",".join(["`%s`"] * len(keys)) %  tuple (keys) + ") VALUES (" + ",".join(["%s"]*len(values)) + ")"
        elif args:
            values = args
            query += " VALUES(" + ",".join(["%s"]*len(values)) + ")"

        self.db.my_database.execute(query, values)
        self.db.db_connection.commit()
        return self.db.my_database.lastrowid

    def update(self, table, where=None, *args, **kwargs):
        query  = "UPDATE %s SET " % table
        keys   = kwargs.keys()
        values = tuple(kwargs.values()) + tuple(args)
        l = len(keys) - 1
        for i, key in enumerate(keys):
            query += "`"+key+"` = %s"
            if i < l:
                query += ","
            ## End if i less than 1
        ## End for keys
        query += " WHERE %s" % where


        self.db.my_database.execute(query, values)
        self.db.db_connection.commit()

        # Obtain rows affected
        update_rows = self.db.my_database.rowcount
 
        return update_rows
    
    def delete(self, table, where=None, *args):
        query = "DELETE FROM %s" % table
        if where:
            query += ' WHERE %s' % where

        values = tuple(args)

        self.db.my_database.execute(query, values)
        self.db.db_connection.commit()

        delete_rows = self.db.my_database.rowcount

        return delete_rows


db = Database.RelDatabase()
daoUser = Dao(db)
conditional_query = 'username = %s '
print(daoUser.select('usuario',conditional_query,'Password',username = 'admin'))

daoUser.insert('Usuario',Username = 'admin2',Password='admin456')
daoUser.update('Usuario',conditional_query,'admin',Password='ADMIN123')
daoUser.delete('Usuario',conditional_query,'admin2')









