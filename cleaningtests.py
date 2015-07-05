#!/usr/bin/env python

import unittest
import cleaning

class Test(unittest.TestCase):

    """ Unit tests for the application logic """

    @classmethod
    def setUpClass(self):
        self.tasks = ['task1', 'task2', 'task3']

    def test_week_one_user_one(self):
        task = cleaning.get_task(1, 1, self.tasks)
        self.assertTrue('task3' == task)
    
    def test_week_two_user_one(self):
        task = cleaning.get_task(1, 2, self.tasks)
        self.assertTrue('task1' == task)
      
    @classmethod
    def tearDownClass(self):
        pass

if __name__ == '__main__':
    unittest.main()
