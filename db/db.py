#!/usr/bin/env python


#################################################
#        The Database Operator                  #
#################################################


import psycopg2
import configparser
from datetime import datetime

class DatabaseOperator:

    """This class is responsible for talking to the PSQL database. All queries go here."""

    def __init__(self, db_name, db_user):
        self.connect_args = "dbname=" + db_name + " user=" + db_user


    def _query_all(self, sql):
        
        """ Performs a query on a new connection and fetches all from the cursor """

        conn = psycopg2.connect(self.connect_args)
        cur = conn.cursor()
        cur.execute(sql)
        result = cur.fetchall()
        cur.close()
        conn.close()
        return result
    

    def get_all_users(self):
        
        """ Get all the users from the db """
        
        sql = "select * from users"
        return self._query_all(sql)
    

    def get_all_tasks(self):
        
        """ Get all the tasks from the db """
        
        sql = "select * from tasks;"
        return self._query_all(sql) 
       

    def complete_task(self, user_id, task_id, completed=datetime.now()):
        
        """ Marks a task as completed for a specific user and time """

        sql = "select complete_task(%s, %s, %s)"
        data = (user_id, task_id, completed)
        conn = psycopg2.connect(self.connect_args)
        cur = conn.cursor()
        cur.execute(sql, data)
        conn.commit()
        conn.close()


    def is_task_completed(self, user_id, task_id, completed_start, completed_end):
        
        """ Checks if a user has completed a specific task during a specified time """

        sql = """select exists 
            (select 1 from completed_tasks 
            where user_id = %s 
            and task_id = %s 
            and completed >= %s 
            and completed < %s)"""
        data = (user_id, task_id, completed_start, completed_end)
        conn = psycopg2.connect(self.connect_args)
        cur = conn.cursor()
        cur.execute(sql, data)
        result = cur.fetchone()
        conn.close()
        return result
