#!/usr/bin/env python


import psycopg2
import configparser

# Load configs
#config = configparser.ConfigParser()
#config.read("./conf.ini")
#db_name = config.get("ConfigSection", "db_name")
#db_user = config.get("ConfigSection", "db_user")

class DatabaseOperator:

    """This class is responsible for talking to the PSQL database. All queries go here."""

    def __init__(self, db_name, db_user):
        self.db_name = db_name
        self.db_user = db_user

    # Get all the users in the db
    def get_all_users(self):
        conn = psycopg2.connect("dbname=" + self.db_name + " user=" + self.db_user)
        cur = conn.cursor()
        cur.execute("select * from users;")
        users = cur.fetchall()
        cur.close()
        conn.commit()
        conn.close()
        return users;


    # Get all the tasks in the db
    def get_all_tasks(self):
        conn = psycopg2.connect("dbname=" + self.db_name + " user=" + self.db_user)
        cur = conn.cursor()
        cur.execute("select * from tasks;")
        tasks = cur.fetchall()
        cur.close()
        conn.commit()
        conn.close()
        return tasks;


if __name__ == "__main__":
        db = DatabaseOperator(db_name, db_user)
        print(db.get_all_users())
        print(db.get_all_tasks())
