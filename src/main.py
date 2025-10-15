from .commands import (
    add_task,
    show_tasks,
    update_task,
    delete_task,
    mark_completed
)


def print_menu():
    print("\n--- TODO CLI ---")
    print("1. Add Task")
    print("2. List Tasks")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Mark Completed")
    print("6. Exit\n")


def main():
    while True:
        print_menu()
        choice = input("Select option: ").strip()

        if choice == "1":
            add_task()
        elif choice == "2":
            show_tasks()
        elif choice == "3":
            update_task()
        elif choice == "4":
            delete_task()
        elif choice == "5":
            mark_completed()
        elif choice == "6":
            print("Dasturdan chiqildi.")
            break
        else:
            print("❌ Noto'g'ri tanlov!")
