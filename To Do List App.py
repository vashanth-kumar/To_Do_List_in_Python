print("\n\t\t\tWelcome To Do List App")

tasks = []

def add_task(task):
    tasks.append(task)
    print("Task added!")

def view_tasks():
    if len(tasks) == 0:
        print("No tasks to display!")
    else:
        for i, task in enumerate(tasks):
            print(f"{i+1}. {task}")

def remove_task(index):
    try:
        task = tasks.pop(index-1)
        print(f"{task} removed!")
    except IndexError:
        print("Invalid task number!")

while True:
    print("1. Add task")
    print("2. View tasks")
    print("3. Remove task")
    print("4. Exit")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        task = input("Enter task: ")
        add_task(task)
    elif choice == 2:
        view_tasks()
    elif choice == 3:
        index = int(input("Enter task number to remove: "))
        remove_task(index)
    elif choice == 4:
        break
    else:
        print("Invalid choice!")
