#!/usr/bin/python3
"""" gets employees tasks from REST API"""
import requests
import sys


def todo_list_progress(user_id):
    # Get the employee information
    emp_url = "https://jsonplaceholder.typicode.com/users/" + user_id
    employee_response = requests.get(emp_url)
    name = employee_response.json().get("name")

    # Get the TODO list for the employee
    todo_url = "https://jsonplaceholder.typicode.com/users/" user_id + "/todos"
    todo_response = requests.get(todo_url)
    todo_data = todo_response.json()    
    # Count the number of completed tasks
    completed_tasks = [task for task in todo_data if task["completed"] is True]
    total_tasks = len(todo_data)
    done_tasks = len(completed_tasks)
    # Display the employee TODO list progress
    print(f"Employee {name} is done with tasks({done_tasks}/{total_tasks}):")
    for task in completed_tasks:
        print(f"\t {task['title']}")


if __name__ == "__main__":
    if len(sys.argv) == 2:
        employee_id = int(sys.argv[1])
        todo_list_progress(employee_id)
    else:
        print("Please provide the employee ID as a command-line argument.")
