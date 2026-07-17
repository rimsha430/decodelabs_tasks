my_tasks = []

def add_task(task):
    """Adds a new task to the list (INSERT operation)."""
    if task.strip() == "":
        print("Task cannot be empty. Please try again.")
        return

    my_tasks.append(task.strip())
    print(f"Task added: '{task.strip()}'")


def view_tasks():
    """Displays all tasks with their index (READ operation)."""
    print("\n----- YOUR TO-DO LIST -----")

    if not my_tasks:
        print("No tasks yet. Add one!")
    else:
        # enumerate() gives both index (ID) and value (Data) together
        for index, task in enumerate(my_tasks):
            print(f"{index + 1}. {task}")

    print("----------------------------\n")


def remove_task(task_number):
    """Removes a task by its displayed number (DELETE operation)."""
    try:
        task_number = int(task_number)

        if 1 <= task_number <= len(my_tasks):
            removed = my_tasks.pop(task_number - 1)
            print(f"Removed: '{removed}'")
        else:
            print("Invalid task number.")

    except ValueError:
        print("Please enter a valid number.")


def show_menu():
    """Displays the main menu options."""
    print("=" * 30)
    print("   DECODELABS TO-DO LIST")
    print("=" * 30)
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")


def main():
    """Main program loop - the entry point of the application."""
    while True:
        show_menu()
        choice = input("Choose an option (1-4): ").strip()

        if choice == "1":
            task = input("Enter your task: ")
            add_task(task)

        elif choice == "2":
            view_tasks()

        elif choice == "3":
            view_tasks()

            if my_tasks:
                task_num = input("Enter task number to remove: ")
                remove_task(task_num)

        elif choice == "4":
            print("Goodbye! Your session tasks were temporary (RAM).")
            break

        else:
            print("Invalid choice. Please select 1-4.\n")


# Gatekeeper: ensures main() only runs when this file is executed directly
if __name__ == "__main__":
    main()