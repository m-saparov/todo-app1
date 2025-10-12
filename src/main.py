import sys
from src.commands import add_task, list_tasks, update_task, delete_task, mark_completed


def print_menu():
    print("\n--- TODO CLI ---")
    print("1. Add Task")
    print("2. List Tasks")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Mark Completed")
    print("6. Exit")


def main():
    while True:
        print_menu()
        choice = input("Select option: ").strip()

        if choice == "1":
            name = input("Task name: ").strip()
            description = input("Description: ").strip()
            category = input("Category: ").strip()
            add_task(name, description, category)

        elif choice == "2":
            list_tasks()

        elif choice == "3":
            task_id = int(input("Enter Task ID: "))
            name = input("New name (leave empty to skip): ").strip()
            description = input("New description (leave empty to skip): ").strip()
            category = input("New category (leave empty to skip): ").strip()
            update_task(task_id, name or None, description or None, category or None)

        elif choice == "4":
            task_id = int(input("Enter Task ID: "))
            delete_task(task_id)

        elif choice == "5":
            task_id = int(input("Enter Task ID: "))
            mark_completed(task_id)

        elif choice == "6":
            print("Dasturdan chiqildi.")
            sys.exit()

        else:
            print("Noto'g'ri tanlov, qaytadan urinib ko'ring.")
