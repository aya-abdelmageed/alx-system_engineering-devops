#!/usr/bin/python3
""" using this REST API, for a given employee ID,
returns information about his/her TODO list progress """

from requests import get
from sys import argv


if __name__ == '__main__':
    userId = argv[1]
    user = get("https://jsonplaceholder.typicode.com/users/{}"
               .format(userId))

    name = user.json().get('name')

    todos = get('https://jsonplaceholder.typicode.com/todos')
    total = 0
    comp = 0

    for task in todos.json():
        if task.get('userId') == int(userId):
            total += 1
            if task.get('completed'):
                comp += 1

    print('Employee {} is done with tasks({}/{}):'
          .format(name, comp, total))

    print('\n'.join(["\t " + task.get('title') for task in todos.json()
          if task.get('userId') == int(userId) and task.get('completed')]))
