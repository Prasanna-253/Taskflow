tasks = []
task_id = 1

# To show the tasks that's been added in the list tasks
def show_tasks():
    print("Tasks:")
    for t in tasks:
        print(f"{t['id']}: {t['title']}")
    if not tasks:
        print("No tasks yet!")

# Appending the titles to the list
def add_task(title):
    global task_id
    new_task = {"id": task_id, "title": title}
    tasks.append(new_task)
    task_id += 1
    print("Task added:", new_task)

# Removing the tasks using the tid's
def delete_task(tid):
    found = None
    for t in tasks:
        if t["id"] == tid:
            found = t
            break
    if found:
        tasks.remove(found)
        print("Deleted:", found)
    else:
        print("Task not found")

# This allows the user to use the program until they want to exit
while True:
    print("\n1. Show tasks")
    print("2. Add task")
    print("3. Delete task")
    print("4. Exit")
    choice = input("Choose: ")

    if choice == "1":
        show_tasks()
    elif choice == "2":
        title = input("Enter task title: ")
        add_task(title)

# Raising a ValueError to get a input in integer
    elif choice == "3":
        if tasks == []:
            print("There's no tasks to delete, please add some tasks!!!")
        else:
            tid_input = input("Enter task id to delete: ")
            try:
                tid = int(tid_input)
                delete_task(tid)
            except ValueError:
                print("Enter a valid id to delete (only numbers allowed)")    
    elif choice == "4":
        print("Thanks for using the Task Manager!!!")
        break
    else:
        print("Invalid choice")

    
