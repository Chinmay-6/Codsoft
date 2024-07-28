#Data structure to save tasks
tasks = []
1
'''Create functions for adding, removing, and displaying tasks'''
def add_task(task):
#To Addd task
    tasks.append(task)
    print(f"Task '{task}' added.")

def remove_task(task):
#To remove task
    if task in tasks:
        tasks.remove(task)
        print(f"Task '{task}' removed.")
    else:
        print(f"Task '{task}' not found in the list.")

def display_tasks():
#To display tasks
    if tasks:
        print("Tasks:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")
    else:
        print("The to-do list is empty.")

#Main program to select Options
while True:
    print("\nOptions:")
    print("1. Add task")
    print("2. Remove task")
    print("3. Display tasks")
    print("4. Exit")
    choice = input("Choose an option: ")

    if choice == '1':
        task = input("Enter a task: ")
        add_task(task)
    elif choice == '2':
        task = input("Enter the task to remove: ")
        remove_task(task)
    elif choice == '3':
        display_tasks()
    elif choice == '4':
        print("Exiting the to-do list application.")
        break
    else:
        print("Invalid choice. Please choose again.")


