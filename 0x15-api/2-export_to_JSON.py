import requests
import sys
import json

def todo_list_progress(employee_id):
    # Get the employee information
    employee_response = requests.get(f"https://jsonplaceholder.typicode.com/users/{employee_id}")
    employee_data = employee_response.json()
    employee_username = employee_data["username"]
    
    # Get the TODO list for the employee
    todo_response = requests.get(f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}")
    todo_data = todo_response.json()
    
    # Write the TODO list data to a JSON file
    with open(f"{employee_id}.json", "w") as jsonfile:
        tasks = [{"task": task["title"], "completed": task["completed"], "username": employee_username} for task in todo_data]
        json.dump({employee_id: tasks}, jsonfile)

if __name__ == "__main__":
    # Get the employee ID from the script arguments
    employee_id = int(sys.argv[1])
    todo_list_progress(employee_id)

