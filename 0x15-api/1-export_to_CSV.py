#!/usr/bin/python3
''' gather data from an API '''
import csv
import requests
from sys import argv

if __name__ == '__main__':
    # get employee response [used to get name in line 19]
    endpoint = 'https://jsonplaceholder.typicode.com'
    user_res = requests.get(endpoint + '/users/' + argv[1]).json()

    # get total number of tasks [used to get len of all tasks in line 18]
    todos = requests.get(endpoint + '/todos?userId=' + argv[1]).json()

    with open(f"{argv[1]}.csv", "w") as data_file:
        fields = ["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"]
        writer = csv.DictWriter(data_file, fields,
                                quotechar='"', quoting=csv.QUOTE_ALL)

        writer.writerows({
            "USER_ID": argv[1],
            "USERNAME": user_res.get('username'),
            "TASK_COMPLETED_STATUS": task.get('completed'),
            "TASK_TITLE": task.get('title')
        } for task in todos)
