import json
import os

FILE_NAME = "tasks.json"

def load_tasks():
    if not os.path.exists(FILE_NAME):
        return []
    with open(FILE_NAME, "r") as file:
        return json.load(file)

def save_tasks(tasks):
    with open(FILE_NAME, "w") as file:
        json.dump(tasks, file, indent=4)

def add_task():
    task = input("Enter task: ")
    tasks = load_tasks()
    tasks.append({"task": task, "done": False})
    save_tasks(tasks)
    print("✅ Task added successfully!")

def view_tasks():
    tasks = load_tasks()
    if not tasks:
        print("No tasks available.")
        return
    for i, task in enumerate(tasks, start=1):
        status = "✔" if task["done"] else "❌"
        print(f"{i}. {task['task']} [{status}]")

def mark_done():
    view_tasks()
    tasks = load_tasks()
    try:
        choice = int(input("Enter task number to mark as done: "))
        tasks[choice - 1]["done"] = True
        save_tasks(tasks)
        print("✅ Task marked as completed!")
    except (IndexError, ValueError):
        print("❌ Invalid task number.")

def delete_task():
    view_tasks()
    tasks = load_tasks()
    try:
        choice = int(input("Enter task number to delete: "))
        tasks.pop(choice - 1)
        save_tasks(tasks)
        print("🗑 Task deleted successfully!")
    except (IndexError, ValueError):
        print("❌ Invalid task number.")

def main():
    while True:
        print("\n--- TO-DO LIST MENU ---")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Done")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            mark_done()
        elif choice == "4":
            delete_task()
        elif choice == "5":
            print("👋 Exiting To-Do List. Goodbye!")
            break
        else:
            print("❌ Invalid choice. Try again.")

if __name__ == "__main__":
    main()
