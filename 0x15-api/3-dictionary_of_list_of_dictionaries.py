#!/usr/bin/python3
""" accepts employee IDs and returns todo list"""

import json
import requests


def gather_data_from_an_API(employee_id):
    """
    accepts employee ID and returns employee's TODO list progress.

    :param employee_id: ID of the employee
    :return: information about employee's TODO list progress
    """
    # API endpoint to get all tasks
    url = f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"
    # Get response from API
    response = requests.get(url)
    # Check if the API call was successful
    if response.status_code == 200:
        # Convert API response to JSON
        todos = response.json()
        # API endpoint to get employee information
        url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
        # Get response from API
        response = requests.get(url)
        # Convert API response to JSON
        user = response.json()
        # Get employee name
        employee_name = user["username"]
        # Get completed tasks
        completed_tasks = [todo for todo in todos if todo["completed"]]
        # Get total number of tasks
        total_tasks = len(todos)
        # Get number of completed tasks
        completed_tasks_count = len(completed_tasks)
        # Return employee TODO list progress
        return {
                "employee_name": employee_name,
                "completed_tasks_count": completed_tasks_count,
                "total_tasks": total_tasks,
                "completed_tasks": completed_tasks
        }
    else:
        # If API call was not successful, return None
        return None


def export_data_to_json(employee_id):
    """
    Accepts employee ID and exports the TODO list progress in JSON format.

    :param employee_id: ID of the employee
    :return: None
    """
    # Get employee TODO list progress
    data = gather_data_from_an_API(employee_id)
    # Check if data was returned
    if data:
        # Create a list to store task data
        task_data = []
        # Get employee name
        employee_name = data["employee_name"]
        # Get completed tasks
        completed_tasks = data["completed_tasks"]
        # Loop through completed tasks
        for task in completed_tasks:
            task_data.append({"username": employee_name, "task": task["title"], 
                "completed": task["completed"]})
        # Create a dictionary to store all task data
        todo_data = {employee_id: task_data}
        # Export data to JSON file
        with open(f"{employee_id}.json", "w") as file:
            json.dump
