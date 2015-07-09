#!/usr/bin/env python

#################################################
#                Start the server               #
#################################################

from db import db
import configparser
import server

######## Configuration #############

config = configparser.ConfigParser()
config.read("conf/conf.ini")
db_name = config.get("ConfigSection", "db_name")
db_user = config.get("ConfigSection", "db_user")
db = db.DatabaseOperator(db_name, db_user)

server.start(db, 'localhost', 8080, True)

