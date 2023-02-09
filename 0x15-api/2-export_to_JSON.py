#!/usr/bin/python3
''' gather data from an API '''
import json
import requests
from sys import argv

if __name__ == '__main__':
    # get employee response [used to get name in line 19]
    endpoint = 'https://jsonplaceholder.typicode.com'
    user_res = requests.get(endpoint + '/users/' + argv[1]).json()

    # get total number of tasks [used to get len of all tasks in line 18]
    todos = requests.get(endpoint + '/todos?userId=' + argv[1]).json()

    result = {}
    result[argv[1]] = [{
        "task": task.get('title'),
        "completed": task.get('completed'),
        "username": user_res.get('username'),
    } for task in todos]

    with open("{}.json".format(argv[1]), "w") as outfile:
        json.dump(result, outfile)
