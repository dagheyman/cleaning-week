#!/usr/bin/env python

# This module is responsible for the application logic

import db

# This method returns the task for a user and for a specific week. 
def get_task(user_id, week_number):
    # First we get all the tasks in the database. These are sorted on id.
    all_tasks = db.get_all_tasks()
    # Then we add the week number to the user id. 
    # This way the number will be different by one each week.
    number = user_id + week_number
    # Then we use the modulus operator, to get the position of the task.
    task_position = number % len(all_tasks)
    return all_tasks[task_position]
   
