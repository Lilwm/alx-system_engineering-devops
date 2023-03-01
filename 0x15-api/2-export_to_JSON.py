#!/usr/bin/python3
'''
Python script using REST API.
'''


if __name__ == "__main__":
    import json
    import requests
    import sys

    if len(sys.argv) >= 2 and sys.argv[1].isdigit():
        user = sys.argv[1]
        url = "https://jsonplaceholder.typicode.com/users/" + user
        repo = requests.get(url)
        username = repo.json().get("username")

        url = "https://jsonplaceholder.typicode.com/users/" + user + "/todos"
        repo = requests.get(url)

        todo = {}
        cust = []
        for element in repo.json():
            s = {"task": element.get('title'),
                 "completed": element.get('completed'),
                 "username": username}
            cust.append(s)
        todo[user] = cust

        with open('{}.json'.format(user), 'w') as f:
            json.dump(todo, f)