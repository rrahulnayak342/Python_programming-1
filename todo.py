# Simple To-Do List Application in Python

todo_list = []

def show_menu():
    print("\n==== TO-DO LIST MENU ====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Mark Task as Completed")
    print("6. Exit")

def add_task():
    task = input("Enter a new task: ")
    todo_list.append({"task": task, "status": "Pending"})
    print("Task added successfully!")

def view_tasks():
    if not todo_list:
        print("No tasks found!")
        return
    print("\nYour Tasks:")
    for index, item in enumerate(todo_list, start=1):
        print(f"{index}. {item['task']} - [{item['status']}]")

def update_task():
    view_tasks()
    try:
        task_no = int(input("\nEnter task number to update: "))
        new_task = input("Enter new task name: ")
        todo_list[task_no - 1]["task"] = new_task
        print("Task updated successfully!")
    except:
        print("Invalid task number!")

def delete_task():
    view_tasks()
    try:
        task_no = int(input("\nEnter task number to delete: "))
        todo_list.pop(task_no - 1)
        print("Task deleted successfully!")
    except:
        print("Invalid task number!")

def mark_completed():
    view_tasks()
    try:
        task_no = int(input("\nEnter task number to mark completed: "))
        todo_list[task_no - 1]["status"] = "Completed"
        print("Task marked as completed!")
    except:
        print("Invalid task number!")

# -------- Main Program Loop --------
while True:
    show_menu()
    choice = input("Enter your choice: ")

    if choice == "1":
        add_task()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        update_task()
    elif choice == "4":
        delete_task()
    elif choice == "5":
        mark_completed()
    elif choice == "6":
        print("Exiting... Thank you!")
        break
    else:
        print("Invalid choice! Please try again.")
