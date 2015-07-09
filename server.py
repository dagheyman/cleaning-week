#!/usr/bin/env python

#################################################
#                Web API                        #
#################################################

from bottle import route, run
import json


####### API methods #####################

@route('/api/tasks')
def get_all_tasks():
    return _json(_db.get_all_tasks())
  

@route('/api/users')
def get_all_users():
    return _json(_db.get_all_users())



####### Util methods #####################

def _json(data):
    return json.dumps(data, ensure_ascii=False).encode('utf8')


def start(db, host, port, debug):
    """ Start the server """
    global _db 
    _db = db
    run(host=host, port=port, debug=debug)



