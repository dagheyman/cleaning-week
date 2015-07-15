#!/usr/bin/env python

#################################################
#                Web API                        #
#################################################


from bottle import route, run, error, response
import json


#########################################
#       API methods                     #
#########################################


@route('/api/tasks')
def get_all_tasks():
    return _json(_db.get_all_tasks())
  

@route('/api/users')
def get_all_users():
    return _json(_db.get_all_users())


@route('/api/tasks/week/<week_number>/user/<user_id>')
def get_tasks_for_week(week_number, user_id):
    if not _user_exists(int(user_id)):
        response.status = 404
        return "No such user."

    tasks = _db.get_all_tasks()
    return _json(_get_task(int(user_id), int(week_number), tasks))

@error(500)
def error500(error):
    response.status = 500
    return "Something went wrong"

@error(404)
def error404(error):
    response.status = 404
    return "Nothing here."

#########################################
#       Private methods                 #
#########################################

def _get_task(user_id, week_number, ordered_tasks):

    """ Computes the task for a week for a specific user. 
        The week number is added to the user id, 
        so that all users gets a new task each week. """

    number = user_id + week_number
    task_position = number % len(ordered_tasks) 
    return ordered_tasks[task_position]


def _user_exists(user_id):

    """ Returns true if a user id exists in the db. """

    for user in _db.get_all_users():
        if user_id == user[0]:
            return True
    return False


def _json(data):
    
    """ Convert the response to JSON and set encoding to UTF-8. """

    return json.dumps(data, ensure_ascii=False).encode('utf8')


def start(db, host, port, debug):
    
    """ Start the server """
    
    global _db 
    _db = db
    run(host=host, port=port, debug=debug)



