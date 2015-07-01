#!/usr/bin/env python

# This module is responsible for talking to the PSQL database. All queries go here.

import psycopg2
import configparser

# Load configs
config = configparser.ConfigParser()
config.read("./conf.ini")
db_name = config.get("ConfigSection", "db_name")
db_user = config.get("ConfigSection", "db_user")


# Get all the users in the db
def get_all_users():
    conn = psycopg2.connect("dbname=" + db_name + " user=" + db_user)
    cur = conn.cursor()
    cur.execute("select * from users;")
    users = cur.fetchall()
    cur.close()
    conn.commit()
    conn.close()
    return users;


# Get all the tasks in the db
def get_all_tasks():
    conn = psycopg2.connect("dbname=" + db_name + " user=" + db_user)
    cur = conn.cursor()
    cur.execute("select * from tasks;")
    tasks = cur.fetchall()
    cur.close()
    conn.commit()
    conn.close()
    return tasks;


if __name__ == "__main__":
        print(get_all_users())
        print(get_all_tasks())
