#Proyecto Iot - Assignment #1
#Authors: Alvaro Delgado Brenes, Felipe Guzman,
#Isaac Touma Rodriguez

import unittest
import DaoUser
import Database

class TestMyData(unittest.TestCase):
    """
        Simple demo de unit test case para DaoUser
    """
    db = Database.RelDatabase()
    users = DaoUser.DaoUsers(db)
    def setUp(self):
        self.users.insert('admin','admin')

    def test_users(self):
        self.users.select()

    def tearDown(self):
        self.users.delete('admin')

if __name__ == "__main__":
    unittest.main()