import requests
import json

def todo_lists_all_employees():
    # Get information about all employees
    employee_response = requests.get("https://jsonplaceholder.typicode.com/users")
    employee_data = employee_response.json()
    employee_map = {employee["id"]: employee["username"] for employee in employee_data}
    
    # Get TODO lists for all employees
    todo_response = requests.get("https://jsonplaceholder.typicode.com/todos")
    todo_data = todo_response.json()
    
    # Write the TODO list data to a JSON file
    with open("todo_all_employees.json", "w") as jsonfile:
        tasks = {}
        for task in todo_data:
            user_id = task["userId"]
            if user_id not in tasks:
                tasks[user_id] = []
            tasks[user_id].append({"username": employee_map[user_id], "task": task["title"], "completed": task["completed"]})
        json.dump(tasks, jsonfile)

if __name__ == "__main__":
    todo_lists_all_employees()

