#!/usr/bin/env python

#################################################
#                Web API                        #
#################################################


from bottle import route, get, post, run, error, response, request
from isoweek import Week
from datetime import date
import json


#########################################
#       API methods                     #
#########################################


@get('/api/tasks')
def get_all_tasks():
    
    """ Get all available tasks """
    
    return _json(_db.get_all_tasks())
  

@get('/api/users')
def get_all_users():

    """ Get all available users """

    return _json(_db.get_all_users())


@get('/api/tasks/<user_id:int>')
def get_task_for_current_week(user_id):
    
    if not _user_exists(user_id):
        response.status = 404
        return _json("Invalid user id.")

    return _get_task_for_week(date.today().year, date.today().isocalendar()[1], user_id)


@post('/api/tasks/<user_id:int>/<task_id:int>/complete')
def complete_task(user_id, task_id):

    """ Complete a task for a specific user for the current week """

    if not _user_exists(user_id):
        response.status = 404
        return "Invalid user id."
   
    if not _task_exists(task_id):
        response.status = 404
        return "Invalid task id."

    if _task_completed(user_id, task_id, date.today().year, date.today().isocalendar()[1]):
        response.status = 403
        return "Task already completed."

    _db.complete_task(user_id, task_id)
    return _json("Task completed.")


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

def _get_task_for_week(year, week_number, user_id):

    """ Get the task for a user for a week, with completion status. """
    
    if not _user_exists(user_id):
        response.status = 404
        return _json("Invalid user id.")
   
    if not _valid_week(week_number):
        response.status = 500
        return _json("Invalid week number.")

    task = _get_task(user_id, week_number, _db.get_all_tasks())
   
    task_with_status = {
                            "task": {
                                "id": task[0], 
                                "title": task[1], 
                                "description": task[2], 
                                "status": _task_completed(user_id, task[0], year, week_number)
                            }
                       }    
   
    return _json(task_with_status)


def _get_task(user_id, week_number, ordered_tasks):

    """ Get the task for a week for a specific user. 
        The week number is added to the user id, 
        so that all users will get a new task each week. """

    number = user_id + week_number
    task_position = number % len(ordered_tasks) 
    return ordered_tasks[task_position]


def _user_exists(user_id):

    """ Return true if a user id exists in the db. """

    for user in _db.get_all_users():
        if user_id == user[0]:
            return True
    return False


def _task_exists(task_id):

    """ Return true if a task id exists in the db. """

    for task in _db.get_all_tasks():
        if task_id == task[0]:
            return True
    return False


def _valid_week(week_number):

    """ Check that an int is a valid week number """
    
    return (week_number > 0) and (week_number < 54)


def _task_completed(user_id, task_id, year, week_number):
    
    """ Return true if a task is completed for this specific user and week """
    
    week = Week(year, week_number)
    monday = week.monday().isoformat()
    sunday = week.sunday().isoformat()
    return _db.is_task_completed(user_id, task_id, monday, sunday)
                

def _json(data):
    
    """ Convert the response to JSON and set encoding to UTF-8. """

    return json.dumps(data, ensure_ascii=False).encode('utf8')


def start(db, host, port, debug):
    
    """ Start the server """
    
    global _db 
    _db = db
    run(host=host, port=port, debug=debug)



