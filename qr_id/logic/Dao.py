# Proyecto Iot - Assignment #1
# Authors: Alvaro Delgado Brenes, Felipe Guzman,
# Isaac Touma Rodriguez


class Dao(object):
    """
        Generic Data Access Object 
    """

    def __init__(self, database):
        self.db = database

    def select(self, table, where=None, *args, **kwargs):
        result = None
        query = 'SELECT '
        keys = args
        values = tuple(kwargs.values())
        l = len(keys) - 1

        for i, key in enumerate(keys):
            query += key + " "
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
            result = [item for item in self.db.my_database.fetchall()]
        return result

    def insert(self, table, *args, **kwargs):
        values = None
        query = "INSERT INTO %s " % table
        if kwargs:
            keys = kwargs.keys()
            values = tuple(kwargs.values())
            query += "(" + ",".join(["`%s`"] * len(keys)) % tuple(keys) + ") VALUES (" + ",".join(
                ["%s"] * len(values)) + ")"
        elif args:
            values = args
            query += " VALUES(" + ",".join(["%s"] * len(values)) + ")"

        self.db.my_database.execute(query, values)
        self.db.db_connection.commit()
        return self.db.my_database.lastrowid

    def update(self, table, where=None, *args, **kwargs):
        query = "UPDATE %s SET " % table
        keys = kwargs.keys()
        values = tuple(kwargs.values()) + tuple(args)
        l = len(keys) - 1
        for i, key in enumerate(keys):
            query += "`" + key + "` = %s"
            if i < l:
                query += ","

        query += " WHERE %s" % where

        self.db.my_database.execute(query, values)
        self.db.db_connection.commit()

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
