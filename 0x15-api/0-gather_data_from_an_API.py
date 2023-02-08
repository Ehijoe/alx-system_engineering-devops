#!/usr/bin/python3
''' Show the TODO list progress of an employee '''
import json
from sys import argv
from urllib.request import urlopen


if __name__ == '__main__':
    if len(argv) < 2:
        print(f"Usage: {argv[0]} employee_id")
        exit(1)

    Employee = int(argv[1])

    # Get the Employee Todolist
    todos = urlopen(
        f"https://jsonplaceholder.typicode.com/todos?userId={Employee}"
    ).read()
    todos = json.loads(todos)

    # Get the Employee details
    Employee = urlopen(
        f"https://jsonplaceholder.typicode.com/users/{Employee}"
    ).read()
    Employee = json.loads(Employee)

    # Count Todos
    completed = [todo for todo in todos if todo.get('completed')]
    done = len(completed)
    total = len(todos)

    print(
        f"Employee {Employee.get('name')} is done with tasks({done}/{total}):"
    )
    for task in completed:
        print(f"\t {task.get('title')}")
