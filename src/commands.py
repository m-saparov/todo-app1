from datetime import datetime
from rich.console import Console
from rich.table import Table

from .storage import (
    create_task,
    get_tasks,
    update_task_by_id,
    delete_task_by_id,
    mark_task_completed,
)

console = Console()


def add_task():
    name = input("Task name: ").strip().capitalize()
    description = input("Description: ").strip().capitalize()
    category = input("Category: ").strip().title()
    due_date = input("Date (example: 2025/10/11): ")

    due_date = datetime.strptime(due_date, "%Y/%m/%d")
    if due_date < datetime.now():
        print("Date shoulde be greater than or equal to now.")
        return

    create_task(name, description, category, due_date)
    print("✅ Vazifa muvaffaqiyatli qo'shildi!")


def show_tasks():
    tasks = get_tasks()

    if not tasks:
        print("Hech qanday task yo'q!")
        return

    console = Console()

    table = Table(title="All Tasks")
    table.add_column("ID")
    table.add_column("Name")
    table.add_column("Category")
    table.add_column("Status")
    table.add_column("Due Date")

    for task in tasks:
        task_status = "❌Incompleted"
        if task["status"]:
            task_status = "✅ Completed"
        du_date = task["due_date"].strftime("%d/%m/%Y")
        table.add_row(str(task["id"]), task["name"], task["category"], task_status, du_date)
    
    console.print(table)

    task_id_str = input("Task detail (id): ").strip()
    if not task_id_str.isdigit():
        print("ID raqam bo'lishi kerak.")
        return

    task_id = int(task_id_str)
    task = None
    for t in tasks:
        if t["id"] == task_id:
            task = t
            break

    if not task:
        print("Bunday ID topilmadi!")
        return
    
    status = "❌Incompleted"
    if task["status"]:
        status = "✅ Completed"
    du_date = task["due_date"].strftime("%d/%m/%Y")
    created_date = task["created_date"].strftime("%d/%m/%Y, %H:%M:%S")

    print(f"Task name: {task['name']}")
    print(f"Description: {task['description']}")
    print(f"Category: {task['category']}")
    print(f"Status: {status}")
    print(f"Due Date: {du_date}")
    print(f"Created Date: {created_date}")
    
    print()


def update_task():
    tasks = get_tasks()
    if not tasks:
        print("Hech qanday vazifa yo'q!")
        return

    task_id = input("Yangi ma'lumot kiritiladigan task ID: ").strip()
    if not task_id.isdigit():
        print("ID raqam bo'lishi kerak.")
        return
    task_id = int(task_id)

    task = None
    for t in tasks:
        if t["id"] == task_id:
            task = t
            break

    if not task:
        print("Bunday ID topilmadi!")
        return

    name = input(f"New name ({task['name']}): ").strip().capitalize()
    if not name:
        name = task["name"]

    description = input(f"New description ({task['description']}): ").strip().capitalize()
    if not description:
        description = task["description"]

    category = input(f"New category ({task['category']}): ").strip().title()
    if not category:
        category = task["category"]

    due_date_str = input(f"New due date ({task['due_date'].strftime('%Y/%m/%d')}): ").strip()
    due_date = task["due_date"]

    if due_date_str:
        if len(due_date_str) != 10 or due_date_str[4] != "/" or due_date_str[7] != "/":
            print("Sana formati noto'g'ri! Masalan: 2025/10/11")
            return

        parts = due_date_str.split("/")
        if len(parts) != 3 or not all(p.isdigit() for p in parts):
            print("Sana faqat raqamlardan iborat bo'lishi kerak!")
            return

        year, month, day = map(int, parts)
        current_year = datetime.now().year

        if not (1 <= month <= 12 and 1 <= day <= 31 and year >= current_year):
            print("yil-oy-kun (formatni tekshiring!)")
            return

        due_date = datetime(year, month, day)

        if due_date < datetime.now():
            print("Sana hozirgi kundan kichik bo'lishi mumkin emas.")
            return

    update_task_by_id(task_id, name, description, category, due_date)
    print("Task yangilandi!")


def delete_task():
    tasks = get_tasks()
    if not tasks:
        print("Hech qanday vazifa yo'q.")
        return

    task_id = input("O'chiriladigan task ID: ").strip()
    if not task_id.isdigit():
        print("ID raqam bo'lishi kerak.")
        return

    delete_task_by_id(int(task_id))
    print("Task muvaffaqiyatli o'chirildi!")


def mark_completed():
    task_id = input("Bajarilgan deb belgilash uchun task ID: ").strip()
    if not task_id.isdigit():
        print("ID raqam bo'lishi kerak.")
        return

    task_id_int = int(task_id)
    success = mark_task_completed(task_id_int)
    if success:
        print("Task completed sifatida belgilandi!")
    else:
        print("Bunday ID topilmadi!")
