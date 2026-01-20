import json

try:
    with open("tasks.json", "r") as file:
        tasks = json.load(file)
except:
    tasks = []
    
def save_tasks():
    with open("tasks.json", "w") as file:
        json.dump(tasks, file, indent=4)




def add_task():
    title = input("Task name: ")

    
    assigned = input("Assigned to: ")
    priority = input("Priority (Low / Medium / High): ")
    due = input("Due date (DD/MM/YYYY): ")

    task = {
        "title": title,
        "assigned": assigned,
        "priority": priority,
        "due": due,
        "status": "Pending"
    }

    tasks.append(task)
    save_tasks()
    print("Task added.\n")



def view_tasks():
    if not tasks:
        print("No tasks yet.\n")
        return

    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task['title']} | {task['assigned']} | {task['priority']} | {task['due']} | {task['status']}")
    print()


def complete_task():
    view_tasks()
    num = int(input("Enter task number to mark completed: "))
    tasks[num - 1]["status"] = "Completed"
    save_tasks()
    print("Task updated.\n")
 
while True:
    print("---- Task Tracker ----")
    print("1. Add task")
    print("2. View tasks")
    print("3. Complete task")
    print("4. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        add_task()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        complete_task()
    elif choice == "4":
        break
    else:
        print("Invalid option\n")
