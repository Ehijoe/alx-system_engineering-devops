#!/usr/bin/python3
''' gather data from an API '''
import json
import requests
from sys import argv

if __name__ == '__main__':
    # get employee response [used to get name in line 19]
    endpoint = 'https://jsonplaceholder.typicode.com'
    user_res = requests.get(endpoint + '/users/').json()

    result = {}
    for user in user_res:
        user_id = str(user.get('id'))
        todos = requests.get(
            endpoint + '/todos?userId=' + user_id
        ).json()

        result[user_id] = [{
            "username": user.get('username'),
            "task": task.get('title'),
            "completed": task.get('completed'),
        } for task in todos]

    with open("todo_all_employees.json", "w") as outfile:
        json.dump(result, outfile)
