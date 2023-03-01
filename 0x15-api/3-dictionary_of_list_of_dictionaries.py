#!/usr/bin/python3
'''
Python script that, using REST API.
'''


if __name__ == "__main__":

    import json
    import requests
    import sys

    users = requests.get("https://jsonplaceholder.typicode.com/users")
    users = users.json()
    todos = requests.get('https://jsonplaceholder.typicode.com/todos')
    todos = todos.json()
    todo = {}

    for user in users:
        cust = []
        for elementos in todos:
            if elementos.get('userId') == user.get('id'):
                task = {"username": user.get('username'),
                        "task": elementos.get('title'),
                        "completed": elementos.get('completed')}
                cust.append(task)
        todo[user.get('id')] = cust

    with open('todo_all_employees.json', mode='w') as f:
        json.dump(todo, f)
