# Simple CLI To-Do List Application

def show_menu():
    # Displays options menu to the user
    print("\nWelcome to the My To-Do List App")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Remove Task")
    print("4. Exit")

def display_tasks(tasks):
    # Displays stored tasks or a message if empty
    if not tasks:
        print("\nYour task list is empty!")
    else:
        print("\nMy Current Tasks")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")

def main():
    tasks = []  # List store for task items

    while True:
        show_menu()
        choice = input("Enter choice (1-4): ")

        if choice == "1":
            display_tasks(tasks)

        elif choice == "2":
            new_task = input("\nEnter task description: ").strip()
            if new_task:
                tasks.append(new_task)
                print(f"✓ Task '{new_task}' added successfully.")
            else:
                print("Task cannot be blank!")

        elif choice == "3":
            display_tasks(tasks)
            if tasks:
                task_num_input = input("\nEnter task number to remove: ")
                if task_num_input.isdigit():
                    task_num = int(task_num_input)
                    if 1 <= task_num <= len(tasks):
                        removed_task = tasks.pop(task_num - 1)
                        print(f"✓ Task '{removed_task}' removed.")
                    else:
                        print("Invalid task number!")
                else:
                    print("Please enter a valid whole number!")

        elif choice == "4":
            print("\nGoodbye! Happy productivity.")
            break

        else:
            print("Invalid selection! Please enter a number from 1 to 4.")

if __name__ == "__main__":
    main()