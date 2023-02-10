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
        name = repo.json().get("name")

        url = "https://jsonplaceholder.typicode.com/users/" + user + "/todos"
        repo = requests.get(url)
        done = len([todo for todo in repo.json() if todo.get("completed")])
        total = len(repo.json())

        first = True
        for element in repo.json():
            if first:
                print("Employee {} is done with tasks({}/{}):".
                      format(name, done, total))
                first = False
            if element.get("completed"):
                print("\t {}".format(element.get("title")))