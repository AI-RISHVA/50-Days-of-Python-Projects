# Simple To-Do List App
# File: todo.py

def show_tasks():
    try:
        f = open("tasks.txt", "r")
        tasks = f.readlines()
        f.close()

        if len(tasks) == 0:
            print("No tasks yet!")
        else:
            print("\nYour Tasks:")
            for i, t in enumerate(tasks, 1):
                print(i, t.strip())
    except FileNotFoundError:
        print("No tasks file found!")

def add_task():
    task = input("Enter new task: ")
    f = open("tasks.txt", "a")
    f.write(task + "\n")
    f.close()
    print("Task added!")

def delete_task():
    show_tasks()
    num = int(input("Enter task number to delete: "))

    f = open("tasks.txt", "r")
    tasks = f.readlines()
    f.close()

    if 1 <= num <= len(tasks):
        removed = tasks.pop(num-1)
        f = open("tasks.txt", "w")
        f.writelines(tasks)
        f.close()
        print("Deleted:", removed.strip())
    else:
        print("Wrong number!")

def main():
    while True:
        print("\n--- To-Do App ---")
        print("1. Show Tasks")
        print("2. Add Task")
        print("3. Delete Task")
        print("4. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            show_tasks()
        elif choice == "2":
            add_task()
        elif choice == "3":
            delete_task()
        elif choice == "4":
            print("Bye!")
            break
        else:
            print("Invalid choice!")

main()
