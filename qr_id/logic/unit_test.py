# Proyecto Iot - Assignment #1
# Authors: Alvaro Delgado Brenes, Felipe Guzman,
# Isaac Touma Rodriguez

import Database
import Dao
import unittest


class TestMethods(unittest.TestCase):

    def setUp(self):
        self.db = Database.RelDatabase()
        self.daoUser = Dao.Dao(self.db)

    def testOperations(self):
        self.daoUser.insert('Usuario', Username='admin1', Password='admin123')
        self.daoUser.insert('Usuario', Username='admin2', Password='admin456')
        conditional_query = 'username = %s '

        self.assertEqual('admin1',
                         self.daoUser.select('usuario', conditional_query, '*', username='admin1')[0][0])
        self.assertEqual('admin123',
                         self.daoUser.select('usuario', conditional_query, '*', username='admin1')[0][1])

        self.assertEqual('admin2',
                         self.daoUser.select('usuario', conditional_query, '*', username='admin2')[0][0])
        self.assertEqual('admin456',
                         self.daoUser.select('usuario', conditional_query, '*', username='admin2')[0][1])

        self.daoUser.update('Usuario', conditional_query, 'admin1', Password='ADMIN123')
        self.daoUser.update('Usuario', conditional_query, 'admin2', Password='ADMIN456')

        self.assertEqual('ADMIN123',
                         self.daoUser.select('usuario', conditional_query, '*', username='admin1')[0][1])

        self.assertEqual('ADMIN456',
                         self.daoUser.select('usuario', conditional_query, '*', username='admin2')[0][1])

        self.daoUser.delete('Usuario', conditional_query, 'admin1')
        self.daoUser.delete('Usuario', conditional_query, 'admin2')

        self.assertEqual([], self.daoUser.select('usuario', conditional_query, '*', username='admin1'))
        self.assertEqual([], self.daoUser.select('usuario', conditional_query, '*', username='admin2'))

    def tearDown(self):
        self.db.db_connection.close()


if __name__ == '__main__':
    unittest.main()
