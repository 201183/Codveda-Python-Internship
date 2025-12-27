import json
TASK_FILE = "tasks.json"
# Load tasks from file
try:
    with open(TASK_FILE, "r") as file:
        tasks = json.load(file)
except (FileNotFoundError, json.JSONDecodeError):
    tasks = []

def save_tasks():
    with open(TASK_FILE, "w") as file:
        json.dump(tasks, file, indent=4)

def show_tasks():
    if not tasks:
        print("No tasks available.")
        return
    print("\n--- Tasks ---")
    for i, task in enumerate(tasks, 1):
        status = "Done" if task["completed"] else "Pending"
        print(f"{i}. {task['title']} - {status}")

def add_task():
    title = input("Enter task title: ").strip()
    if title:
        tasks.append({"title": title, "completed": False})
        save_tasks()
        print("Task added successfully!")
    else:
        print("Task title cannot be empty.")

def delete_task():
    show_tasks()
    try:
        choice = int(input("Enter task number to delete: "))
        if 1 <= choice <= len(tasks):
            removed = tasks.pop(choice - 1)
            save_tasks()
            print(f"Task '{removed['title']}' deleted!")
        else:
            print("Invalid task number!")
    except ValueError:
        print("Please enter a valid number.")

def mark_done():
    show_tasks()
    try:
        choice = int(input("Enter task number to mark as done: "))
        if 1 <= choice <= len(tasks):
            if tasks[choice - 1]["completed"]:
                print("Task already completed!")
            else:
                tasks[choice - 1]["completed"] = True
                save_tasks()
                print(f"Task '{tasks[choice - 1]['title']}' marked as done!")
        else:
            print("Invalid task number!")
    except ValueError:
        print("Please enter a valid number.")
# Main menu
while True:
    print("\n1. Show Tasks\n2. Add Task\n3. Delete Task\n4. Mark Task as Done\n5. Exit")
    try:
        choice = int(input("Select an option: "))
        if choice == 1:
            show_tasks()
        elif choice == 2:
            add_task()
        elif choice == 3:
            delete_task()
        elif choice == 4:
            mark_done()
        elif choice == 5:
            print("Exiting...")
            break
        else:
            print("Invalid option!")
    except ValueError:
        print("Please enter a number.")
