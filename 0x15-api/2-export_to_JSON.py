#!/usr/bin/python3
"""Exporting records of an employee into a josn
   format and presented it into a josn file
"""
import json
import requests
import sys


def main():
    USER_ID = sys.argv[1]
    url_user = f"https://jsonplaceholder.typicode.com/users/{USER_ID}"
    response_user = requests.get(url_user)
    users = response_user.json()
    USERNAME = users.get("username")
    url_todo = 'https://jsonplaceholder.typicode.com/todos'
    params = {'userId': USER_ID}
    response = requests.get(url_todo, params=params)

    if response.status_code == 200:
        todos = response.json()

    to_list = []
    for i in todos:
        COMPLETED = i.get("completed")
        TASK = i.get("title")
        usr_dict = {"task": TASK, "completed": COMPLETED, "username": USERNAME}
        to_list.append(usr_dict)

    to_dict = {USER_ID: to_list}
    filename = f"{USER_ID}.json"
    with open(filename, 'w') as f:
        json.dump(to_dict, f)


if __name__ == '__main__':
    main()
