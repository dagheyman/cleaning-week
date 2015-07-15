#!/usr/bin/env python

#################################################
#                Web API                        #
#################################################


from bottle import route, run, error, response
from isoweek import Week
from datetime import date
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


@route('/api/task/<year:int>/<week_number:int>/<user_id:int>')
def get_tasks_for_week(year, week_number, user_id):

    """ Get the task for a user for a week, with completion status. """
    
    if not _user_exists(user_id):
        response.status = 404
        return "Invalid user id."
   
    if (week_number < 1 or week_number > 53):
        response.status = 500
        return "Invalid week number."

    tasks = _db.get_all_tasks()
    task = _get_task(user_id, week_number, tasks)
    week = Week(year, week_number)
    monday = week.monday().isoformat()
    sunday = week.sunday().isoformat()
    completed = _db.is_task_completed(user_id, task[0], monday, sunday)
   
    task_with_status = {
                            "task": {
                                "id": task[0], 
                                "title": task[1], 
                                "description": task[2], 
                                "status": str(completed[0])
                            }
                       }    
   
    return _json(task_with_status)



#########################################
#       Error handling                  #
#########################################


@error(500)
def error500(error):
    response.status = 500
    return "Something went wrong."


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



