#!/usr/bin/env python



def get_task(user_id, week_number, ordered_tasks):
    
    """ Computes the task for a week for a specific user. 
    The week number is added to the user id, so that all users gets a new task each week. """

    number = user_id + week_number
    task_position = number % len(ordered_tasks)
    return ordered_tasks[task_position]



