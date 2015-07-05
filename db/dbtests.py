#!/usr/bin/env python

#################################################
#        Integration tests                      #
#################################################

import unittest
from subprocess import call, DEVNULL
import configparser
import db

class Test(unittest.TestCase):
    
    @classmethod
    def setUpClass(self):
        
        """ Creates and populates a testing DB to be used in the integration tests. """
        
        config = configparser.ConfigParser()
        config.read("../conf/conf.ini")
        self.test_db_name = config.get("ConfigSection", "test_db_name")
        self.test_db_user = config.get("ConfigSection", "test_db_user")
        call(["createdb", self.test_db_name])
        call(["psql", "-d", self.test_db_name, "-f", "../sql/create_tables.sql", "-q"]) 
        call(["psql", "-d", self.test_db_name, "-f", "../sql/functions.sql", "-q"])
        call(["psql", "-d", self.test_db_name, "-f", "../sql/populate_test_db.sql", "-q"], stdout=DEVNULL)
        self.db = db.DatabaseOperator(self.test_db_name, self.test_db_user)

    
    def test_4_users_in_db(self):
        users = self.db.get_all_users()
        self.assertTrue(len(users) == 4);
    
    def test_4_tasks_in_db(self):
        tasks = self.db.get_all_tasks()
        self.assertTrue(len(tasks) == 4);
    
    
    @classmethod
    def tearDownClass(self): 
        """ Drop the test DB """
        call(["dropdb", self.test_db_name])

if __name__ == '__main__':
    unittest.main()
