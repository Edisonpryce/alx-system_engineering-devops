#!/usr/bin/python3
"""For a gien employee id return
    their todo list progress
"""

import requests
import sys


def main():
    userid = sys.argv[1]
    url_usr = f"https://jsonplaceholder.typicode.com/users/{userid}"
    response_usr = requests.get(url_usr)
    users = response_usr.json()
    EMPLOYEE_NAME = users.get("name")

    url_todo = 'https://jsonplaceholder.typicode.com/todos'
    params = {'userId': userid}

    response = requests.get(url_todo, params=params)

    if response.status_code == 200:
        todos = response.json()

# Iterating the todo list
    NUMBER_OF_DONE_TASKS = 0
    TOTAL_NUMBER_OF_TASKS = 0
    TASK_TITLE = []
    for i in todos:
        if isinstance(i, dict):
            TOTAL_NUMBER_OF_TASKS += 1
        if i.get("completed") is True:
            NUMBER_OF_DONE_TASKS += 1
            TASK_TITLE.append(i.get("title"))
    print(f"Employee {EMPLOYEE_NAME} is done with tasks(\
            {NUMBER_OF_DONE_TASKS}/{TOTAL_NUMBER_OF_TASKS}):")
    for i in TASK_TITLE:
        print('\t ' + i)


if __name__ == '__main__':
    main()
