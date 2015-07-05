#!/usr/bin/env python


import psycopg2
import configparser

class DatabaseOperator:

    """This class is responsible for talking to the PSQL database. All queries go here."""

    def __init__(self, db_name, db_user):
        self.db_name = db_name
        self.db_user = db_user


    def query_all(self, sql):
        
        """ Performs a query on a new connection and fetches all from the cursor """

        conn = psycopg2.connect("dbname=" + self.db_name + " user=" + self.db_user)
        cur = conn.cursor()
        cur.execute(sql)
        result = cur.fetchall()
        cur.close()
        conn.close()
        return result
    

    def get_all_users(self):
        
        """ Get all the users from the db """
        
        sql = "select * from users"
        return self.query_all(sql)
    

    def get_all_tasks(self):
        
        """ Get all the tasks from the db """
        
        sql = "select * from tasks;"
        return self.query_all(sql) 
        
    
       
