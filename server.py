#!/usr/bin/env python

#################################################
#                Web API                        #
#################################################

from db import db
from bottle import route, run
import json
import configparser

######## Configuration #############

config = configparser.ConfigParser()
config.read("conf/conf.ini")
db_name = config.get("ConfigSection", "db_name")
db_user = config.get("ConfigSection", "db_user")
_db = db.DatabaseOperator(db_name, db_user)



@route('/api/tasks')
def get_all_tasks():
    return _json(_db.get_all_tasks())
  

@route('/api/users')
def get_all_users():
    return _json(_db.get_all_users())


def _json(data):
    return json.dumps(data, ensure_ascii=False).encode('utf8')



######## Run server ################

run(host='localhost', port=9090, debug=True)



