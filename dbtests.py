#!/usr/bin/env python

# Integration tests

import unittest
from subprocess import call, DEVNULL
import configparser

# Load configs
config = configparser.ConfigParser()
config.read("./conf.ini")
test_db_name = config.get("ConfigSection", "test_db_name")


class Test(unittest.TestCase):
    
    @classmethod
    def setUpClass(self):
        """ Create a test DB and populate with data """
        call(["createdb", test_db_name])
        call(["psql", "-d", test_db_name, "-f", "sql/create_tables.sql", "-q"]) 
        call(["psql", "-d", test_db_name, "-f", "sql/functions.sql", "-q"])
        call(["psql", "-d", test_db_name, "-f", "sql/populate_test_db.sql", "-q"], stdout=DEVNULL)


    def testOne(self):
        self.assertTrue(True);
    @classmethod
    def tearDownClass(self): 
        """ Drop the test DB """
        call(["dropdb", test_db_name])

if __name__ == '__main__':
    unittest.main()
