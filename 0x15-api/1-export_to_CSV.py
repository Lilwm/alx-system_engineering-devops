#!/usr/bin/python3
'''
Python script using REST API.
'''
import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) >= 2 and sys.argv[1].isdigit():
        user = sys.argv[1]
        url = "https://jsonplaceholder.typicode.com/users/" + user
        repo = requests.get(url)
        username = repo.json().get("username")

        url = "https://jsonplaceholder.typicode.com/users/" + user + "/todos"
        repo = requests.get(url)

        with open('{}.csv'.format(user), 'w') as f:
            for element in repo.json():
                f.write('"{}","{}","{}","{}"\n'.
                        format(user, username, element.get("completed"),
                               element.get("title")))